import pandas as pd
import matplotlib.pyplot as plt
import streamlit as st

@st.cache_data
def load_csv(path):
    """Load CSV and parse Timestamp column."""
    return pd.read_csv(path, parse_dates=['Timestamp'])

def plot_ghi_boxplot(dfs):
    """Return a matplotlib figure of GHI boxplots for given dataframes."""
    fig, ax = plt.subplots(figsize=(8,4))
    data = [dfs[c]['GHI'].dropna() for c in dfs]
    ax.boxplot(data, labels=list(dfs.keys()))
    ax.set_ylabel("GHI (W/m^2)")
    return fig

def get_top_regions(dfs):
    """Aggregate mean and median GHI by country."""
    agg = []
    for c, df in dfs.items():
        agg.append({
            "country": c,
            "mean_GHI": df["GHI"].mean(),
            "median_GHI": df["GHI"].median()
        })
    return pd.DataFrame(agg).sort_values("mean_GHI", ascending=False)
