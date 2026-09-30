# Environmental Claims Scan — shipfast.example

Scan date **2026-09-30** · Pages scanned **1** · Dictionary **2026.10.1**

**12 findings** — P0: **4** · P1: 6 · P2: 2 · P3: 0

> Detection only. This scan flags wording for review against the ECGT Directive (EU) 2024/825. It is not legal advice, not a compliance assessment, and an absence of findings is not a clean bill of health — see the limitations below.

## P0 — action within 48 hours

### Carbon neutrality claim  `NEU-001`

- **Page:** [Ship Fast — Sustainable Shipping](https://shipfast.example/)
- **Matched:** `Carbon neutral`
- **Why:** ECGT Annex I: neutral/reduced/positive impact based on offsetting, blacklisted per se regardless of credit quality.
- **Rewrite:** see rewrite library §1.1

> …Ship Fast — Sustainable Shipping Carbon neutral delivery on every order We offset 100% of our emissions and plant a tree for every order.…

### Climate positive / carbon negative claim  `NEU-004`

- **Page:** [Ship Fast — Sustainable Shipping](https://shipfast.example/)
- **Matched:** `Climate positive`
- **Why:** Neutrality prohibition plus an effectively unevidenceable net-positive assertion.
- **Rewrite:** see rewrite library §1.3

> …der. Our eco-friendly packaging is kind to the planet. Shop our sustainable choice range. Climate positive badge — Carbon Verified We are committed to net zero and will be carbon neutral by 2030.…

### Offsetting claim  `OFF-001`

- **Page:** [Ship Fast — Sustainable Shipping](https://shipfast.example/)
- **Matched:** `We offset`
- **Why:** Offsetting framing in support of an impact claim. Offering an offset purchase is not prohibited; describing the result as neutral or reduced is.
- **Rewrite:** see rewrite library §2.1

> …Ship Fast — Sustainable Shipping Carbon neutral delivery on every order We offset 100% of our emissions and plant a tree for every order. Our eco-friendly packaging is kin…

### Carbon neutral shipping or delivery  `OFF-003`

- **Page:** [Ship Fast — Sustainable Shipping](https://shipfast.example/)
- **Matched:** `Carbon neutral delivery`
- **Why:** Service-level neutrality by offsetting. The most common live violation in EU ecommerce.
- **Rewrite:** see rewrite library §2.3

> …Ship Fast — Sustainable Shipping Carbon neutral delivery on every order We offset 100% of our emissions and plant a tree for every order. Our eco-…

## P1 — action within 2 weeks

### Generic environmental claim: eco-friendly  `GEN-001`

- **Page:** [Ship Fast — Sustainable Shipping](https://shipfast.example/)
- **Matched:** `eco-friendly`
- **Why:** ECGT: generic environmental claim without demonstrated recognised excellence.
- **Rewrite:** see rewrite library §3.1

> …very on every order We offset 100% of our emissions and plant a tree for every order. Our eco-friendly packaging is kind to the planet. Shop our sustainable choice range. Climate positive badg…

### Generic environmental claim: eco-friendly  `GEN-001`

- **Page:** [Ship Fast — Sustainable Shipping](https://shipfast.example/)
- **Matched:** `kind to the planet`
- **Why:** ECGT: generic environmental claim without demonstrated recognised excellence.
- **Rewrite:** see rewrite library §3.1

> …set 100% of our emissions and plant a tree for every order. Our eco-friendly packaging is kind to the planet. Shop our sustainable choice range. Climate positive badge — Carbon Verified We are commi…

### Generic environmental claim: sustainable as merit  `GEN-002`

- **Page:** [Ship Fast — Sustainable Shipping](https://shipfast.example/)
- **Matched:** `our sustainable choice`
- **Why:** Generic claim when used as a claim of merit. Descriptive uses ('sustainability report', 'sustainability team') are not caught.
- **Rewrite:** see rewrite library §3.2

> …and plant a tree for every order. Our eco-friendly packaging is kind to the planet. Shop our sustainable choice range. Climate positive badge — Carbon Verified We are committed to net zero and will be…

### Undefined eco filter or product badge  `IMP-001`

- **Page:** [Ship Fast — Sustainable Shipping](https://shipfast.example/)
- **Matched:** `sustainable choice`
- **Why:** A generic environmental claim expressed through UI with no defined criteria.
- **Rewrite:** see rewrite library §6.1

> …plant a tree for every order. Our eco-friendly packaging is kind to the planet. Shop our sustainable choice range. Climate positive badge — Carbon Verified We are committed to net zero and will be…

### Possible self-created sustainability label  `LBL-001`

- **Page:** [Ship Fast — Sustainable Shipping](https://shipfast.example/)
- **Matched:** `Carbon Verified`
- **Why:** ECGT: displaying a sustainability label not based on a certification scheme or established by a public authority. Verify the scheme exists and the client is entitled to display it.
- **Rewrite:** see rewrite library §4.1

> …kaging is kind to the planet. Shop our sustainable choice range. Climate positive badge — Carbon Verified We are committed to net zero and will be carbon neutral by 2030. Our boxes are 80% recycl…

### Tree planting as impact claim  `OFF-004`

- **Page:** [Ship Fast — Sustainable Shipping](https://shipfast.example/)
- **Matched:** `plant a tree for every`
- **Why:** Implies offsetting and a permanence not evidenced. Trees planted is an input, not an outcome.
- **Rewrite:** see rewrite library §2.4

> …nable Shipping Carbon neutral delivery on every order We offset 100% of our emissions and plant a tree for every order. Our eco-friendly packaging is kind to the planet. Shop our sustainable choice rang…

## P2 — action within 30 days

### Forward-looking target, substantiation required  `FWD-001`

- **Page:** [Ship Fast — Sustainable Shipping](https://shipfast.example/)
- **Matched:** `carbon neutral by 2030`
- **Why:** ECGT: unsubstantiated claims about future environmental performance. Check all five tests: base year and boundary, published milestone plan, allocated resource, annual progress reporting, third-party verification where feasible.
- **Rewrite:** see rewrite library §5.1

> …range. Climate positive badge — Carbon Verified We are committed to net zero and will be carbon neutral by 2030. Our boxes are 80% recycled and fully compostable. Note: we do not describe our offsite a…

### Vague commitment language  `FWD-002`

- **Page:** [Ship Fast — Sustainable Shipping](https://shipfast.example/)
- **Matched:** `committed to net zero`
- **Why:** Unsubstantiated future performance. Vaguer wording provides no additional protection.
- **Rewrite:** see rewrite library §5.2

> …lanet. Shop our sustainable choice range. Climate positive badge — Carbon Verified We are committed to net zero and will be carbon neutral by 2030. Our boxes are 80% recycled and fully compostable. Not…

## Observed, outside scope

Detected but **not assessed**. Equally within the Directive's reach, but requiring materials and sector expertise. We express no view on these and recommend separate advice.

- `80% recycled`
- `compostable`

## Limitations

- **Detection, not clearance.** Matches are candidates for human review. No finding means no *dictionary match*, not compliance.
- Automated matching cannot assess overall impression, imagery, colour or layout, which can carry a claim on their own. A visual review is a separate manual step.
- Only public pages reachable from the sitemap or by crawling were scanned. Packaging, paid advertising creative, email templates and PDFs are not covered here.
- Point-in-time as at the scan date.
