# Statement of Work — Template

**CarbonMeter · [[SUPPLIER_LEGAL_NAME]], Lda.**

> **Status: draft template for legal review alongside the MSA.** Not legal advice. The master form below is common to all engagements; **Annexes 1–4** are the product-specific scope schedules. Use the master form plus exactly one annex per engagement.
>
> **The out-of-scope lists are the commercially important part of this document.** A fixed-fee consultancy loses margin through scope drift, not through underpricing. Do not delete lines from them to make a SOW look more generous.

---

# Master form

**STATEMENT OF WORK No. [[SOW_NO]]**

Under the Master Services Agreement dated **[[MSA_DATE]]** between **[[SUPPLIER_LEGAL_NAME]], Lda.** ("Supplier") and **[[CLIENT_LEGAL_NAME]]** ("Client").

| | |
|---|---|
| **SOW number** | [[SOW_NO]] |
| **Engagement** | [[PRODUCT_NAME]] — see Annex [[ANNEX_NO]] |
| **Start date** | [[START_DATE]] |
| **Target delivery** | [[DELIVERY_DATE]] |
| **Reporting period** | [[REPORTING_PERIOD]] |
| **Fee** | €[[FEE]] excl. IVA |

## 1. Scope

The Services are as set out in **Annex [[ANNEX_NO]]** to this SOW. The in-scope and out-of-scope statements in that Annex are definitive. Anything not stated as in scope is out of scope and requires a change order under clause 6.3 of the MSA.

## 2. Boundary and basis of preparation

| Parameter | Value |
|---|---|
| Reporting period | [[REPORTING_PERIOD]] |
| Entities in scope | [[ENTITIES]] |
| Consolidation approach | [[CONSOLIDATION]] *(recommended: operational control)* |
| Emission Factor Set | [[FACTOR_SET]] |
| GWP basis | GWP100, IPCC AR6 |
| Base year | [[BASE_YEAR]] |
| Recalculation threshold | [[RECALC_PCT]]% of Category 6 |
| De minimis | Up to [[DEMINIMIS_PCT]]% of Category 6 may be estimated, disclosed as such |
| Radiative forcing treatment | Reported separately from the GWP100 figure; never blended |
| Data lane | [[DATA_LANE]] *(A: TMC export · B: expense export · C: attendee roster)* |

## 3. Deliverables

| # | Deliverable | Format | Due |
|---|---|---|---|
| [[D1_NO]] | [[D1_NAME]] | [[D1_FORMAT]] | [[D1_DUE]] |
| [[D2_NO]] | [[D2_NAME]] | [[D2_FORMAT]] | [[D2_DUE]] |
| [[D3_NO]] | [[D3_NAME]] | [[D3_FORMAT]] | [[D3_DUE]] |

## 4. Client obligations and dates

| Obligation | Owner | Due |
|---|---|---|
| Nominate Data Owner | [[CLIENT_SIGNATORY]] | On execution |
| Provide [[DATA_DESCRIPTION]], pseudonymised per Schedule 3 | [[DATA_OWNER]] | [[DATA_DUE]] |
| Provide GL travel account total for coverage reconciliation | [[FINANCE_CONTACT]] | [[DATA_DUE]] |
| Attend kickoff (60 min) | [[ATTENDEES]] | [[KICKOFF_DATE]] |
| Respond to written queries | [[DATA_OWNER]] | Within 5 business days |
| Nominate Deliverable approver | [[CLIENT_SIGNATORY]] | On execution |
| Attend readout (60 min) | [[ATTENDEES]] | [[READOUT_DATE]] |

**Data Owner:** [[DATA_OWNER_NAME]], [[DATA_OWNER_EMAIL]]

Client acknowledges that the target delivery date assumes data is provided by [[DATA_DUE]], and that clause 4.4 of the MSA applies to delay.

## 5. Fees and payment

| Milestone | Amount | Invoiced |
|---|---|---|
| On execution of this SOW | €[[FEE_DEPOSIT]] | [[START_DATE]] |
| On delivery | €[[FEE_BALANCE]] | [[DELIVERY_DATE]] |
| **Total** | **€[[FEE]]** | excl. IVA |

[[IVA_TREATMENT_NOTE]]

## 6. Assumptions

This SOW and its fee are based on the following. Where an assumption proves incorrect, Supplier will notify Client and the Parties will agree a change order.

1. Approximately **[[TRAVELLER_COUNT]]** travellers and **[[JOURNEY_COUNT]]** journeys in the reporting period.
2. Data is available in a machine-readable export (CSV or XLSX). Manual transcription from PDF receipts or images is out of scope.
3. A single reporting entity and a single reporting period, as stated in clause 2.
4. Client holds the employee reference mapping and provides pseudonymised data per MSA clause 4.3.
5. One consolidated set of review comments on each Deliverable, returned within the acceptance period.
6. [[ADDITIONAL_ASSUMPTIONS]]

## 7. Acceptance

