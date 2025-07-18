# pollution_correlation_calculator.py
# Functions to calculate correlations between pollution and EV adoption

import pandas as pd
from scipy.stats import pearsonr


def pollution_ev_correlation(df: pd.DataFrame, pollution_col: str, ev_adoption_col: str):
    """Calculates Pearson correlation coefficient"""
    corr, p_value = pearsonr(df[pollution_col], df[ev_adoption_col])
    return corr, p_value
