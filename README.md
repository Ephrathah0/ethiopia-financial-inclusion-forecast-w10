Forecasting Financial Inclusion in Ethiopia
Project Overview
This project develops a transparent, policy-oriented forecasting system to analyze and project Ethiopia’s financial inclusion trajectory using the World Bank Global Findex framework.

The analysis focuses on two core dimensions:

Access — Account Ownership Rate
Usage — Digital Payment Adoption Rate
Given limited historical survey data, the project emphasizes event-based reasoning, scenario analysis, and explicit treatment of uncertainty rather than complex machine learning models.

Business Context
Ethiopia is undergoing rapid digital financial transformation driven by:

Expansion of mobile money platforms (Telebirr, M-Pesa)
Market liberalization and new entrants
National digital infrastructure initiatives
Despite these developments, financial inclusion growth has slowed, raising important policy questions that this project aims to explore.

Project Objectives
Understand and enrich financial inclusion data for Ethiopia
Analyze historical patterns and structural gaps
Model the impact of major events and policy interventions
Forecast financial inclusion outcomes for 2025–2027
Communicate insights through an interactive dashboard
Data
Primary Dataset: ethiopia_fi_unified_data.csv
Reference Codes: reference_codes.csv
Data follows a unified schema supporting observations, events, and modeled impact links.
Additional data sources are documented in data_enrichment_log.md.

Methodology Overview
Exploratory Data Analysis (EDA) on sparse time-series data
Event impact modeling using lagged, additive effects
Trend-based and scenario-driven forecasting
Explicit uncertainty representation via confidence ranges
Interactive visualization using Streamlit
Project Structure
data/ — Raw and processed datasets
notebooks/ — Task-based analysis notebooks
src/ — Reusable data processing and modeling logic
dashboard/ — Interactive Streamlit application
reports/ — Figures and written summaries
