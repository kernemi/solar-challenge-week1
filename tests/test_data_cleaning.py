"""
test_data_cleaning.py
Basic unit tests for data_cleaning.py functions.
Author: Kernemi Kidane
"""

import pandas as pd
import numpy as np
from src.data_cleaning import drop_comments, handle_missing_values, remove_outliers

def test_drop_comments():
    df = pd.DataFrame({'A':[1,2], 'Comments':[np.nan, np.nan]})
    df_clean = drop_comments(df)
    assert 'Comments' not in df_clean.columns

def test_handle_missing_values():
    df = pd.DataFrame({'A':[1, np.nan, 3]})
    df_clean = handle_missing_values(df, ['A'])
    assert df_clean['A'].isna().sum() == 0
    assert df_clean['A'].iloc[1] == 2  # median

def test_remove_outliers():
    df = pd.DataFrame({'A':[1,2,1000,3]})
    df_clean = remove_outliers(df, ['A'], z_thresh=3)
    assert 1000 not in df_clean['A'].values
