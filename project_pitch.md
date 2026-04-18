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




<!-- ## Business Problem
Local Law 97 (LL97), enacted in 2019 and effective in 2024, has been described by the NYC Department of Buildings as one of the most ambitious building emissions laws in the nation. LL97 places carbon caps on buildings larger than 25,000 square feet as these buildings account for over two-thirds of NYC's greenhouse gas emissions. While NYC is known for its iconic skyline with large skyscrapers and corporate buildings, multifamily buildings account for nearly 60% of the buildings covered by LL97. Most of these buildings are low-rise buildings, 7 stories or fewer, and were constructed before 1940 (pre-WWII). Additionally, the Urban Green Council analyzed 2023 benchmarking data and found 57% of all properties currently emit more greenhouse gases than their 2030 cap. This represents a significant financial exposure as buildings that exceed their limits face fines of $268 per metric ton of CO2 over their cap. For example, > A 100,000 sq ft building emitting 132 MT over its cap faces a **$35,376 annual fine** — recurring every year until compliant. >

The current process for reporting emissions has a potential gap for misreporting data. Building owners submit their own energy consumption data to the city which is then certified by a Registered Design Professional (RDP), an engineer or architect. The RDP, which is hired by the building owner, reviews and signs the submission before it goes to the NYC Department of Buildings (DOB). Because the RDP does not independently verify the utility readings, there is a potential risk of misreporting energy consumption data.

The NYC Department of Buildings (DOB) lacks the capacity to independently audit all 50,000 covered buildings and currently has no principled method for prioritizing which ones to investigate. A simple threshold-based approach cannot capture the multivariate patterns that distinguish genuinely anomalous reporting from normal variation across building types, ages, and neighborhoods. However, a machine learning model is well-suited to systematically identify which buildings warrant closer scrutiny at a scale and specificity no manual process could match. -->

## Stakeholders

The NYC DOB is the direct user and primary stakeholder of this project as the DOB currently has no principled method for selecting which buildings to prioritize for investigation. This model provides a ranked risk score for each covered building, enabling auditors to focus resources where they are most likely to find data discrepancies.

The NYC Mayor's Office of Climate and Environmental Justice has publicly committed to strict enforcement of LL97, making a systematic audit prioritization tool directly aligned with the administration's stated policy position.

The NYC Accelerator, the city's free technical assistance program for building owners, serves as a natural downstream partner. Buildings flagged by the model and subsequently audited can be connected to the Accelerator for guidance on retrofit pathways and compliance planning.

Building owners, particularly in the multifamily residential sector, are indirect beneficiaries — early identification of data discrepancies gives owners time to correct reporting and plan retrofits before fines compound annually.

The Urban Green Council, a nonprofit research organization that tracks LL97 compliance across the city's building stock, benefits indirectly from improved data quality in the benchmarking system — more accurate reported emissions makes their policy research and compliance analysis more reliable.

## Primary goals
 - needs a rewrite
The primary goal of the project is to strategically target buildings for auditing. By augmenting the auditing process buildings will have no choice but increase compliance and retrofit. This could result in a large decrease in carbon emissions by 2030. Reducing carbon emissions will decrease operational bills like utilities.

missing -
Improved accuracy of the city's emissions dataset as a standalone goal
The financial recovery angle — potential penalty revenue from corrected buildings
Explicit connection to the 2030 compliance deadline as the business urgency


## Why is Machine Learning A Good Fit for this Problem?

The sheer scale of the problem, over 50,000 buildings subject to Local Law 97,  makes comprehensive manual review impractical at scale, and machine learning is the only practical path to comprehensive coverage. Simple rule-based systems cannot capture the complex, multivariate patterns that emerge across building age, size, type, and neighborhood, whereas ML models can learn these relationships simultaneously. Unsupervised anomaly detection is particularly well-suited here because it identifies statistical outliers without requiring labeled examples of fraud or misreporting, which are rarely available. An impact segmentation layer then ensures that flagged buildings are prioritized by the consequence of non-compliance, not merely by anomaly likelihood, and peer group comparison is made possible through clustering across multiple dimensions at once.

## Datasets and Relevance

Given the complexity of the covered building universe, this project scopes to multifamily residential buildings as an MVP as this building type represents nearly 60% of covered square footage, has the most homogeneous physical characteristics for peer comparison, and faces the steepest compliance challenge ahead of the 2030 cap tightening.

1. NYC Energy and Water Data Disclosure (LL84)
Sourced from NYC Open Data, LL84 covers all buildings over 25,000 square feet and has been collected annually since 2011, providing over a decade of longitudinal reporting. It includes key variables such as energy consumption by fuel type, water usage, EPA Energy Star score, property ID, and BBL. This dataset is the analytical core of the model — it contains the self-reported emissions figures that are directly examined for anomalies, inconsistencies, and patterns indicative of misreporting.
2. PLUTO (Primary Land Use Tax Lot Output)
PLUTO is published by the NYC Department of City Planning and available through NYC Open Data, with coverage extending to every tax lot in the five boroughs. Its variables include building age, gross square footage, number of units, zoning classification, land use code, ownership information, assessed value, and the number of buildings on a lot. This dataset supplies the physical and ownership characteristics used to construct meaningful peer groups and calculate the expected emissions benchmarks against which each building's reported figures are evaluated.
3. DOB Violations
The DOB Violations dataset is drawn from the NYC Department of Buildings via NYC Open Data and encompasses all violation records across the city, including violation type, date, BBL, and disposition status. While not a direct measure of emissions fraud, LL84 non-compliance violations serve as a weak proxy label for buildings with a history of reporting problems, making this dataset valuable for model validation and calibration.