Acceptance is governed by MSA clause 6. A Deliverable is accepted where it conforms to this SOW and the Methodology Statement. **Acceptance is not conditional on** a third party accepting a Reported Figure, on Client achieving any score, rating or certification, or on any regulatory or contractual outcome.

## 8. Signature

**For [[SUPPLIER_LEGAL_NAME]], Lda.** Name: .................... Date: ..........

**For [[CLIENT_LEGAL_NAME]]** Name: .................... Date: ..........

---
---

# Annex 1 — Tier 0: Offsite Impact Snapshot

**Fee: €2,200 · Delivery: 5 working days from receipt of complete data · Data lane: C**

## In scope

1. One event, up to **80 travellers**.
2. Distribution of an attendee data-collection form and one reminder; collation of responses.
3. Calculation of event emissions: air travel (distance-based, great-circle plus 9% routing uplift, by haul band and cabin), hotel room-nights, and ground transfers.
4. GWP100 figure and separately-stated radiative-forcing-inclusive figure.
5. Identification of emissions concentration by cohort and by travel mode.
6. **Deliverables:** (a) Snapshot report, 4–6 pages, PDF; (b) short methodology note; (c) 30-minute readout.

## Out of scope

- Any travel other than travel to and from the named event
- Annual or full-financial-year business travel
- Venue, catering, accommodation-operations or event-production emissions (Category 1)
- Expense-system or TMC data ingestion and reconciliation
- Coverage reconciliation against the general ledger
- VSME or ESRS mapping, disclosure tables, or assurance-ready evidence binder
- Base year establishment or recalculation policy
- Destination impact partner identification or diligence
- Claim Language Pack
- Reduction scenario modelling beyond the observations in the report
- Responses to customer or investor questionnaires

## Notes

- Attendee response rates below **[[MIN_RESPONSE_PCT]]%** materially affect accuracy; Supplier will state the response rate and gross up on a disclosed basis.
- **Credit:** the full fee is creditable against a Tier 1 Annual Category 6 Audit commissioned within **90 days** of delivery.

---

# Annex 2 — Tier 1: Annual Category 6 Audit

**Fee: €7,500 · Delivery: 3 weeks from receipt of complete data · Data lane: A or B**

## In scope

1. **Kickoff** (60 min) and boundary setting: reporting period, entity scope, consolidation approach, base year, recalculation threshold, de minimis rule, data lane. Minuted; minutes form an appendix to the report.
2. **Ingestion** of one financial year of business travel data via the agreed lane, including classification of expense rows into air / rail / hotel / ground / other where lane B applies.
3. **Calculation** of Scope 3 Category 6 for the full reporting period: air, rail, hotel room-nights, ground transport and other business travel. Distance-based method where itinerary is recoverable; spend-based where it is not, with the split disclosed.
4. **Validation:** deduplication, outlier review, coverage reconciliation against the general ledger travel account, and an independent recalculation of a 10% random sample by a second Supplier reviewer.
5. **Disclosure preparation:** VSME mapping and an ESRS E1-6 crosswalk table; tank-to-wheel and well-to-tank split; GWP100 and radiative-forcing figures stated separately; primary versus estimated data share.
6. **Deliverables:**
   - **A.** Disclosure Table (VSME-mapped, ESRS E1-6 crosswalked) — XLSX + PDF
   - **B.** Methodology & Uncertainty Statement, 2–3 pages — PDF
   - **C.** Evidence Binder: source exports, factor extracts, calculation workbook, audit log, kickoff minutes, reviewer sign-off — indexed folder
   - **D.** Reduction Levers Memo: modelled scenarios with stated assumptions — PDF
   - **F.** Claim Language Pack, populated for Client — PDF
   - **G.** Read-only dashboard — hosted link
   - Readout (60 min) plus a 20-minute board-pack version
7. One round of consolidated review comments on each Deliverable.

## Out of scope

- Scope 1 and Scope 2 emissions
- Scope 3 categories other than Category 6 (notably Category 1 purchased goods and services, Category 2 capital goods, Category 7 employee commuting and home working)
- Assurance, verification, certification, or any form of audit opinion — see MSA clause 12
- Preparation or filing of any statutory report
- Completion of third-party platform questionnaires (EcoVadis, CDP, customer portals) — available under Tier 2
- Science-based target setting, validation or submission
- Destination impact partner identification or diligence — see Annex 4
- SAF or in-sector intervention advisory — separate module
- Prior-year restatement beyond establishment of the stated base year
- Legal advice on any claim — see MSA clause 12.4
- Travel policy drafting — available under Tier 2
- More than one reporting entity or period
- Reliance letters or duties of care to third parties — see MSA clause 14.4

## Notes

- Where lane B applies and more than **[[SPEND_BASED_THRESHOLD]]%** of travel spend proves unrecoverable to itinerary level, Supplier will notify Client before proceeding; additional reconstruction is a change order.
- Coverage ratio is reported as delivered, not guaranteed. A low coverage ratio is a finding, not a defect.

---

# Annex 3 — Tier 2: Travel Impact Operating System (retainer)

