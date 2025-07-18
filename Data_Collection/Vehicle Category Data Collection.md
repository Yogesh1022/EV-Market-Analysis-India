# Vehicle Category Data Collection 

This document provides a detailed overview of the datasets used  to conduct segmentation, trend analysis, and strategic planning for Two-Wheelers (2W) and Four-Wheelers (4W) in the Indian Electric Vehicle (EV) market.

---

## 📁 Dataset 1: EV_India_2014-2025_MarketData.csv

### 🔹 Description:
A comprehensive dataset covering EV registrations from 2014 to 2025 across Indian states, segmented by vehicle type (2W, 3W, 4W) and consumer attributes.

### 🔑 Key Columns:
- `Year`
- `State`
- `Vehicle Type` (2W / 3W / 4W)
- `Registrations`
- `EV Share (%)`
- `Monthly Income Bracket (Main Buyer)`
- `Age Group`
- `City Type`
- `Psychographic Segment`
- `Chargers`
- `FAME II Policy`

### 🎯 Use in Analysis:
- Analyze 2W and 4W EV adoption over time
- Identify buyer personas (e.g., income, age, psychographic segments)
- Perform deep-dive segmentation for 2W and 4W strategy
- Used in `two_wheeler_analysis.ipynb`, `four_wheeler_analysis.ipynb`, and specialized notebooks

---

## 📁 Dataset 2: ev_sales_by_category_2018_2023.csv

### 🔹 Description:
Category-wise EV sales data from 2018 to mid-2023, including total vehicle sales, EV sales, and EV share (%) across years.

### 🔑 Key Columns:
- `Vehicle Category` (2W, 3W, 4W, Goods, Public Service)
- Yearly columns:
  - `2018 - Total`, `2018 - EV`, `2018 - %`
  - ...
  - `2023 (Till 01-08-2023) - Total`, `EV`, `%`

### 🎯 Use in Analysis:
- Study growth trends in EV adoption across vehicle categories
- Compare 2W and 4W penetration rates year-on-year
- Support strategic prioritization of vehicle segments
- Visualized in category trend plots and share bar charts

---

## 📁 Dataset 3: ev_registration_percentage_by_state.csv

### 🔹 Description:
State-wise EV penetration as of 2023, showing the percentage of EVs among all vehicles registered in each state/UT.

### 🔑 Key Columns:
- `State/ UT`
- `Total EV`
- `Total Vehicles Sold`
- `% of Share of EV in Total Vehicles Sold`

### 🎯 Use in Analysis:
- Identify high-adoption and low-adoption states
- Segment regions based on EV maturity (for clustering)
- Compare state-level readiness for 2W vs 4W rollout
- Integrated with infra and sales data for geo-targeting

---

## 📁 Dataset 4: charging_stations_data.csv

### 🔹 Description:
State-wise number of operational public EV charging stations as of 02-Feb-2024. Extracted manually from government reports (ANNEXURE-II, Ministry of Power).

### 🔑 Key Columns:
- `S.No`
- `State`
- `Operational_Charging_Stations`

### 🎯 Use in Analysis:
- Measure infrastructure readiness (especially for 4W EVs)
- Calculate EVs per charging station (EV/PCS) metric
- Identify states with infra bottlenecks vs well-equipped markets
- Supports strategic entry decisions for 4W segment

---

## ✅ Summary

Together, these datasets provide a complete foundation for:
- 📊 Vehicle category-wise EV adoption trends
- 🔍 State-level market maturity & readiness
- 👥 Target customer profiling
- 📍 Geographic & infrastructure-based segmentation

They enable to develop clear, data-driven strategic recommendations for the Indian 2W and 4W electric vehicle markets.
