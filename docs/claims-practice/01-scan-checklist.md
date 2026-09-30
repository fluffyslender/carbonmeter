# Claims Scan — Delivery Checklist

**Internal procedure. Not a client document.**

Target: **75–100 minutes** for a standard engagement. If a scan runs past two hours, the client is out of profile — either too large (escalate to a tiered quote) or the findings are outside carbon/climate scope (see §7).

| Step | Time | Output |
|---|---|---|
| 1. Property inventory | 10 min | Property list |
| 2. Phrase sweep | 25 min | Raw hit list |
| 3. Visual & implied check | 10 min | Additional findings |
| 4. Label & badge check | 5 min | Additional findings |
| 5. Forward-looking check | 5 min | Additional findings |
| 6. Evidence capture | 15 min | Screenshots + archive links |
| 7. Triage & scope call | 10 min | Severity-ranked findings |
| 8. Report assembly | 20 min | Client deliverable |

---

## 1. Property inventory

Record every property before searching any of them. Missing a property is the only way this engagement fails.

- [ ] Primary domain + all subdomains (`blog.`, `help.`, `shop.`, `careers.`, `investors.`)
- [ ] Careers / jobs pages — **highest hit rate in practice**, lowest internal ownership
- [ ] Blog archive, including posts 3+ years old
- [ ] Product / pricing / shipping / checkout pages
- [ ] PDFs: impact reports, brochures, whitepapers, media kits, investor decks
- [ ] Email footers and transactional email templates (ask the client for samples)
- [ ] Social bios and pinned posts: LinkedIn, Instagram, X, TikTok, YouTube channel description
- [ ] App store listings (iOS / Google Play descriptions)
- [ ] Event and conference pages, sponsor listings
- [ ] Packaging and physical collateral (ask; often the worst offender and out of their own memory)
- [ ] Third-party: press release wires, partner sites, directory listings, podcast descriptions
- [ ] Paid advertising — ask directly. **Live ads are always P0**

**Ask the client two questions at intake.** They save 20 minutes each: *"Which pages do you think are riskiest?"* and *"Are any environmental claims running in paid ads right now?"*

## 2. Phrase sweep

Run each as a site-restricted search on the client's domain, then repeat on the careers subdomain. Record every hit with its URL.

```
site:CLIENT.com "carbon neutral" OR "climate neutral" OR "CO2 neutral" OR "carbon-neutral"
site:CLIENT.com "net zero" OR "net-zero" OR "carbon negative" OR "climate positive"
site:CLIENT.com "offset" OR "offsetting" OR "compensated" OR "neutralise" OR "neutralize"
site:CLIENT.com "eco-friendly" OR "eco friendly" OR "environmentally friendly" OR "planet friendly"
site:CLIENT.com "sustainable" OR "sustainability" OR "green" OR "regenerative"
site:CLIENT.com "climate friendly" OR "climate conscious" OR "carbon footprint"
site:CLIENT.com "plant a tree" OR "trees planted" OR "reforestation"
site:CLIENT.com "plastic neutral" OR "water neutral" OR "zero impact" OR "low impact"
site:CLIENT.com filetype:pdf "carbon" OR "climate" OR "sustainab"
```

Also sweep, manually:
- **On-site search box** for `carbon`, `climate`, `sustainab`, `green`, `offset`
- **Sitemap** (`/sitemap.xml`) for any page whose slug contains `sustain`, `impact`, `climate`, `esg`, `planet`, `green`, `responsib`
- **Non-English properties** — a `.de`, `.fr`, `.es` or `.pt` site carries its own claims and its own transposed national law. `klimaneutral`, `neutre en carbone`, `neutro en carbono`, `neutro em carbono`. Where the client sells in a Member State that has transposed, **that** market sets the constraint

Site-restricted search misses unindexed and recently-changed pages. Where the client has more than ~50 pages, ask for a page list or crawl their sitemap manually. **Do not build or run an automated scraper** — unnecessary at this volume and an avoidable terms-of-service argument.

## 3. Visual and implied claims

Claims are assessed on overall impression, by any means including imagery. Check for:

- [ ] Leaf, tree, globe, earth motifs adjacent to product or service claims
- [ ] Green colour coding used to signal an environmental benefit (filters, badges, tiers)
- [ ] "Eco" / "sustainable choice" product filters or labels in a shop
- [ ] Nature photography paired with claim-adjacent headings
- [ ] Iconography implying certification without a named scheme

An ecommerce "eco" filter with no defined criteria is a generic environmental claim expressed as UI. Frequently missed because it lives in the product catalogue rather than in copy.

## 4. Labels and badges

- [ ] Self-designed seals, badges or marks implying environmental performance
- [ ] Badges supplied by a vendor (offset providers routinely supply these)
- [ ] Third-party scheme logos — **verify the client is actually entitled to display each one** and that the scheme is a certification scheme or public-authority label
- [ ] "Verified" / "Certified" wording without a named certifying body

## 5. Forward-looking claims

For each target or pledge found, check all five tests: stated base year and boundary; published implementation plan with dated milestones; allocated resource; public progress reporting; third-party verification where feasible.

A bare "net zero by 2030" with no plan behind it is a finding. Most will fail at least three of the five.

## 6. Evidence capture

For each finding, capture **before recommending any change** — a client may fix a page mid-engagement and then dispute that it said what it said.

- [ ] Full-page screenshot, dated
- [ ] Exact URL
- [ ] Exact verbatim wording, copied not paraphrased
- [ ] Wayback Machine / archive.today snapshot URL where one exists
- [ ] Best evidence of first-published date (post date, git history, archive snapshots)

**First-published date matters legally.** Duration of an infringement is an explicit penalty criterion, so the age of a claim shapes both the client's exposure and the urgency of the fix. Two minutes in the Wayback Machine per P0 finding is worth it.

## 7. Triage and scope

| Severity | Definition | Fix deadline |
|---|---|---|
| **P0** | Live neutrality or offsetting claim on a consumer-reachable page; any live paid ad; any claim on packaging in current production | 48 hours |
| **P1** | Generic environmental claim; self-made badge; unverified third-party label | 2 weeks |
| **P2** | Unsubstantiated forward-looking claim or target | 30 days |
| **P3** | Archived posts, superseded PDFs, third-party-controlled copy | 60 days |

### Scope boundary — say this plainly in the report

**In scope:** carbon, climate, emissions, offsetting, neutrality and energy claims. This is where the expertise is.

**Out of scope, flag and refer:** material composition claims (recycled content percentages, "biodegradable", "compostable", "plastic-free"), organic and food claims, animal welfare, social and labour claims, chemical and packaging regulation. These are equally caught by ECGT but need materials and sector expertise. Note them as observed, state they are outside scope, and recommend counsel.

Refusing adjacent work builds more trust than absorbing it. It also keeps the engagement inside three hours.

## 8. Quality gate before sending

- [ ] Every finding has verbatim wording, URL, screenshot and severity
- [ ] Every finding has at least one concrete rewrite, not a general instruction
- [ ] No finding overstates the legal position — see the discipline rules in `04-outbound-sequence.md` §6
- [ ] The B2C / B2B perimeter is stated accurately, not glossed
- [ ] The non-transposition position is stated for the client's own jurisdiction
- [ ] Out-of-scope observations are listed and disclaimed
- [ ] "Not legal advice" appears in the summary, not only in the footer
- [ ] Scan date recorded — the report is a point-in-time assessment and says so
