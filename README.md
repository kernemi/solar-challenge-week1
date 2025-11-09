# TenX Academy – Solar Challenge (Week 0)
## Task1: Reproducing the Environment 
Goal: Set up a reproducible Python environment for solar data analysis.
Steps:
```
# 1. Clone the Repository
git clone https://github.com/<your-username>/solar-challenge-week1.git
cd solar-challenge-week1

# 2. Create and Activate Python Virtual Environment
python -m venv venv
# VS Code or Windows
venv\Scripts\activate
# macOS/Linux
source venv/bin/activate

# 3. Install Required Packages
pip install --upgrade pip
pip install -r requirements.txt

# 4. Verify Setup
python --version
pip list
```
5. Notes:
- The data/ folder is ignored in Git.
- Place your local datasets in data/ (do not commit them).
- All notebooks and scripts are configured to use this environment.

## Task2: Data Profiling, Cleaning & EDA
Goal: Clean and explore solar datasets for Benin, Sierra Leone, and Togo.- Notebooks:
      - notebooks/benin_eda.ipynb
      - notebooks/sierra_leone_eda.ipynb
      - notebooks/togo_eda.ipynb
- Steps Performed

1. Data Profiling
      -Checked for null values, duplicates, and data types.
      -Reviewed distributions of key numeric features.

2. Cleaning
      -Filled missing numeric values using median imputation.
      -Detected and removed outliers using Z-score filtering (|Z| > 3).
      -Exported cleaned datasets to /data/*_clean.csv (ignored in Git).

3. Exploratory Data Analysis (EDA)
      -Plotted irradiance trends: GHI, DNI, DHI.
      -Correlation heatmaps between temperature, humidity, and irradiance.
      -Cleaning impact plots for ModA and ModB.
      -Scatterplots:
            -Wind Speed (WS) vs GHI
            -Relative Humidity (RH) vs Ambient Temperature (Tamb)
            -Tamb vs Module Temperatures (TModA, TModB)
4. Key Observations:
   - Sierra Leone: Higher GHI but lower wind speed frequency.
   - Togo: Module B temperatures dominate; blue (site) points are less visible.
   - Benin: Balanced irradiance distribution; steady wind pattern.
     
## Next Steps
  - Perform cross-country comparison and deeper correlation analysis (Task 3).
  - Develop a Streamlit dashboard for interactive visualization and presentation.
