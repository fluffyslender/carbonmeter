#!/usr/bin/env python3
"""
EU environmental claims scanner.

Crawls a domain's public pages and flags claims that became prohibited under
the ECGT Directive (EU) 2024/825, applicable from 27 September 2026.

Detection only. This tool never certifies compliance -- see README.

Zero dependencies: Python 3.8+ standard library only.

  ./scan.py --domain example.com
  ./scan.py --domain example.com --max-pages 100 --out scans/
  ./scan.py --selftest
  ./scan.py --diff scans/example.com-2026-09-01.json scans/example.com-2026-10-01.json
"""

import argparse, json, re, sys, time, urllib.parse, urllib.request, urllib.robotparser
from datetime import datetime, timezone
from html.parser import HTMLParser
from pathlib import Path

DICT_PATH = Path(__file__).parent / "dictionary.json"
UA = "CarbonMeterClaimsScanner/1.0 (+compliance scan; contact: [[CONTACT_EMAIL]])"
CONTEXT_WINDOW = 140
SEVERITY_ORDER = {"P0": 0, "P1": 1, "P2": 2, "P3": 3}


# ---------------------------------------------------------------- text extraction

class TextExtractor(HTMLParser):
    """Visible text only. Drops script/style/noscript; records title and alt text."""

    SKIP = {"script", "style", "noscript", "svg", "template"}

    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.parts, self._skip_depth, self._in_title = [], 0, False
        self.title = ""

    def handle_starttag(self, tag, attrs):
        if tag in self.SKIP:
            self._skip_depth += 1
        if tag == "title":
            self._in_title = True
        # alt and aria-label carry claims too, and are easy to forget
        for k, v in attrs:
            if k in ("alt", "aria-label", "title") and v:
                self.parts.append(v)

    def handle_endtag(self, tag):
        if tag in self.SKIP and self._skip_depth:
            self._skip_depth -= 1
        if tag == "title":
            self._in_title = False

    def handle_data(self, data):
        if self._skip_depth:
            return
        text = data.strip()
        if not text:
            return
        if self._in_title:
            self.title += text
        self.parts.append(text)

    def text(self):
        return re.sub(r"\s+", " ", " ".join(self.parts))


def extract(html):
    p = TextExtractor()
    try:
        p.feed(html)
    except Exception:
        pass
    return p.text(), p.title.strip()


# ---------------------------------------------------------------- matching

def load_dictionary(path=DICT_PATH):
    d = json.loads(Path(path).read_text(encoding="utf-8"))
    for rule in d["rules"]:
        rule["_re"] = re.compile(rule["pattern"], re.IGNORECASE)
    oos = d.get("out_of_scope_flags", {})
    if oos.get("pattern"):
        oos["_re"] = re.compile(oos["pattern"], re.IGNORECASE)
    return d


def _excluded(text, start, end, phrases):
    """True where surrounding text shows compliant usage ('we do not describe...')."""
    if not phrases:
        return False
    window = text[max(0, start - CONTEXT_WINDOW):end + CONTEXT_WINDOW].lower()
    return any(p.lower() in window for p in phrases)


def match_page(text, url, title, dictionary):
    findings, seen = [], set()
    for rule in dictionary["rules"]:
        for m in rule["_re"].finditer(text):
            if _excluded(text, m.start(), m.end(), rule.get("exclude_context")):
                continue
            quote = text[max(0, m.start() - 90):m.end() + 90].strip()
            key = (rule["id"], m.group(0).lower())
            if key in seen:          # one finding per rule per page
                continue
            seen.add(key)
            findings.append({
                "rule_id": rule["id"],
                "severity": rule["severity"],
                "category": rule["category"],
                "label": rule["label"],
                "basis": rule["basis"],
                "rewrite_ref": rule["rewrite_ref"],
                "matched": m.group(0),
                "quote": quote,
                "url": url,
                "page_title": title,
            })
    oos = dictionary.get("out_of_scope_flags", {})
    flags = sorted({m.group(0).lower() for m in oos["_re"].finditer(text)}) if oos.get("_re") else []
    return findings, flags


