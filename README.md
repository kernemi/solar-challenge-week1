# Program: TenX Academy – Solar Challenge (Week 0)
## Task1: Reproducing the Environment 
- steps: 
```
# 1. Clone the Repository
git clone https://github.com/<your-username>/solar-challenge-week1.git
cd solar-challenge-week1

# 2. Create and Activate Python Virtual Environment
# vscode
python -m venv venv
source venv/Scripts/activate

# 3. Install Required Packages
pip install --upgrade pip
pip install -r requirements.txt

# 4. Verify Setup
python --version
pip list
```
5. Notes: The data/ folder is ignored in Git. Place your local datasets in data/ (do not commit them).All notebooks and scripts are configured to use this environment.

## Task2: Data Profiling, Cleaning & EDA
-Clean and explore solar datasets for Benin, Sierra Leone, and Togo.
- Notebooks:
      - notebooks/benin_eda.ipynb
      - notebooks/sierra_leone_eda.ipynb
      - notebooks/togo_eda.ipynb
- Steps:
1. Loaded datasets, checked for null values and outliers(data profiling)
2. Cleaning:
   - Imputed missing numeric values using the median.
   - Detected outliers with Z-scores (|Z| > 3).
   - Exported cleaned versions to /data/<country>_clean.csv (ignored in Git).
3. Exploration (EDA):
   - Visualized irradiance trends (GHI, DNI, DHI).
   - Correlation heatmaps among temperature, humidity, and irradiance.
   - Cleaning impact plots for ModA and ModB.
   - Scatterplots: WS vs GHI, RH vs Tamb.
4. Key Observations:
   - it is listed is the report   
## Next Steps
  - Perform cross-country analysis in Task 3.
  - Create Streamlit dashboard for visualization.
