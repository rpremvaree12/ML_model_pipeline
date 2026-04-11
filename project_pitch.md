# Business Problem and Scope
1. Clearly articulate the business problem or challenge that your model will address
2. Identify the specific stakeholders who would benefit from your solution.
3. Define the primary goals of your project in terms of business outcomes.
4. Explain why a machine learning approach is appropriate for this problem.
5. Describe the dataset/s you've chosen, including their source, size, and key variables.
6. Connect the dataset (s) ' relevance to your business problem.
7. Define how you will measure success from both technical and business perspectives.

In 2019, the most ambitious building emissions legislation in New York City, Local Law 97, was enacted to reduce carbon emissions for buildings larger than 25,000 square feet. In 2024 Local Law 97 went into effect by placing carbon caps on buildings larger than 25,000 square feet. These buildings are responsible for more than two-thirds of NYC's greenhouse gas emissions. Currently, building owners submit their own energy consumption data to the city. While the submission must be certified by a Registered Design Professional (RDP), an engineer or architect, the RDP is hired by the building owner, not an independent auditor by the city. Since the RDP does not independently verify the utility consumption figures are accurate there is a potential risk of misreporting energy consumption. No systematic, data-driven prioritization method currently exists. A machine learning model would be well-suited to address this need as carbon emission caps are slated to tighten in 2030.

[1] Urban Green Council — urbangreencouncil.org/what-we-do/explore-nyc-building-data-hub/local-law-97-progress/

Based on 2023 benchmarking data, Urban Green Council states about 57 percent of properties currently emit more greenhouse gases than their 2030 cap. [1]




The primary stakeholder is the NYC Department of Buildings (DOB). With over 50,000 buildings to potentially audit, implementing this model could yield increased compliance by increasing oversight. Other stakeholders include the NYC Accelerator (https://accelerator.nyc/), an organization that 'provides free resources, training, and one-on-one expert guidance to help building owners and industry professionals improve energy efficiency and reduce carbon emissions from buildings in NYC.' While the NYC Accelerator provides a tool to access specific information about buildings and predicts future potential fees, this tool does this passively. The NYC Accelerator could implement this tool to identify the high-impact buildings that need the most support and actively reach out with targeted campaigns or support. The Accelerator could implement financial support as well to buildings and the model would give insight to which buildings to prioritize for support.

The primary goal of the project is to strategically target buildings for auditing. By augmenting the auditing process buildings will have no choice but increase compliance and retrofit. This could result in a large decrease in carbon emissions by 2030. Reducing carbon emissions will decrease operational bills like utilities.
avoiding steep emission fines $268 per metric ton = hundreds of thousands or millions in 2030 where caps tighten. upgrading infrastructure reduces the cost of emergency repairs.

Machine learning is appropriate here as we can leverage unsupervised models to identify groupings and anomaly reportings for 50,000 or more buildings. While auditing is valuable to ensure compliance to LL97, implementing this targeted auditing practice will lighten auditors caseload. Here we hope to minimize false positives (buildings that labeled as audited but not needing it)

Success will be if the machine learning model is more effective than random sampling for auditing and if the auditing results in a large enough decrease of carbon emissions through enforcement.

Focus on multifamily residential homes which

# Problem Solving Process
1. Data Acquisition and Understanding

How you will obtain and explore the dataset
Initial data quality assessment plan
Preliminary visualization strategy

2. Data Preparation and Feature Engineering

Data cleaning approach
Feature selection/engineering methodology
Implementation plan for sci-kit learn Pipeline

3. Modeling Strategy
Algorithms you plan to evaluate (minimum 3)
Cross-validation strategy
Hyperparameter tuning approach
Evaluation metrics selection and justification

classification so logistic regression, random forest,

4. Results Interpretation and Communication
How will you translate model results into business insights
Visualization plans for model performance and feature importance
Strategy for explaining technical concepts to non-technical stakeholders

5. Conceptual Framework
Include a flowchart of your proposed solution pipeline
Outline dependencies between different stages of your project

# Timeline

1. Dataset finalization and problem formulation - [4/1/26]

[ ] Dataset acquisition and initial exploration
[ ] Business problem definition refinement
[ ] Project repository setup

2. Exploratory Data Analysis - [4/3/26]

[ ] Comprehensive data profiling
[ ] Statistical analysis of relationships
[ ] Creation of informative visualizations
[ ] Documentation of insights

3. Data Preprocessing - [TIME]

[ ] Data cleaning implementation
[ ] Feature engineering
[ ] Pipeline development
[ ] Data splitting (train/validation/test)

4. Model Development - [4/30/26]
[ ] Implementation of baseline models
[ ] Algorithm comparison
[ ] Hyperparameter tuning
[ ] Cross-validation

5. Model Evaluation and Refinement - [5/5/26]

[ ] Final model selection
[ ] Performance evaluation on test data
[ ] Business metric calculation
[ ] Interpretation of results

6. Documentation and Reporting - [5/10/26]

[ ] Code commenting and cleanup
[ ] Technical report writing
[ ] Executive presentation development

7. Final Review and Submission - [5/12/26]

[ ] Quality assurance
[ ] Video recording
[ ] Final submission preparation
[ ] Identify potential challenges or areas where you might need to conduct additional research or learning.
