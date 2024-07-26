import pandas as pd
# from airflow import Variable
import logging

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
        logging.info('Data loaded and date column parsed successfully.')
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
    logging.info('Renamed columns')
    return df.rename(columns=col_map, inplace=True)


def clean_and_transform_data():
    try:
        players_path = f'../data/fb_ref_players_2023_2024.csv'
        players_df = load_data(players_path)

        # remove duplicate rows
        players_df = players_df.drop_duplicates()

        # standardise player positions and rename them
        position_mappings = Variable.get('position_mappings')
        players_df = standardise_positions(players_df, position_mappings)

        # Add new columns goal involvement and x_goal_involvement
        players_df["goal_involvements"] = players_df["goals"] + players_df["assists"]
        players_df["xg_involvements"] = players_df["xg"] + players_df["xg_assist"]

        num_rows_before = len(players_df)
        logging.info(f'Number of rows before dropping NA values: {num_rows_before}')

        players_df = players_df.dropna()

        num_rows_after = len(players_df)
        num_rows_dropped = players_df - num_rows_after
        logging.info(f'Number of rows after dropping NA values: {num_rows_after}')
        logging.info(f'Number of rows dropped: {num_rows_dropped}')

        transformed_df_path = '../data/processed/fb_ref_players_processed.csv'

        # Store the transformed df to the processed folder
        players_df.to_csv(transformed_df_path)
        logging.info(f'Successfully stored the data in data/processed')

    except Exception as e:
        logging.error(f'An unexpected error occurred while renaming columns: {e}')
        raise


if __name__ == '__main__':
    clean_and_transform_data()
