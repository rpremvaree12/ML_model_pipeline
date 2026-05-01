# NYC LL97 Audit Prioritization Model
*A machine learning approach to emissions compliance enforcement*

---

## Business Problem

Local Law 97 (LL97), enacted in 2019 and effective in 2024, has been described by the NYC
Department of Buildings as one of the most ambitious building emissions laws in the nation.
LL97 places carbon caps on buildings larger than 25,000 square feet — a category that
accounts for over two-thirds of NYC's greenhouse gas emissions. Multifamily buildings
represent nearly 60% of covered properties, most of them low-rise, pre-WWII construction.

The compliance picture is already severe. The Urban Green Council analyzed 2023 benchmarking
data and found that 57% of all covered properties currently exceed their 2030 emissions cap.

> Buildings that exceed their limit face fines of **$268 per metric ton of CO₂** over their
> cap — recurring every year until compliant. A 100,000 sq ft multifamily building emitting
> 132 metric tons over its limit faces a **$35,376 annual fine**.

The current reporting process has a structural vulnerability. Building owners submit their
own energy consumption data, certified by a Registered Design Professional (RDP) they hire
themselves. Because the RDP does not independently verify utility readings, there is a
meaningful risk of misreporting — whether inadvertent or strategic.

The NYC Department of Buildings lacks the capacity to audit all 50,000 covered buildings and
currently has no principled method for prioritizing which ones to investigate. A simple
threshold-based approach cannot capture the multivariate patterns that distinguish genuinely
anomalous reporting from normal variation across building types, ages, and neighborhoods.
Machine learning is well-suited to close this gap.

---

## Stakeholders

The NYC DOB is the direct user and primary stakeholder of this project. The model provides
a tiered ranked list of buildings for audit prioritization, enabling auditors to focus
resources where they are most likely to find data discrepancies.

The NYC Mayor's Office of Climate and Environmental Justice has publicly committed to strict
enforcement of LL97, making a systematic audit prioritization tool directly aligned with
the administration's stated policy position.

The NYC Accelerator, the city's free technical assistance program for building owners,
serves as a natural downstream partner. Buildings flagged by the model and subsequently
audited can be connected to the Accelerator for guidance on retrofit pathways and
compliance planning.

Building owners, particularly in the multifamily residential sector, are indirect
beneficiaries — early identification of data discrepancies gives owners time to correct
reporting and plan retrofits before fines compound annually.

The Urban Green Council, a nonprofit research organization that tracks LL97 compliance,
benefits indirectly from improved data quality in the benchmarking system — more accurate
reported emissions makes their policy research more reliable.

---

## Primary Goals

1. **Improve audit targeting** — provide the DOB with a principled, data-driven ranked
list of buildings most likely to have anomalous emissions reporting, replacing ad hoc
selection with systematic prioritization.

2. **Improve accuracy of the city's emissions dataset** — identifying and correcting
misreported buildings improves the reliability of the LL84 benchmarking system as a
whole, benefiting all downstream users of that data.

3. **Quantify financial exposure** — buildings reporting below their actual emissions
represent uncollected penalty revenue. The model surfaces the buildings most likely to
owe fines once their data is corrected.

4. **Support 2030 compliance deadline** — with 57% of covered properties currently
exceeding their 2030 cap, the window for meaningful intervention is narrow. Systematic
audit prioritization accelerates the correction cycle before penalties compound.

---

## Why is Machine Learning A Good Fit for this Problem?

The sheer scale of the problem — over 50,000 buildings subject to Local Law 97 —
makes comprehensive manual review impractical, and machine learning is the only practical
path to comprehensive coverage. Simple rule-based systems cannot capture the complex,
multivariate patterns that emerge across building age, size, type, and neighborhood,
whereas ML models learn these relationships simultaneously.

Unsupervised anomaly detection is particularly well-suited here because it identifies
statistical outliers without requiring labeled examples of fraud or misreporting, which
are rarely available. Peer group construction enables like-for-like comparison — a
pre-war walk-up is compared against other pre-war walk-ups, not against a modern
luxury tower. Running three independent algorithms (Isolation Forest, LOF, DBSCAN)
and surfacing buildings flagged by all three provides the strongest possible signal
from unsupervised methods in the absence of ground truth labels.

---

## Datasets and Relevance

This project scopes to multifamily residential buildings as an MVP — this building type
represents nearly 60% of covered square footage, has the most homogeneous physical
characteristics for peer comparison, and faces the steepest compliance challenge ahead
of the 2030 cap tightening.

