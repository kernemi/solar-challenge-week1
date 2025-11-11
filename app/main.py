import streamlit as st
from utils import load_csv, plot_ghi_boxplot, get_top_regions

st.set_page_config(layout="wide", page_title="Solar Data Discovery")

st.title("Solar Data Discovery — MoonLight Energy Solutions")
st.markdown("Compare GHI, DNI, DHI across Benin, Sierra Leone, and Togo")

# Local CSV paths
country_files = {
    "Benin": "data/benin_clean.csv",
    "Sierra Leone": "data/sierra_clean.csv",
    "Togo": "data/togo_clean.csv",
}

# Widget: select countries
selected = st.multiselect("Select countries", list(country_files.keys()), default=list(country_files.keys()))
if not selected:
    st.warning("Select at least one country to view data")
    st.stop()

# Load data
dfs = {}
for country in selected:
    try:
        dfs[country] = load_csv(country_files[country])
    except FileNotFoundError:
        st.error(f"Missing CSV for {country}. Put cleaned CSV at {country_files[country]}")
        st.stop()

# GHI boxplot
st.header("GHI Boxplots by Country")
fig = plot_ghi_boxplot(dfs)
st.pyplot(fig)

# Top regions table
st.header("Top regions by average GHI")
agg_df = get_top_regions(dfs)
agg_df.index = range(1, len(agg_df) + 1)
st.dataframe(agg_df)

st.info("This app reads local cleaned CSVs. Keep `data/` out of the repo. For deployment, stage CSVs in secure storage or load dynamically.")
