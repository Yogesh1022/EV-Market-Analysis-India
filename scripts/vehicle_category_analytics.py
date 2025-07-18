# vehicle_category_analytics.py
# Functions related to analysis of vehicle categories like 2W, 4W and commercial vehicles

import pandas as pd


def calculate_category_share(df: pd.DataFrame, category_col: str, sales_col: str) -> pd.DataFrame:
    """Calculates share of each vehicle category in total sales"""
    total_sales = df[sales_col].sum()
    df['category_share'] = df[sales_col] / total_sales
    return df


def segment_by_category(df: pd.DataFrame, category_col: str):
    """Divide DataFrame by vehicle category and return a dict"""
    categories = df[category_col].unique()
    return {cat: df[df[category_col] == cat] for cat in categories}
