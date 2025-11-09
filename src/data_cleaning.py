"""
data_cleaning.py
Purpose: Handle loading, cleaning, and preprocessing of solar datasets.
"""

import pandas as pd
import numpy as np
from scipy import stats

# 1 Load and Prepare Data
def load_and_prepare_data(file_path: str, numeric_cols: list[str], z_thresh: float = 3.0) -> pd.DataFrame:
    
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

# 2 Save Cleaned Data
def save_clean_data(df: pd.DataFrame, output_path: str) -> None:
    
    df.to_csv(output_path, index=False)
    print(f"✅ Clean data saved to: {output_path}")

# 3 Data Quality Summary
def data_quality_report(df: pd.DataFrame) -> pd.DataFrame:
    
    report = pd.DataFrame({
        "dtype": df.dtypes,
        "missing_count": df.isna().sum(),
        "missing_percent": (df.isna().mean() * 100).round(2)
    })
    print("📊 Data Quality Report:")
    print(report)
    return report
