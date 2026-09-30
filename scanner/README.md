# Claims Scanner — PARKED

**Status: working prototype, shelved 2026-09-30.** Direction changed: a claims-compliance
product requires ongoing legal review and carries advice-adjacent liability, which is not
wanted. Kept because it works and cost little.

## What this is

Zero-dependency Python crawler that flags environmental claims prohibited under the ECGT
Directive (EU) 2024/825. Detection only — it never asserts compliance.

```
./scan.py --selftest                      # 19 rules, fixture assertions
./scan.py --domain example.com            # writes scans/<domain>-<date>.{json,md}
./scan.py --diff old.json new.json        # change since last scan (monitoring mode)
```

- `dictionary.json` — 19 rules: pattern, severity, legal basis, rewrite reference, and
  `exclude_context` phrases that suppress matches where surrounding text shows compliant
  usage. This is the asset; the crawler is commodity.
- `scan.py` — sitemap-first crawl with breadth-first fallback, robots.txt respected,
  rate limited, page-capped. Strips script/style, captures `alt`/`aria-label`.
- `sample-report.md` — output on the built-in fixture.

## If ever revived

The crawler is generic. Swapping `dictionary.json` retargets it at any text-pattern
problem with no code change — that is the reusable part.

Known limits: regex matching cannot assess overall impression, imagery or layout; false
positives need the `exclude_context` lists maintained; network fetch was not verified
end-to-end against a live domain (sandbox proxy blocked it), so test `fetch()` before use.