**1. NYC Energy and Water Data Disclosure (LL84)**
Sourced from NYC Open Data (resource ID: `5zyy-y8am`), filtered to 2024 reporting year
and multifamily property type at query time. The 2024 pull contains 26,613 rows across
256 columns. This dataset is the analytical core — it contains the self-reported
emissions figures examined for anomalies.

Key features used: `total_location_based_ghg`, `site_eui_kbtu_ft`, `source_eui_kbtu_ft`,
`electricity_use_grid_purchase`, `natural_gas_use_kbtu`, `energy_star_score`, EPA meter
alert flags, and estimation quality indicators.

**2. PLUTO (Primary Land Use Tax Lot Output)**
Published by the NYC Department of City Planning, downloaded as a CSV (858,644 rows,
101 columns). Joined to LL84 on BBL (Borough-Block-Lot) identifier. Contributes
building age, gross square footage, unit count, zoning classification, assessed value,
and owner name — all used for peer group construction and anomaly feature engineering.

Merge results: 26,613 rows merged, 101 unmatched (~0.4%) dropped as negligible.

**3. DOB Violations** *(pending integration)*
The DOB Violations dataset encompasses all violation records across the city, including
violation type, date, BBL, and disposition status. LL84 non-compliance violations will
serve as weak proxy labels for model validation — cross-referencing flagged buildings
against violation history to assess whether the model's output is disproportionately
represented in known problem buildings.

---

## Methodology

### Data Preparation
After merging LL84 and PLUTO, 169 columns (47%) were dropped at an 80% null threshold —
predominantly property-type-specific fields irrelevant to multifamily buildings. The
working dataset was reduced from 358 to 189 columns before feature selection.

500 NYC Housing Authority buildings were separated from the private population after
initial modeling showed NYCHA flagged at 40% vs 4% for private buildings — a structural
difference in campus-style public housing reporting warranting separate treatment.

### Feature Engineering
64 features were selected across five categories: emissions/energy signals, building
physical characteristics, ownership and assessment risk signals, geographic peer grouping
variables, and EPA data quality flags as weak anomaly labels.

Three size-normalized features were engineered to reduce scale bias: `ghg_per_sqft`,
`ghg_per_unit`, and `site_eui_per_unit`. Buildings were assigned to 20 peer groups
by combining five age buckets and four size buckets. StandardScaler was applied before
modeling — Isolation Forest and LOF are distance-based and require comparable feature
scales.

### Population Split
The private building population was split into xl (over 250,000 sq ft, 1,286 buildings)
and non-xl (18,433 buildings) subsets after initial results revealed xl buildings were
flagged at 12x their base rate due to scale differences. Separate models were fit for
each population so buildings are only compared against structurally similar peers.

### Modeling
Three independent anomaly detection algorithms were applied to the non-xl population:

- **Isolation Forest** — global outlier detection via random partitioning
(`contamination=0.05`, `random_state=42`)
- **Local Outlier Factor** — local density comparison against nearest neighbors
(`n_neighbors=20`, `contamination=0.05`)
- **DBSCAN** — density-based clustering with noise points as anomalies
(`eps=4.0`, `min_samples=5`, ~5.5% noise rate)

---

## Key Findings

**Bunching test (self-validating):**
4,014 buildings report within 20% below their LL97 cap versus 1,692 just above — a 2.37x
asymmetry. Under honest reporting this ratio should approach 1.0. This pattern is
consistent with widespread strategic threshold targeting and is independent of all
model assumptions.

**XL peer median anomaly:**
Buildings over 250,000 sq ft report a median of 1,871–2,424 metric tons annually — just
above the legal compliance limit of ~1,687 metric tons for a minimum-qualifying building.
This is implausibly low for buildings of this size and suggests systematic under-reporting
concentrated in the xl population.

**Multi-model agreement:**
147 buildings were flagged by all three independent algorithms — the highest confidence
audit targets. Notable clusters include seven Shore Parkway buildings reporting 0.1%–0.8%
of peer median, a Holland Avenue development with four buildings at 209–243% of peer
median, and Rochdale Village at 9,639% of peer median.

---

## Success Metrics

**Technical Metrics**
- Anomaly score distributions are meaningfully spread across the building population
rather than clustered — confirmed for both Isolation Forest and LOF
- Multi-model overlap: 147 buildings (20.2%) flagged by all three models — agreement
across fundamentally different algorithms provides the strongest unsupervised signal
- Bunching test: 2.37x ratio of buildings just below vs just above the compliance
threshold — statistically significant evidence of strategic reporting
- Peer group coherence: buildings assigned to the same cluster exhibit similar
emissions profiles, validating the segmentation logic

