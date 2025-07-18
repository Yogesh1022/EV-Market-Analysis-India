# integrated_analysis_pipeline.py
# Orchestrates the end-to-end multi-factor analysis pipeline for EV market

import pandas as pd
from vehicle_category_analytics import calculate_category_share
from demographic_analysis_tools import segment_by_age
from pollution_correlation_calculator import pollution_ev_correlation


def run_full_analysis(paths: dict):
    """Executes full workflow loading, processing, and analysis"""
    df_vehicle = pd.read_csv(paths['vehicle_data'])
    df_demo = pd.read_csv(paths['demographic_data'])
    df_pollution = pd.read_csv(paths['pollution_data'])

    print("Data loaded")

    # Vehicle category analysis
    vehicle_shares = calculate_category_share(df_vehicle, 'Category', 'Sales')
    print("Vehicle category shares calculated")

    # Demographic segmentation
    demo_segmented = segment_by_age(df_demo, 'Age')
    print("Demographic data segmented")

    # Pollution correlation
    corr, p_value = pollution_ev_correlation(df_pollution, 'PM2.5', 'EV_Adoption_Rate')
    print(f"Pollution-EV adoption correlation: {corr:.3f}, p-value: {p_value:.4f}")

    return {
        'vehicle_shares': vehicle_shares,
        'demo_segmented': demo_segmented,
        'pollution_correlation': (corr, p_value)
    }
