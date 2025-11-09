"""
data_cleaning.py
Purpose: Handle loading, cleaning, and preprocessing of solar datasets.
Author: Kernemi Kidane
Date: Nov 9, 2025
"""

import pandas as pd
import numpy as np
from scipy import stats

# -------------------------------------------------------------------
# 1️⃣ Load and Prepare Data
# -------------------------------------------------------------------
def load_and_prepare_data(file_path: str, numeric_cols: list[str], z_thresh: float = 3.0) -> pd.DataFrame:
    """
    Load, clean, and preprocess solar farm data.

    Args:
        file_path (str): Path to the raw CSV dataset.
        numeric_cols (list[str]): List of numeric columns to check for outliers.
        z_thresh (float): Z-score threshold for outlier removal. Default = 3.0.

    Returns:
        pd.DataFrame: Cleaned and processed DataFrame ready for EDA.
    """
    # Load dataset
    df = pd.read_csv(file_path)

    # Handle missing values — fill numeric columns with median
    for col in numeric_cols:
        if df[col].isna().sum() > 0:
            df[col] = df[col].fillna(df[col].median())

    # Compute Z-scores to detect outliers
    z_scores = np.abs(stats.zscore(df[numeric_cols]))
    df_clean = df[(z_scores < z_thresh).all(axis=1)].copy()

    # Convert timestamp and set as index
    if 'Timestamp' in df_clean.columns:
        df_clean['Timestamp'] = pd.to_datetime(df_clean['Timestamp'], errors='coerce')
        df_clean = df_clean.dropna(subset=['Timestamp'])
        df_clean.set_index('Timestamp', inplace=True)

    return df_clean

# -------------------------------------------------------------------
# 2️⃣ Save Cleaned Data
# -------------------------------------------------------------------
def save_clean_data(df: pd.DataFrame, output_path: str) -> None:
    """
    Save the cleaned DataFrame to a specified path.

    Args:
        df (pd.DataFrame): Cleaned dataset.
        output_path (str): Path to save the cleaned CSV.
    """
    df.to_csv(output_path, index=False)
    print(f"✅ Clean data saved to: {output_path}")

# -------------------------------------------------------------------
# 3️⃣ Data Quality Summary
# -------------------------------------------------------------------
def data_quality_report(df: pd.DataFrame) -> pd.DataFrame:
    """
    Generate a simple data quality report for missing values and data types.

    Args:
        df (pd.DataFrame): Input dataset.

    Returns:
        pd.DataFrame: Summary of missing values and data types.
    """
    report = pd.DataFrame({
        "dtype": df.dtypes,
        "missing_count": df.isna().sum(),
        "missing_percent": (df.isna().mean() * 100).round(2)
    })
    print("📊 Data Quality Report:")
    print(report)
    return report