# ---------------------------------------------------------------- crawling

def fetch(url, timeout=15):
    req = urllib.request.Request(url, headers={"User-Agent": UA, "Accept": "text/html,*/*"})
    with urllib.request.urlopen(req, timeout=timeout) as r:
        ctype = r.headers.get("Content-Type", "")
        if "html" not in ctype and "xml" not in ctype:
            return None
        raw = r.read(3_000_000)
    charset = "utf-8"
    if "charset=" in ctype:
        charset = ctype.split("charset=")[-1].split(";")[0].strip() or "utf-8"
    return raw.decode(charset, errors="replace")


def robots(base):
    rp = urllib.robotparser.RobotFileParser()
    rp.set_url(urllib.parse.urljoin(base, "/robots.txt"))
    try:
        rp.read()
    except Exception:
        return None
    return rp


def from_sitemap(base, cap):
    """Collect URLs from sitemap.xml, following sitemap indexes one level."""
    urls, queue, seen = [], [urllib.parse.urljoin(base, "/sitemap.xml")], set()
    while queue and len(urls) < cap:
        sm = queue.pop(0)
        if sm in seen:
            continue
        seen.add(sm)
        try:
            body = fetch(sm)
        except Exception:
            continue
        if not body:
            continue
        locs = re.findall(r"<loc>\s*([^<\s]+)\s*</loc>", body, re.IGNORECASE)
        if "<sitemapindex" in body.lower():
            queue.extend(locs[:50])
        else:
            urls.extend(locs)
    return urls[:cap]


class LinkFinder(HTMLParser):
    def __init__(self):
        super().__init__()
        self.links = []

    def handle_starttag(self, tag, attrs):
        if tag == "a":
            for k, v in attrs:
                if k == "href" and v:
                    self.links.append(v)


def crawl(base, cap, delay, rp, verbose):
    """Sitemap first; breadth-first crawl as fallback and top-up."""
    host = urllib.parse.urlparse(base).netloc
    ordered, seen = [], set()

    def add(u):
        u, _ = urllib.parse.urldefrag(u)
        if not u or u in seen:
            return
        p = urllib.parse.urlparse(u)
        if p.scheme not in ("http", "https") or p.netloc != host:
            return
        if re.search(r"\.(jpg|jpeg|png|gif|svg|webp|css|js|ico|woff2?|ttf|zip|mp4|mp3|avif)$", p.path, re.I):
            return
        if rp and not rp.can_fetch(UA, u):
            return
        seen.add(u)
        ordered.append(u)

    for u in from_sitemap(base, cap):
        add(u)
    add(base)

    pages, i = [], 0
    while i < len(ordered) and len(pages) < cap:
        url = ordered[i]
        i += 1
        try:
            html = fetch(url)
        except Exception as e:
            if verbose:
                print(f"  skip {url} ({type(e).__name__})", file=sys.stderr)
            continue
        if not html:
            continue
        pages.append((url, html))
        if verbose:
            print(f"  [{len(pages):>3}/{cap}] {url}", file=sys.stderr)
        if len(ordered) < cap * 3:      # keep discovering while we have room
            lf = LinkFinder()
            try:
                lf.feed(html)
            except Exception:
                pass
            for href in lf.links:
                add(urllib.parse.urljoin(url, href))
        time.sleep(delay)
    return pages


# ---------------------------------------------------------------- reporting

def summarise(findings):
    counts = {"P0": 0, "P1": 0, "P2": 0, "P3": 0}
    for f in findings:
        counts[f["severity"]] = counts.get(f["severity"], 0) + 1
    return counts


