# Data Dictionary

## Purpose

This document defines the initial synthetic data fields used in the AML transaction monitoring and typology detection project. The data structure is designed to support rule-based monitoring, feature engineering, machine learning, graph analytics, alert generation, and investigator review.

All records in this project are synthetic and do not represent real customers, accounts, transactions, or financial institutions.

## Customer Data

| Field | Data Type | Description |
|---|---|---|
| customer_id | String | Unique synthetic identifier assigned to each customer |
| customer_type | String | Identifies whether the customer is an individual or business |
| customer_risk_rating | String | Initial customer risk category such as Low, Medium, or High |
| country | String | Customer country of residence or registration |
| state | String | Customer state or regional location |
| occupation_or_industry | String | Customer occupation for individuals or industry for businesses |
| customer_since | Date | Date the customer relationship began |
| expected_monthly_volume | Decimal | Estimated normal monthly transaction volume |
| expected_transaction_count | Integer | Estimated normal number of monthly transactions |
| is_pep | Boolean | Indicates whether the synthetic customer is identified as a politically exposed person |
| adverse_media_flag | Boolean | Indicates whether an adverse media indicator is present |
| sanctions_flag | Boolean | Indicates whether a sanctions-related indicator is present |

## Account Data

| Field | Data Type | Description |
|---|---|---|
| account_id | String | Unique synthetic identifier assigned to each account |
| customer_id | String | Customer associated with the account |
| account_type | String | Account category such as checking, savings, or business checking |
| account_open_date | Date | Date the account was opened |
| account_status | String | Current account status such as Active, Dormant, or Closed |
| opening_balance | Decimal | Initial account balance |
| current_balance | Decimal | Most recent account balance |
| account_country | String | Country where the account is maintained |
| account_state | String | State or regional location associated with the account |
| digital_banking_enrolled | Boolean | Indicates whether the account is enrolled in digital banking |

## Transaction Data

| Field | Data Type | Description |
|---|---|---|
| transaction_id | String | Unique synthetic identifier assigned to each transaction |
| account_id | String | Account associated with the transaction |
| counterparty_account_id | String | Destination or originating account associated with the transaction |
| customer_id | String | Customer associated with the transaction |
| transaction_timestamp | Datetime | Date and time the transaction occurred |
| transaction_type | String | Transaction category such as cash deposit, wire, ACH, card, or transfer |
| transaction_direction | String | Indicates whether the transaction is incoming or outgoing |
| transaction_amount | Decimal | Monetary value of the transaction |
| transaction_currency | String | Currency used for the transaction |
| channel | String | Channel used such as branch, ATM, online, mobile, or wire platform |
| origin_country | String | Country where the transaction originated |
| destination_country | String | Country where the transaction was sent |
| merchant_or_counterparty | String | Synthetic merchant or counterparty name |
| transaction_description | String | Synthetic transaction memo or description |
| balance_after_transaction | Decimal | Account balance immediately after the transaction |
| is_cross_border | Boolean | Indicates whether the transaction crossed national borders |
| is_cash_transaction | Boolean | Indicates whether the transaction involved cash |
| is_high_risk_country | Boolean | Indicates whether the transaction involved a designated high-risk jurisdiction |

## Typology and Label Data

| Field | Data Type | Description |
|---|---|---|
| is_suspicious | Boolean | Indicates whether the transaction was generated as suspicious activity |
| typology_label | String | Suspicious activity category assigned to the transaction |
| scenario_id | String | Identifier connecting transactions that belong to the same suspicious scenario |
| rule_triggered | Boolean | Indicates whether a rule-based monitoring scenario generated an alert |
| rule_name | String | Name of the rule that generated the alert |
| model_risk_score | Decimal | Machine learning risk score assigned to the transaction or customer |
| alert_priority | String | Alert priority such as Low, Medium, High, or Critical |
| explanation_code | String | Reason code explaining why the transaction or customer was prioritized |

## Initial Typology Labels

The initial synthetic dataset will support the following labels:

- Normal Activity
- Structuring
- Rapid Movement of Funds
- Transaction Velocity Anomaly
- Funnel Account Activity
- Circular Movement of Funds

## Data Quality Expectations

The dataset will be validated for:

- Unique identifiers
- Required fields
- Valid date ranges
- Nonnegative transaction amounts
- Valid account and customer relationships
- Consistent transaction directions
- Valid categorical values
- Reasonable account balances
- Controlled suspicious activity rates
- Reproducible synthetic data generation

## Privacy and Confidentiality

This project does not use production data, TD Bank data, customer information, internal monitoring rules, or proprietary methodologies. All names, identifiers, balances, risk indicators, transactions, and outcomes are synthetic.