
# Data Source Planning and Team Roles

---

## 🗃️ Data Sources Used (All Teams)

### 📊 Vehicle Registration and Market Data

- **VAHAN Dashboard** – https://vahan.parivahan.gov.in/vahan4dashboard/
- **Kaggle Datasets** – EV statistics, charging station locations, EV buyer preferences
- **GitHub Repositories** – Manually compiled CSVs from state EV policies and market reports

### ⚡ EV Infrastructure & Charging Stations

- **BEE India Portal / EV Yatra** – https://evyatra.beeindia.gov.in/
- **Google Places API** (planned) – For real-time charging station data

### 👥 Demographic & Behavioral Data

- **Census 2011, NSSO** – Population, income, urbanization
- **Google Trends API** (planned) – State-wise interest in EV-related search terms
- **Survey Data (if available)** – Used for behavioral analysis

---

## 👥 Team Roles and Responsibilities (As per Folder Assignments)

---

### 🧩 Team 1 – Aditya Rastogi and Nakkanaboina Deekshitha

#### 📁 01_Problem_Breakdown/
- Broke down the EV market problem using Fermi estimation and adoption lifecycle.
- Defined market segmentation strategies and data source plans.

#### 📁 02_Data_Collection/scripts/web_scraping/
- Scraped data from VAHAN and EV Yatra websites.
- Planned scraping of charging station data and real-time adoption statistics.

#### 📁 03_Data_Analysis/notebooks/clustering_analysis.ipynb
- Performed clustering analysis on collected EV and infrastructure data to segment regions and user types.

#### 📁 Supporting_Documents/Data_Sources_References.md
- Documented all datasets and web sources used in the project.

---

### 🧩 Team 2 – Saurabh Doke and Yogeshvar Chaudhari

#### 📁 02_Data_Collection/scripts/data_cleaning/
- Cleaned and merged vehicle registration, demographic, and behavioral datasets.

#### 📁 03_Data_Analysis/notebooks/regression_analysis.ipynb
- Developed regression models to estimate EV adoption potential.

#### 📁 03_Data_Analysis/Statistical_Analysis_and_Segmentation_Modeling.md
- Documented insights from statistical analysis and defined segmentation rules.

#### 📁 Supporting_Documents/Glossary_and_Definitions.md
- Maintained a glossary of terms and definitions used across the project.

---

### 🧩 Team 3 – Anik Parui and Arkaprava Bhandari

#### 📁 02_Data_Collection/scripts/api_integration/
- Planned and implemented data collection via APIs (e.g., Google Places API for charging stations).

#### 📁 03_Data_Analysis/notebooks/geographic_mapping.ipynb, visualization.ipynb
- Created visualizations and maps to support geographic segmentation and insights.

#### 📁 04_Strategy_Development/ (all .md files)
- Wrote strategic documents on pricing, go-to-market strategy, and risk planning.

#### 📁 Supporting_Documents/Project_Timeline_and_Milestones.md
- Maintained the overall project timeline and milestone tracking.

---

## ✅ Summary

Each team was assigned focused tasks across the data pipeline.  
- **Team 1** handled decomposition, scraping, and clustering.  
- **Team 2** managed data cleaning, regression, and segmentation logic.  
- **Team 3** developed visuals, API data integration, and final strategy writing.

Together, these efforts provide a full end-to-end analysis of India's EV market for informed decision-making.