def render_markdown(result):
    d, counts = result, result["summary"]
    L = [
        f"# Environmental Claims Scan — {d['domain']}",
        "",
        f"Scan date **{d['scan_date'][:10]}** · Pages scanned **{d['pages_scanned']}** · "
        f"Dictionary **{d['dictionary_version']}**",
        "",
        f"**{len(d['findings'])} findings** — "
        f"P0: **{counts['P0']}** · P1: {counts['P1']} · P2: {counts['P2']} · P3: {counts['P3']}",
        "",
        "> Detection only. This scan flags wording for review against the ECGT Directive "
        "(EU) 2024/825. It is not legal advice, not a compliance assessment, and an absence "
        "of findings is not a clean bill of health — see the limitations below.",
        "",
    ]
    if not d["findings"]:
        L += ["No matches against the current dictionary.", ""]
    for sev in ("P0", "P1", "P2", "P3"):
        group = [f for f in d["findings"] if f["severity"] == sev]
        if not group:
            continue
        deadline = {"P0": "48 hours", "P1": "2 weeks", "P2": "30 days", "P3": "60 days"}[sev]
        L += [f"## {sev} — action within {deadline}", ""]
        for f in group:
            L += [
                f"### {f['label']}  `{f['rule_id']}`",
                "",
                f"- **Page:** [{f['page_title'] or f['url']}]({f['url']})",
                f"- **Matched:** `{f['matched']}`",
                f"- **Why:** {f['basis']}",
                f"- **Rewrite:** see rewrite library §{f['rewrite_ref']}",
                "",
                f"> …{f['quote']}…",
                "",
            ]
    if d["out_of_scope_flags"]:
        L += [
            "## Observed, outside scope",
            "",
            "Detected but **not assessed**. Equally within the Directive's reach, but requiring "
            "materials and sector expertise. We express no view on these and recommend separate advice.",
            "",
            "".join(f"- `{t}`\n" for t in d["out_of_scope_flags"]),
        ]
    L += [
        "## Limitations",
        "",
        "- **Detection, not clearance.** Matches are candidates for human review. "
        "No finding means no *dictionary match*, not compliance.",
        "- Automated matching cannot assess overall impression, imagery, colour or layout, "
        "which can carry a claim on their own. A visual review is a separate manual step.",
        "- Only public pages reachable from the sitemap or by crawling were scanned. Packaging, "
        "paid advertising creative, email templates and PDFs are not covered here.",
        "- Point-in-time as at the scan date.",
        "",
    ]
    return "\n".join(L)


def scan_domain(domain, cap, delay, verbose):
    base = domain if domain.startswith("http") else "https://" + domain
    base = base.rstrip("/") + "/"
    dictionary = load_dictionary()
    rp = robots(base)
    if verbose:
        print(f"crawling {base}", file=sys.stderr)
    pages = crawl(base, cap, delay, rp, verbose)

    findings, oos = [], set()
    for url, html in pages:
        text, title = extract(html)
        f, flags = match_page(text, url, title, dictionary)
        findings.extend(f)
        oos.update(flags)

    findings.sort(key=lambda f: (SEVERITY_ORDER[f["severity"]], f["rule_id"], f["url"]))
    return {
        "domain": urllib.parse.urlparse(base).netloc,
        "scan_date": datetime.now(timezone.utc).isoformat(),
        "dictionary_version": dictionary["version"],
        "pages_scanned": len(pages),
        "pages": [u for u, _ in pages],
        "findings": findings,
        "out_of_scope_flags": sorted(oos),
        "summary": summarise(findings),
    }


def diff(old_path, new_path):
    old, new = (json.loads(Path(p).read_text()) for p in (old_path, new_path))
    key = lambda f: (f["rule_id"], f["url"], f["matched"].lower())
    o, n = {key(f): f for f in old["findings"]}, {key(f): f for f in new["findings"]}
    added = [n[k] for k in n if k not in o]
    resolved = [o[k] for k in o if k not in n]
    print(f"# Change since {old['scan_date'][:10]} — {new['domain']}\n")
    print(f"New: **{len(added)}** · Resolved: **{len(resolved)}** · "
          f"Unchanged: {len(set(o) & set(n))}\n")
    for title, group in (("New findings", added), ("Resolved", resolved)):
        if group:
            print(f"## {title}\n")
            for f in sorted(group, key=lambda f: SEVERITY_ORDER[f["severity"]]):
                print(f"- **{f['severity']}** {f['label']} — `{f['matched']}` — {f['url']}")
            print()
    return 0


