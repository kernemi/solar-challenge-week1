"""
eda_plots.py
Purpose: Provide reusable plotting functions for solar farm data.
Author: Kernemi Kidane
Date: Nov 9, 2025
"""

import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

# -------------------------------------------------------------------
# 1️⃣ Irradiance Over Time
# -------------------------------------------------------------------
def plot_irradiance_time_series(df, columns=['GHI', 'DNI', 'DHI']):
    """Plot solar irradiance (GHI, DNI, DHI) over time."""
    plt.figure(figsize=(14,5))
    for col in columns:
        plt.plot(df.index, df[col], label=col)
    plt.title("Solar Irradiance over Time")
    plt.xlabel("Timestamp")
    plt.ylabel("Irradiance (W/m²)")
    plt.legend()
    plt.show()

# -------------------------------------------------------------------
# 2️⃣ Daily & Monthly Averages
# -------------------------------------------------------------------
def plot_daily_monthly_mean(df, columns=['GHI', 'DNI', 'DHI']):
    """Plot daily and monthly average irradiance."""
    daily_mean = df.resample('D').mean()
    daily_mean[columns].plot(figsize=(14,5), title="Daily Average Irradiance")
    plt.show()

    monthly_mean = df.resample('ME').mean()
    monthly_mean[columns].plot(figsize=(14,5), title="Monthly Average Irradiance")
    plt.show()

# -------------------------------------------------------------------
# 3️⃣ Cleaning Impact
# -------------------------------------------------------------------
def plot_cleaning_impact(df, module_cols=['ModA','ModB']):
    """Compare module irradiance before and after cleaning."""
    df.groupby('Cleaning')[module_cols].mean().plot(kind='bar', figsize=(8,5))
    plt.title("Impact of Cleaning on Modules")
    plt.ylabel("Average Irradiance (W/m²)")
    plt.show()

# -------------------------------------------------------------------
# 4️⃣ Correlation Heatmap
# -------------------------------------------------------------------
def plot_correlation_heatmap(df, columns=['GHI','DNI','DHI','TModA','TModB','Tamb','RH']):
    """Plot correlation heatmap of key numeric variables."""
    plt.figure(figsize=(10,6))
    sns.heatmap(df[columns].corr(), annot=True, cmap='coolwarm')
    plt.title("Correlation Heatmap")
    plt.show()

# -------------------------------------------------------------------
# 5️⃣ Scatter Relationship Plots
# -------------------------------------------------------------------
def plot_scatter_wind_vs_ghi(df):
    """Plot Wind Speed vs GHI."""
    sns.scatterplot(x='WS', y='GHI', data=df)
    plt.title("Wind Speed vs GHI")
    plt.show()

def plot_scatter_rh_vs_temp(df):
    """Plot Relative Humidity vs Ambient Temperature."""
    sns.scatterplot(x='RH', y='Tamb', data=df)
    plt.title("Relative Humidity vs Ambient Temperature")
    plt.show()

def plot_temp_vs_modules(df):
    """Plot Module Temperature (A/B) vs Ambient Temperature."""
    sns.scatterplot(x='Tamb', y='TModA', data=df)
    sns.scatterplot(x='Tamb', y='TModB', data=df)
    plt.title("Module Temperature vs Ambient Temperature")
    plt.show()

def plot_rh_vs_ghi(df):
    """Plot Relative Humidity vs GHI."""
    sns.scatterplot(x='RH', y='GHI', data=df)
    plt.title("Relative Humidity vs GHI")
    plt.show()

# -------------------------------------------------------------------
# 6️⃣ Wind Analysis
# -------------------------------------------------------------------
def plot_wind_distribution(df):
    """Plot histogram of wind speeds."""
    df['WS'].hist(bins=30, figsize=(8,5))
    plt.title("Wind Speed Distribution")
    plt.xlabel("Wind Speed (m/s)")
    plt.ylabel("Frequency")
    plt.show()

def plot_wind_polar(df):
    """Plot wind direction and speed in polar coordinates."""
    plt.figure(figsize=(6,6))
    theta = np.deg2rad(df['WD'])
    r = df['WS']
    plt.subplot(111, polar=True)
    plt.scatter(theta, r, alpha=0.5)
    plt.title("Wind Direction & Speed")
    plt.show()

# -------------------------------------------------------------------
# 7️⃣ Bubble Chart
# -------------------------------------------------------------------
def plot_bubble(df):
    """Bubble chart: GHI vs Ambient Temperature (bubble size = RH)."""
    plt.figure(figsize=(10,6))
    plt.scatter(
        df['Tamb'], df['GHI'],
        s=df['RH'], alpha=0.5
    )
    plt.xlabel("Ambient Temperature (°C)")
    plt.ylabel("GHI (W/m²)")
    plt.title("GHI vs Ambient Temperature (bubble size = RH)")
    plt.show()