## Success Metrics

- Technical Metrics
  -  The model's performance will be assessed first by examining the anomaly score distribution across the full building population, ensuring scores are meaningfully differentiated rather than clustered.
  - Precision will be evaluated within the flagged set by cross-referencing against DOB violation history as weak proxy labels, providing an accessible ground-truth signal.
  - Peer group coherence will be tested to confirm that buildings assigned to the same cluster exhibit genuinely similar emissions profiles, validating the segmentation logic.
  - A bunching test will also be applied to detect statistically significant density of buildings reporting just below the compliance threshold, a classic indicator of strategic misreporting.

- Business Metrics
  - On the operational side, success will be measured by comparing the rate of data corrections or amendments among audited flagged buildings against a random baseline sample.
  - The model will also be evaluated on its ability to quantify the emissions gap between reported values and peer-expected benchmarks across flagged properties
  - The dollar value of potential penalty recovery — assuming flagged buildings are brought into accurate compliance — will serve as a direct measure of fiscal impact.
  - Finally, prospective validation will compare outcomes from model-selected audits against a control sample after one full compliance cycle, providing the strongest long-run test of the model's real-world utility.

[1] Urban Green Council — urbangreencouncil.org/what-we-do/explore-nyc-building-data-hub/local-law-97-progress/

# Problem Solving Process
1. Data Acquisition and Understanding

How you will obtain and explore the dataset
Initial data quality assessment plan
--- merging on BBL, handling missing values, filtering to multifamily residential

Preliminary visualization strategy

2. Data Preparation and Feature Engineering

Data cleaning approach
Feature selection/engineering methodology
Implementation plan for sci-kit learn Pipeline

3. Modeling Strategy
Algorithms you plan to evaluate (minimum 3)
+ Isolation Forest — well-suited for tabular data anomaly detection, handles high dimensionality, interpretable contamination parameter
+ Local Outlier Factor (LOF) — detects anomalies relative to local neighborhood density, which aligns well with your peer group logic
+ DBSCAN — density-based clustering that naturally identifies outliers as noise points

Cross-validation strategy

+ Anomaly score distribution — for Isolation Forest and LOF, you examine whether scores are meaningfully spread across the population rather than clustered around one value. A model that flags everything or nothing is useless.

+ Cross-reference your flagged buildings against DOB violation history. You're not training on violations — you're checking after the fact whether buildings your model flagged are disproportionately represented in the violation records. This is the closest thing to ground truth you have.

+ Bunching test — self-validating
As we discussed earlier, if you find a statistically significant cluster of buildings reporting just below their compliance threshold, that finding validates itself independently of the model. It doesn't require labels at all.


-----

Contamination sensitivity analysis — Isolation Forest requires you to set a contamination parameter (expected proportion of anomalies). You test multiple values and examine how the flagged set changes. Stable flagging across a range of contamination values suggests robust anomalies.

----


+ Prospective validation as your honest acknowledgment that full validation requires real-world deployment

Hyperparameter tuning approach
Evaluation metrics selection and justification

4. Results Interpretation and Communication
How will you translate model results into business insights
Visualization plans for model performance and feature importance
Strategy for explaining technical concepts to non-technical stakeholders

5. Conceptual Framework
Include a flowchart of your proposed solution pipeline
Outline dependencies between different stages of your project

# Timeline

1. Dataset finalization and problem formulation - [4/1/26]

- :white_check_mark: Dataset acquisition and initial exploration
- :white_check_mark: Business problem definition refinement
- :white_check_mark: Project repository setup

2. Exploratory Data Analysis - [4/3/26]

- [ ] Comprehensive data profiling
- [ ] Statistical analysis of relationships
- [ ] Creation of informative visualizations
- [ ] Documentation of insights

3. Data Preprocessing - [TIME]

- [ ] Data cleaning implementation
- [ ] Feature engineering
- [ ] Pipeline development
- [ ] Data splitting (train/validation/test)

4. Model Development - [4/30/26]
- [ ] Implementation of baseline models
- [ ] Algorithm comparison
- [ ] Hyperparameter tuning
- [ ] Cross-validation

5. Model Evaluation and Refinement - [5/5/26]

- [ ] Final model selection
- [ ] Performance evaluation on test data
- [ ] Business metric calculation
- [ ] Interpretation of results

6. Documentation and Reporting - [5/10/26]

- [ ] Code commenting and cleanup
- [ ] Technical report writing
- [ ] Executive presentation development

7. Final Review and Submission - [5/12/26]

- [ ] Quality assurance
- [ ] Video recording
- [ ] Final submission preparation
- [ ] Identify potential challenges or areas where you might need to conduct additional research or learning.
