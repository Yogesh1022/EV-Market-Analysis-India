# 🚘 Vehicle Category Analysis (2W & 4W)

This report presents an in-depth analysis of the adoption, growth, and charging infrastructure of two-wheeler (2W) and four-wheeler (4W) electric vehicles (EVs) in India. The findings are derived from curated datasets including registration trends, state-wise adoption percentages, psychographic segmentation, and charging station availability.

---

## 🛵 Two-Wheeler EV Analysis

### 1. National Registration Trend (2014–2025)
- The 2W EV market witnessed **exponential growth in 2018 and 2019**, attributed to policy incentives.
- **COVID-19 caused a dip in 2020**, but the market stabilized afterward.
- A strong comeback is forecasted for 2025 with **62.98% YoY growth**.

---

### 2. State-wise 2W EV Registrations

Top contributors to 2W EV volumes in 2025:
- **Karnataka**
- **Delhi**
- **Maharashtra**
- **Punjab**
- **Uttar Pradesh**

📊 Bar charts show significant adoption concentration in urban and tech-savvy regions.

---

### 3. Psychographic Segmentation (from EV India 2014–2025)
- 2W EV buyers fall into **practical**, **eco-conscious**, and **cost-conscious** personas.
- Appeal is highest among youth, commuters, and middle-income households.

---

### 4. EV % Share by State

Using `ev_registration_percentage_by_state.csv`, the top states by % EV share in total vehicles sold:
- **Delhi: 7.72%**
- **Karnataka: 4.8%**
- **Uttar Pradesh: 4.2%**
- **Maharashtra: 4.0%**
- **Rajasthan: 3.6%**

These states lead in early adoption.

---

### 5. Clustering Analysis by State (2W Registrations)
Using KMeans clustering:
- States were grouped into **Low**, **Medium**, and **High adoption** clusters.
- Clusters were assigned based on **actual average volumes** to ensure interpretability.

---

### 6. Charging Infrastructure Readiness

EVs per Charging Station (PCS) was calculated to identify infra-stressed states.

🔌 **Most Infra-Stressed States** (High EVs per station):
- **Assam**: 1750 EVs per charging station
- **Bihar**: 1725 EVs per charging station
- **Uttar Pradesh**: 1100 EVs per charging station
- **Tripura**: 1075 EVs per charging station
- **Chandigarh**: 1025 EVs per charging station

These states have the highest number of EVs per charging station, indicating the greatest infrastructure stress.

---

## 🚗 Four-Wheeler EV Analysis

### 1. National Registration Trend (2018–2025)
- The 4W market shows **consistent but slow growth**.
- EV adoption in 4W is yet to cross 2% of total registrations nationally.

---

### 2. Top States by 4W Registrations (2025)
- **Maharashtra**
- **Telangana**
- **Punjab**
- **Uttar Pradesh**
- **Rajasthan**

Urban states dominate due to better infrastructure and early adoption policies.

---

### 3. Psychographic Segmentation
- 4W EV buyers are typically **eco-conscious**, **tech-savvy**, and **practical**.
- Preference for performance, brand value, and premium features.

---

### 4. EV % Share by State

Using `ev_registration_percentage_by_state.csv`, the top states by % EV share in total vehicles sold:
- **Delhi: 7.7%**
- **Karnataka: 4.8%**
- **Uttar Pradesh: 4.3%**
- **Maharashtra: 3.9%**
- **Rajasthan: 3.6%**

This helped identify both high-volume and high-penetration states.

---

### 5. Charging Infrastructure Readiness (4W Focus)
- Merged charging data with 4W registration volumes.
- Calculated **EVs per charging station** to assess readiness.
- States like **Assam**, **Bihar**, and **Uttar Pradesh** urgently need more public charging infrastructure to support the growing EV adoption.

---

## 📌 Summary Insights

| Metric                    | 2W EVs                        | 4W EVs                         |
|---------------------------|-------------------------------|--------------------------------|
| Growth Pattern            | Exponential post-2018         | Slow but steady                |
| Top Adopting States       | Karnataka, Maharashtra, UP    | Maharashtra, Delhi, Karnataka  |
| Psychographic Segments    | Practical, cost-conscious     | Eco-conscious, tech-savvy      |
| Infra-Stressed States     | Bihar, UP, Assam              | Assam, Bihar, UP               |
| EV % in Total Vehicles    | Delhi                         | Maharashtra                    |

---

✅ **Alignment with Project Responsibilities**

This analysis fulfills our core tasks:
- **Vehicle-wise segmentation & trends**
- **Market adoption insights**
- **Charging infrastructure readiness**
- **Support for strategy & clustering**

---
