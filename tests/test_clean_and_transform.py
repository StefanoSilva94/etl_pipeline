import pandas as pd
from unittest.mock import patch
from src.clean_and_transform import *


sample_data = {
    'player': ['Player1', 'Player2'],
    'position': ['cb, lb', 'lw'],
    'goals': [10, 5],
    'assists': [2, 1],
    'gca': [12.5, 6.3],
    'sca': [3.2, 2.1]
}

# define sample data and mappings to be tested
sample_df = pd.DataFrame(sample_data)
position_mappings = {'cb': 'def', 'lw': 'att'}
rename_col_mappings = {'sca': 'shot_creating_actions', 'gca': 'goal_creating_actions'}


def test_load_data():
    with patch('pandas.read_csv') as mock_read_csv:
        mock_read_csv.return_value = sample_df
        df = load_data('../data/raw/fb_ref_players_2023_2024_38.csv')
        assert df.equals(sample_df)


def test_standardise_positions():
    result_df = standardise_positions(sample_df, position_mappings)
    expected_positions = ['def', 'att']
    assert result_df['position'].tolist() == expected_positions


def test_rename_cols():
    result_df = rename_cols(sample_df, rename_col_mappings)
    assert 'goal_creating_actions' in result_df.columns
    assert 'shot_creating_actions' in result_df.columns


