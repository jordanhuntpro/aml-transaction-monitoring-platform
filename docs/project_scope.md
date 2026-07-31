# Project Scope

## Project Title

End-to-End AML Transaction Monitoring and Typology Detection System

## Business Problem

Financial institutions process large volumes of customer and transaction data each day. Transaction monitoring systems are designed to identify potentially suspicious activity, but traditional rule-based approaches can produce large numbers of false positives. Excessive alert volume can increase investigator workload, delay reviews, and make it more difficult to focus on the activity that presents the greatest risk.

This project will develop an end-to-end AML analytics platform using synthetic customer, account, and transaction data. The platform will identify suspicious transaction patterns, generate explainable alerts, prioritize cases for investigation, and compare the performance of rule-based monitoring with machine learning approaches.

The project is designed to demonstrate the analytical, technical, and business problem-solving skills expected in Data Scientist II and Data Scientist III roles within financial crimes risk management.

## Primary Objectives

1. Generate realistic synthetic customer, account, and transaction data.
2. Inject known suspicious activity patterns into the synthetic dataset.
3. Develop configurable AML transaction monitoring rules.
4. Engineer transaction-level, account-level, customer-level, and network-level risk features.
5. Train and evaluate supervised and unsupervised machine learning models.
6. Generate explainable alerts that can support investigator review and decision-making.
7. Measure model performance, false positives, alert volume, detection coverage, and estimated operational impact.
8. Demonstrate how the solution could scale through Microsoft Azure and Databricks.
9. Present analytical findings through Power BI and an interactive Streamlit investigation application.
10. Document model assumptions, limitations, governance considerations, and potential areas for future improvement.

## Initial AML Typologies

The first version of the project will focus on the following suspicious activity patterns:

- Structuring
- Rapid movement of funds
- Transaction velocity anomalies
- Funnel account activity
- Circular movement of funds

Each typology will be represented through configurable business logic, engineered risk indicators, and synthetic transaction patterns.

## Analytical Approach

The project will compare multiple analytical approaches rather than relying on a single model.

The initial approach will include:

- Rule-based transaction monitoring
- Logistic regression as an interpretable baseline
- Gradient boosting for supervised classification
- Isolation Forest for anomaly detection
- Graph analytics for identifying unusual account relationships and fund movement patterns

The final alerting framework will combine rule triggers, machine learning risk scores, and explainable reason codes.

## Technology Stack

The project will use the following tools and platforms:

- Python
- SQL
- PySpark
- Microsoft Azure
- Azure Databricks
- Delta Lake
- MLflow
- scikit-learn
- Power BI
- Streamlit
- Git
- GitHub

## Expected Deliverables

The completed project will include:

- Synthetic customer, account, and transaction datasets
- Documented data definitions and assumptions
- AML typology injection logic
- Data quality and validation checks
- Rule-based monitoring logic
- Machine learning models
- Model evaluation results
- Explainability outputs
- Alert prioritization logic
- Graph-based transaction analysis
- Power BI dashboards
- Streamlit investigation application
- Model governance documentation
- Technical architecture documentation
- Final project summary and business recommendations

## Project Limitations

This project uses entirely synthetic data and publicly documented analytical concepts. It is an educational portfolio project and does not use or represent TD Bank data, systems, models, monitoring thresholds, internal procedures, or regulatory conclusions.

The solution is not intended for production use. It should not replace professional investigators, compliance personnel, model risk management, legal review, internal governance, or regulatory oversight.

Results generated from synthetic data should not be interpreted as evidence of real-world model effectiveness. The purpose of the project is to demonstrate technical capability, analytical judgment, business understanding, and awareness of financial crimes risk management.