import pandas as pd
from src.pipeline import SolarAnalysisPipeline

def test_pipeline_cleaning(tmp_path):
    # Dummy CSV
    csv_file = tmp_path / "dummy.csv"
    csv_file.write_text(
        "Timestamp,GHI,DNI,DHI,ModA,ModB,WS,WSgust\n"
        "2025-01-01 00:00:00,100,50,25,10,12,1,2\n"
        "2025-01-01 01:00:00,110,55,30,11,13,2,3\n"
    )
    output_file = tmp_path / "clean.csv"
    numeric_cols = ['GHI', 'DNI', 'DHI', 'ModA', 'ModB', 'WS', 'WSgust']

    pipeline = SolarAnalysisPipeline(
        file_path=str(csv_file),
        numeric_cols=numeric_cols,
        clean_output_path=str(output_file)
    )
    pipeline.run_cleaning()

    # Assertions
    df_clean = pipeline.df_clean
    assert df_clean.shape[0] == 2
    assert all(col in df_clean.columns for col in numeric_cols)

def test_run_all_plots_raises_without_cleaning():
    numeric_cols = ['GHI', 'DNI', 'DHI']
    pipeline = SolarAnalysisPipeline(
        file_path="dummy.csv",
        numeric_cols=numeric_cols,
        clean_output_path="clean.csv"
    )

    import pytest
    with pytest.raises(ValueError):
        pipeline.run_all_plots()
