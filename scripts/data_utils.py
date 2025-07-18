# data_utils.py
# Utility functions for data loading, cleaning, and exporting in EV Market Analysis Project

import pandas as pd


def load_csv(filepath: str) -> pd.DataFrame:
    """Load a CSV file into DataFrame"""
    return pd.read_csv(filepath)


def clean_numeric_columns(df: pd.DataFrame, cols: list) -> pd.DataFrame:
    """Converts specified columns to numeric, coercing errors"""
    for col in cols:
        df[col] = pd.to_numeric(df[col], errors='coerce')
    return df


def export_df(df: pd.DataFrame, filepath: str):
    """Exports DataFrame to CSV"""
    df.to_csv(filepath, index=False)