**Fee: €1,600/month · Term: 12 months, quarterly break · Invoiced monthly in advance**

## In scope, per quarter unless stated

1. **Quarterly data refresh** and updated Category 6 figures, dashboard maintained current.
2. **Offsite pre-mortem:** forecast modelling of up to **three candidate destinations** per event, before venue commitment, including population-weighted travel centroid analysis, direct-route availability and rail substitutability. Up to **[[PREMORTEM_COUNT]]** per year.
3. **Travel policy advisory:** drafting or review of cabin-class, rail-threshold, routing and booking-lead-time rules.
4. **Questionnaire response service:** preparation of Category 6 responses to customer, investor and platform questionnaires, up to **[[QUESTIONNAIRE_COUNT]]** per quarter.
5. **Claim review** under MSA clause 16.3, up to **[[CLAIM_REVIEW_COUNT]]** items per quarter.
6. **Claim Language Pack maintenance:** version updates on regulatory change, with notification.
7. **Quarterly board pack:** two pages, presentation-ready.
8. Reasonable email and call support, up to **[[SUPPORT_HOURS]]** hours per month.

## Out of scope

- The annual Category 6 Audit itself (Tier 1), which remains separately commissioned
- Scope 1, Scope 2 and other Scope 3 categories
- Assurance, verification or certification
- Completion of questionnaires beyond the stated quarterly allowance
- Destination impact programme design and partner diligence (Annex 4)
- Science-based target setting or submission
- Legal advice, or representation before any authority
- Attendance at Client events, or on-site presence
- Emissions accounting for new entities acquired mid-term, absent a change order

## Notes

- Unused allowances do not carry forward.
- **The pre-mortem is the operative benefit of this tier.** Client should notify Supplier at destination-shortlist stage, not after venue commitment; Supplier cannot model a decision already taken.

---

# Annex 4 — Module A: Destination Impact Programme

**Fee: €4,000 design + €500/month stewardship · Delivery: 4 weeks**

## In scope

1. **Partner identification** in **one** destination from Supplier's existing roster ([[ROSTER_CITIES]]).
2. **Written diligence** on 2–3 candidate partners against the full criteria set: legal standing, additionality, permanence, auditability, no double counting, co-benefits, safeguards, CRCF trajectory and absorptive capacity. Documented, including rejections.
3. **Programme design:** contribution structure, output metrics, reporting cadence, and the direct contracting route between Client and Partner.
4. **Claim framing** for the programme, consistent with the Claim Language Pack, including the severance wording and the standing non-offset statement.
5. **Deliverable E:** Destination Impact Dossier — partner diligence sheets, recommended structure, claim wording — PDF.
6. **Stewardship (monthly):** collation of partner progress reporting, outputs summary, and annual narrative suitable for Client's internal and external reporting.

## Out of scope

- **Receipt, holding or transmission of any Contribution.** Client contracts and pays each Partner directly — MSA clause 11.2
- Any carbon credit, unit, offset or registry transaction
- Any representation that a Contribution reduces, neutralises or offsets any Reported Figure
- Legal review of Client's agreement with a Partner
- Diligence in a destination outside Supplier's existing roster — quoted separately at cost
- Guarantee of Partner performance, outcome permanence, or continued standing — MSA clause 11.5
- On-site monitoring, verification or site visits
- Tax advice on the deductibility or treatment of any Contribution
- Grant application or co-funding support on the Partner's behalf

## Notes

- Supplier receives **no commission or benefit** from any Partner — MSA clause 11.4.
- **Contributions are never expressed in tonnes of CO₂e.** Outputs are stated in euros, hectares, linear metres, species recorded or positions supported.
- A new destination requires a diligence sprint of approximately 4 weeks, quoted separately. Supplier will not recommend an undiligenced partner to meet a Client deadline.

---
---

# Annex 5 — Internal use: SOW assembly checklist

> **Not part of the client document. Delete before sending.**

1. Master form completed, correct product annex attached, **only one** annex included.
2. Fee, deposit and balance arithmetic checked against the rate card.
3. IVA treatment selected: Portuguese client (23%) / EU B2B reverse charge with VIES number recorded / non-EU out of scope.
4. **VIES number validated and the validation screenshot saved** to the engagement folder.
5. Data Owner **named with email** — not a job title, not a shared inbox. A SOW without a named Data Owner is the single most reliable predictor of an overrunning engagement.
6. Data due date set with enough slack that MSA clause 4.4 is credible rather than theatrical.
7. Assumptions in clause 6 reflect the actual traveller and journey counts from the Exposure Estimate, not the defaults.
8. Reporting period, entity scope and consolidation approach match what was agreed on the discovery call.
9. Factor set stated as the current published version.
10. Tier 0: the 90-day credit note is present. Tier 2: allowances quantified, no open-ended commitments.
11. Delivery date is achievable against current committed workload — check the delivery calendar before sending, not after signature.
12. Annex 5 deleted. MSA Annex A deleted.
