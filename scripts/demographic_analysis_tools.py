# demographic_analysis_tools.py
# Functions for demographic and income analysis

import pandas as pd


def segment_by_age(df: pd.DataFrame, age_col: str):
    """Segments data by age groups"""
    bins = [0, 18, 30, 45, 60, 100]
    labels = ['Under 18', '18-29', '30-44', '45-59', '60+']
    df['age_group'] = pd.cut(df[age_col], bins=bins, labels=labels, right=False)
    return df


def average_income_by_group(df: pd.DataFrame, group_col: str, income_col: str):
    """Calculates average income by group"""
    return df.groupby(group_col)[income_col].mean().reset_index()
