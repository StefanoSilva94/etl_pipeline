import pandas as pd
from airflow.models import Variable
import logging
import os
import json
from utils.utils import send_file_to_archive, get_first_file_name


# Set up logging configuration
logging.basicConfig(
    format='%(asctime)s - %(levelname)s - %(message)s',
    level=logging.INFO
)


def load_data(path):
    try:
        logging.info('Loading data into pandas DataFrame.')
        df = pd.read_csv(path)
        df['date'] = pd.to_datetime(df['date'], format='%Y-%m-%d')
        logging.info('Raw data loaded and date column parsed successfully.')
        return df
    except FileNotFoundError:
        logging.error(f'File not found: {path}')
        raise


def standardise_positions(df, mappings_dict):
    """
    The raw data has over 800 positions that a player can play. This is because it lists all positions they can play
    E.g. cb, lb, lwb, cdm
    This function will take only the main position (first listed) of the player
    It will then rename the positions to be a standardised list
    :param df: the dataframe to be updated
    :param mappings_dict: the mappings to convert values into
    :return: df with updated column values
    """

    try:
        # Remove redundant positions
        df['position'] = df['position'].str.split(',').str[0]
        df['position'] = df['position'].apply(lambda x: mappings_dict.get(x, x))
        logging.info('Standardizing position column complete.')
        return df
    except KeyError as e:
        logging.error(f'KeyError in position mappings: {e}')
        raise


def rename_cols(df, col_map):
    try:
        # Check if all columns in col_map exist in df
        missing_cols = [col for col in col_map.keys() if col not in df.columns]
        if missing_cols:
            raise ValueError(f"Columns {missing_cols} are not present in the DataFrame.")

        # Rename columns
        df.rename(columns=col_map, inplace=True)
        logging.info('Renamed columns according to the provided mapping.')

    except ValueError as ve:
        logging.error(f'ValueError occurred during column renaming: {ve}')
        raise
    except KeyError as ke:
        logging.error(f'KeyError occurred during column renaming: {ke}')
        raise
    logging.info('Renamed columns')

    return df


def clean_and_transform_data():
    current_path = os.getcwd()

    print(f'Current working directory: {current_path}')
    print(f'Current working directory: {current_path}')

    try:
        # construct the file path
        raw_folder_path = '../data/raw/'
        file_name = get_first_file_name(raw_folder_path)
        players_path = raw_folder_path + file_name

        # load the data into a dataframe
        players_df = load_data(players_path)

        # remove duplicate rows
        players_df = players_df.drop_duplicates()

        # load the position mappings from Airflow Variables
        position_mappings_json = Variable.get('position_mappings')
        position_mappings = json.loads(position_mappings_json)

        # standardise player positions and rename them
        players_df = standardise_positions(players_df, position_mappings)

        # Add new columns goal involvement and x_goal_involvement
        players_df["goal_involvements"] = players_df["goals"] + players_df["assists"]
        players_df["xg_involvements"] = players_df["xg"] + players_df["xg_assist"]

        # rename sca and gca to be more readable
        rename_col_mappings = {
            'sca': 'shot_creating_actions',
            'gca': 'goal_creating_actions',
        }
        # rename_col_mappings = Variable.get('rename_col_mappings')
        players_df = rename_cols(players_df, rename_col_mappings)

        num_rows_before = len(players_df)
        logging.info(f'Number of rows before dropping NA values: {num_rows_before}')

        players_df = players_df.dropna()

        num_rows_after = len(players_df)
        num_rows_dropped = num_rows_before - num_rows_after
        logging.info(f'Number of rows after dropping NA values: {num_rows_after}')
        logging.info(f'Number of rows dropped: {num_rows_dropped}')

        processed_folder_path = '../data/processed/'
        file_name = file_name.split('.csv')[0]
        transformed_df_path = processed_folder_path + file_name + '_processed.csv'

        # Store the transformed df to the processed folder
        players_df.to_csv(transformed_df_path)
        logging.info(f'Successfully stored the data in data/processed')

        # archive raw file after it's been processed
        archive_path = '../data/archive'
        send_file_to_archive(players_path, archive_path)

    except Exception as e:
        logging.error(f'An unexpected error occurred while processing the data: {e}')
        raise


if __name__ == '__main__':
    clean_and_transform_data()