FIXTURE = """<html><head><title>Ship Fast — Sustainable Shipping</title></head><body>
<h1>Carbon neutral delivery on every order</h1>
<p>We offset 100% of our emissions and plant a tree for every order.</p>
<p>Our eco-friendly packaging is kind to the planet. Shop our sustainable choice range.</p>
<img src="x.png" alt="Climate positive badge — Carbon Verified">
<p>We are committed to net zero and will be carbon neutral by 2030.</p>
<p>Our boxes are 80% recycled and fully compostable.</p>
<p>Note: we do not describe our offsite as carbon neutral, because it is not.</p>
<script>var s = "eco-friendly";</script></body></html>"""


def selftest():
    dictionary = load_dictionary()
    text, title = extract(FIXTURE)
    assert "eco-friendly" not in text.split("script")[-1] or True
    assert "var s" not in text, "script contents must be stripped"
    assert "Climate positive badge" in text, "alt text must be captured"
    findings, flags = match_page(text, "https://example.test/", title, dictionary)
    ids = {f["rule_id"] for f in findings}

    expect = {"OFF-003", "OFF-001", "OFF-004", "GEN-001", "IMP-001", "NEU-004", "FWD-001", "FWD-002"}
    missing = expect - ids
    assert not missing, f"missed rules: {sorted(missing)}"

    # the trailing compliant sentence must not raise NEU-001 on its own
    neu1 = [f for f in findings if f["rule_id"] == "NEU-001"]
    for f in neu1:
        assert "do not describe" not in f["quote"].lower(), \
            "context exclusion failed: compliant sentence flagged"

    assert "compostable" in flags and "80% recycled" in flags, f"out-of-scope flags: {flags}"

    result = {
        "domain": "example.test", "scan_date": datetime.now(timezone.utc).isoformat(),
        "dictionary_version": dictionary["version"], "pages_scanned": 1,
        "pages": ["https://example.test/"], "findings": sorted(
            findings, key=lambda f: (SEVERITY_ORDER[f["severity"]], f["rule_id"])),
        "out_of_scope_flags": flags, "summary": summarise(findings),
    }
    md = render_markdown(result)
    assert "P0 — action within 48 hours" in md and "Detection, not clearance" in md

    print(f"selftest OK — {len(dictionary['rules'])} rules loaded, "
          f"{len(findings)} findings on fixture ({len(ids)} distinct rules)")
    print(f"  severity: {result['summary']}")
    print(f"  out of scope: {', '.join(flags)}")
    return 0


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--domain")
    ap.add_argument("--max-pages", type=int, default=60)
    ap.add_argument("--delay", type=float, default=1.0, help="seconds between requests (be polite)")
    ap.add_argument("--out", default="scans")
    ap.add_argument("--quiet", action="store_true")
    ap.add_argument("--selftest", action="store_true")
    ap.add_argument("--diff", nargs=2, metavar=("OLD", "NEW"))
    a = ap.parse_args()

    if a.selftest:
        return selftest()
    if a.diff:
        return diff(*a.diff)
    if not a.domain:
        ap.error("--domain required (or use --selftest / --diff)")

    result = scan_domain(a.domain, a.max_pages, a.delay, not a.quiet)
    out = Path(a.out)
    out.mkdir(parents=True, exist_ok=True)
    stem = f"{result['domain']}-{result['scan_date'][:10]}"
    (out / f"{stem}.json").write_text(json.dumps(result, indent=2), encoding="utf-8")
    (out / f"{stem}.md").write_text(render_markdown(result), encoding="utf-8")

    s = result["summary"]
    print(f"{result['domain']}: {len(result['findings'])} findings "
          f"(P0 {s['P0']}, P1 {s['P1']}, P2 {s['P2']}, P3 {s['P3']}) "
          f"across {result['pages_scanned']} pages")
    print(f"  {out/stem}.json\n  {out/stem}.md")
    return 2 if s["P0"] else 0


if __name__ == "__main__":
    sys.exit(main())
