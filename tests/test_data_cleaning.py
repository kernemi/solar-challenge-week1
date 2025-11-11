import pandas as pd
from src.data_cleaning import load_and_prepare_data, data_quality_report

def test_load_and_prepare_data_creates_dataframe(tmp_path):
    # Create dummy CSV
    csv_file = tmp_path / "dummy.csv"
    csv_file.write_text(
        "Timestamp,GHI,DNI,DHI\n"
        "2025-01-01 00:00:00,100,50,25\n"
        "2025-01-01 01:00:00,110,55,30\n"
    )

    numeric_cols = ['GHI', 'DNI', 'DHI']
    df = load_and_prepare_data(str(csv_file), numeric_cols)

    # Assertions
    assert isinstance(df, pd.DataFrame)
    assert 'GHI' in df.columns
    assert df.index.name == 'Timestamp'
    assert df.shape[0] == 2  # two rows

def test_data_quality_report_output():
    df = pd.DataFrame({
        'GHI': [1, 2, None],
        'DNI': [1, 2, 3]
    })

    report = data_quality_report(df)
    assert 'missing_count' in report.columns
    assert report.loc['GHI', 'missing_count'] == 1