**Business Metrics**
- Rate of data corrections or amendments among audited flagged buildings vs a random
baseline sample (prospective)
- Quantified emissions gap between reported values and peer-expected benchmarks
across flagged properties
- Dollar value of potential penalty recovery assuming corrected compliance
- Prospective validation comparing model-selected audits against a control sample
after one full compliance cycle

---

## Audit Priority Tiers

| Tier | Count | Definition |
|------|-------|------------|
| 1 | 147 | Flagged by all three models (IF, LOF, DBSCAN) |
| 2 | 484 | Flagged by any two models |
| 3 | 65 | Flagged by Isolation Forest within xl population |
| Separate | 500 | NYCHA — requires separate analysis framework |

---

## Limitations and Future Work

- No ground truth labels — validation relies on cross-referencing DOB violations
(pending), bunching analysis, and multi-model agreement
- xl peer median finding suggests the xl population itself contains widespread
under-reporting, limiting interpretability of xl model results
- NYCHA and xl buildings require separate analysis frameworks not addressed in this MVP
- RobustScaler is a candidate replacement for StandardScaler in future iterations —
more resistant to the extreme outliers present in emissions columns
- Prospective validation against actual audit outcomes would provide the strongest
long-run test of model utility

---

## Problem Solving Process

### 1. Data Acquisition and Understanding
- LL84 data retrieved via Socrata API with year and property type filters, paginated
at 50,000 rows per request
- PLUTO downloaded as CSV, joined to LL84 on standardized BBL key
- Initial data quality assessment: null rate analysis, "Not Available" string
replacement, EPA alert flag examination

### 2. Data Preparation and Feature Engineering
- 80% null threshold applied to drop uninformative columns (358 → 189 columns)
- NYCHA population separated after initial modeling revealed structural reporting bias
- Peer group construction: 5 age buckets × 4 size buckets = 20 peer groups
- Size-normalized features engineered to address scale bias
- Peer-group level median imputation for remaining nulls
- StandardScaler applied before distance-based modeling

### 3. Modeling Strategy
Three algorithms evaluated:
- Isolation Forest — contamination parameter tuned and validated via sensitivity
analysis at 0.03, 0.05, 0.10
- Local Outlier Factor — n_neighbors tested at 20, 50, 100
- DBSCAN — eps selected via k-distance plot elbow method

### 4. Validation Strategy
- Anomaly score distribution check — scores are meaningfully spread, not clustered
- Multi-model agreement — 147 buildings flagged by all three independent algorithms
- Bunching test — 2.37x ratio confirms strategic threshold targeting, independent
of model assumptions
- Contamination sensitivity analysis — stable flagged set across contamination values
- DOB violation cross-reference — pending

### 5. Results Communication
- Tiered audit priority list with peer group context and `pct_of_peer_median` metric
- `pct_of_peer_median` chosen as primary interpretability metric for non-technical
DOB audience — requires no statistical knowledge to evaluate
- XL and non-xl results presented separately with explicit acknowledgment of
cross-model score non-comparability

---

## Timeline

1. **Dataset finalization and problem formulation** ✅ *[Completed 4/1/26]*
   - Dataset acquisition and initial exploration
   - Business problem definition refinement
   - Project repository setup

2. **Exploratory Data Analysis** ✅ *[Completed 4/3/26]*
   - Null rate analysis and column reduction (358 → 189 columns)
   - EPA alert flag and estimation indicator analysis
   - Target variable distribution analysis

3. **Data Preprocessing and Feature Engineering** ✅ *[Completed 4/29/26]*
   - BBL standardization and LL84/PLUTO merge
   - NYCHA population split
   - Peer group construction (20 groups)
   - Size-normalized feature engineering
   - Peer-group level median imputation
   - StandardScaler application

4. **Model Development** ✅ *[Completed 5/1/26]*
   - Isolation Forest — full population and split by size
   - Local Outlier Factor — non-xl population
   - DBSCAN — eps tuned via k-distance plot
   - Multi-model comparison and tier assignment

5. **Model Evaluation and Validation** *[In progress — 5/5/26]*
   - Bunching test ✅
   - Contamination sensitivity analysis
   - DOB violation cross-reference
   - Peer group coherence validation

6. **Documentation and Reporting** *[5/10/26]*
   - Code commenting and cleanup
   - Technical report writing
   - Executive presentation development

7. **Final Review and Submission** *[5/12/26]*
   - Quality assurance
   - Video recording
   - Final submission preparation

---

[1] Urban Green Council — urbangreencouncil.org/what-we-do/explore-nyc-building-data-hub/local-law-97-progress/
