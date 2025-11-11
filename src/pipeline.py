from src.data_cleaning import load_and_prepare_data, save_clean_data, data_quality_report
from src.eda_plots import (
    plot_irradiance_time_series, plot_daily_monthly_mean,
    plot_cleaning_impact, plot_correlation_heatmap,
    plot_scatter_wind_vs_ghi, plot_scatter_rh_vs_temp,
    plot_temp_vs_modules, plot_rh_vs_ghi,
    plot_wind_distribution, plot_wind_polar,
    plot_bubble
)

class SolarAnalysisPipeline:
    """
    Modular pipeline to run Tasks 1 & 2:
    - Load and clean data
    - Generate data quality report
    - Save cleaned CSV
    - Run all EDA plots
    """

    def __init__(self, file_path, numeric_cols, clean_output_path):
        self.file_path = file_path
        self.numeric_cols = numeric_cols
        self.clean_output_path = clean_output_path
        self.df_clean = None

    def run_cleaning(self):
        self.df_clean = load_and_prepare_data(self.file_path, self.numeric_cols)
        data_quality_report(self.df_clean)
        save_clean_data(self.df_clean, self.clean_output_path)

    def run_all_plots(self):
        if self.df_clean is None:
            raise ValueError("Data not cleaned. Run run_cleaning() first.")
        plot_irradiance_time_series(self.df_clean)
        plot_daily_monthly_mean(self.df_clean)
        plot_cleaning_impact(self.df_clean)
        plot_correlation_heatmap(self.df_clean)
        plot_scatter_wind_vs_ghi(self.df_clean)
        plot_scatter_rh_vs_temp(self.df_clean)
        plot_temp_vs_modules(self.df_clean)
        plot_rh_vs_ghi(self.df_clean)
        plot_wind_distribution(self.df_clean)
        plot_wind_polar(self.df_clean)
        plot_bubble(self.df_clean)
