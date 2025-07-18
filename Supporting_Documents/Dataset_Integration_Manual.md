# Dataset Integration Manual
This manual provides instructions for integrating the various datasets used in this project.

## 1. Primary Key
The primary key for joining most datasets at a granular level should be a combination of **`State`**, **`City`**, and **`Month-Year`**.

## 2. Joining Instructions
- **`geographic_adoption_patterns.csv` + `state_wise_demographics.csv`**: Join on `State` to enrich adoption data with demographic context.
- **`pollution_levels_by_city.csv` + `geographic_adoption_patterns.csv`**: Join on `City` and `Month-Year` to prepare data for correlation analysis.
- **`age_income_demographics.csv` + `purchase_intention_survey.csv`**: Join on a unique `respondent_id` to link demographics to behavior.

## 3. Tooling
- **Python:** Use the `pandas` library for all data merging and manipulation. Refer to `scripts/data_utils.py` for helper functions.
- **Notebooks:** All integration logic should be clearly documented in the Jupyter notebooks within the `03_Data_Analysis/notebooks/` directory.

## 4. Data Cleaning
Before merging, ensure data types are consistent (e.g., `State` names are uniformly formatted). Run validation checks for null values and outliers after every merge operation.