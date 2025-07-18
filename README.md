# EV Market Analysis Project

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python Version](https://img.shields.io/badge/Python-3.8%2B-blue)](https://www.python.org/downloads/)

## Project Overview

The **EV Market Analysis Project** is a comprehensive analysis of India's electric vehicle (EV) market, focusing on market potential, adoption drivers, and strategic recommendations for entry and growth. This project leverages data from government sources, consumer surveys, and environmental metrics to provide insights across six key dimensions:  
- **Two-Wheeler (2W)**: Dominant mass-market segment.  
- **Four-Wheeler (4W)**: Emerging premium and family segment.  
- **Age**: Segmentation by generations (e.g., Gen Z, Millennials).  
- **Income**: Targeting based on economic brackets (low, middle, high).  
- **Geographical Area**: Urban, Tier-2, rural, and state-wise analysis.  
- **Pollution Levels**: Correlation with EV adoption and environmental benefits.  

The goal is to support EV startups, OEMs, or policymakers in making data-driven decisions for market entry, pricing, partnerships, and sustainability positioning. Key outputs include statistical models, forecasts, visualizations, and strategic frameworks.

This repository contains all project artifacts: documentation, raw/processed data, analysis notebooks, scripts, and strategy reports. It is designed for collaborative use by data analysts, strategists, and stakeholders.

## Project Objectives
- **Problem Breakdown**: Decompose the EV market opportunity using Fermi estimation and adoption lifecycle models.  
- **Data Collection**: Gather and validate multi-source data (government, surveys, B2B).  
- **Data Analysis**: Perform clustering, regression, and geospatial modeling to uncover insights.  
- **Strategy Development**: Recommend entry sequences, pricing, partnerships, and risk mitigation.  
- **Final Presentation**: Summarize findings with KPIs and executive reports.  
- **Specialized Analysis**: Deep dives into vehicle categories, demographics, geography, and environmental impact.

## Key Features
- **Data-Driven Insights**: Uses real datasets from MoRTH, CPCB, Kaggle, and custom surveys.  
- **Analytical Tools**: Jupyter notebooks for regression, clustering, and visualization.  
- **Strategic Outputs**: Phased market entry plans, pricing frameworks, and risk assessments.  
- **Six-Point Focus**: Ensures holistic coverage of vehicle types, demographics, regions, and environmental factors.  
- **Reproducibility**: Scripts for data utils, analytics pipelines, and integrations.



## Installation and Setup
1. **Clone the Repository**  
git clone https://github.com/yourusername/EV_Market_Analysis_Project.git
cd EV_Market_Analysis_Project

text

2. **Create Virtual Environment**  
python -m venv venv
source venv/bin/activate # On Windows: venv\Scripts\activate

text

3. **Install Dependencies** (from `requirements.txt` in root)  
pip install -r requirements.txt

text
(Requirements include: pandas, numpy, matplotlib, seaborn, scikit-learn, geopandas, scipy, jupyter, jupytext)

4. **Download Data**  
- Place raw datasets in `02_Data_Collection/raw_data/` subfolders (e.g., from MoRTH, Kaggle, CPCB).  
- Refer to `Data_Sources_References.md` for links.

## Usage
### Running Notebooks
- Navigate to `03_Data_Analysis/notebooks/`.  
- Convert scripts to notebooks if needed:  
jupytext --to notebook geographical_adoption_analysis.py

text
- Launch Jupyter:  
jupyter notebook

text
- Open and run notebooks (e.g., `regression_analysis.ipynb`) to generate processed data and visualizations.

### Running Scripts
- Go to `scripts/`:  
cd scripts
python integrated_analysis_pipeline.py # Runs full pipeline; update paths inside

text

### Generating Outputs
- Run analysis notebooks to populate `processed_data/` (e.g., CSVs, PNGs).  
- Use strategy docs in `04_Strategy_Development/` for planning sessions.

### Full Project Workflow
1. Review `01_Problem_Breakdown/` for context.  
2. Collect data per `02_Data_Collection/` guides.  
3. Analyze with `03_Data_Analysis/` notebooks.  
4. Develop strategies from `04_Strategy_Development/`.  
5. Prepare presentations using `05_Final_Presentation/`.  
6. Dive deeper with `06_Specialized_Analysis/`.

## Dependencies
- Python 3.8+  
- Libraries: See `requirements.txt` (pandas, scikit-learn, etc.)  
- Tools: Jupyter Notebook, Git

## Data Sources
- Government: MoRTH (EV registrations), CPCB (AQI/pollution).  
- Surveys: Custom (age/income demographics).  
- External: Kaggle datasets (e.g., India EV Market Data).  
- Full list in `Supporting_Documents/Data_Sources_References.md`.

## Team and Contributors
- **Team A**: Data Collection & Vehicle Categories.  
- **Team B**: Demographics & Geography.  
- **Team C**: Environmental & Strategy.  
- Contributors: [Your Name/Team] – Based on three-team distribution framework.

For roles and timeline, see `Project_Timeline_and_Milestones.md`.

## License
This project is licensed under the MIT License – see the [LICENSE](LICENSE) file for details.

## Contact
For questions, issues, or contributions:  
- Email: your.email@example.com  
- GitHub Issues: Open a new issue in this repo.

*Last Updated: July 2025*  
This project is for educational and analytical purposes. Data is approximate and should be verified with latest sources.
