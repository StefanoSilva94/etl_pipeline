import logging
import pandas as pd
from sqlalchemy.exc import SQLAlchemyError
from models import PlayerStatsDB
from database import engine
from sqlalchemy.orm import Session
from utils.utils import get_first_file_name, send_file_to_archive
import os

logging.basicConfig(
    format='%(asctime)s - %(levelname)s - %(message)s',
    level=logging.INFO
)


def load_data(file_path: str) -> pd.DataFrame:
    try:
        logging.info('Loading data into pandas DataFrame.')
        logging.info(f'Loading data from {file_path}')
        logging.info('Processed data loaded and parsed successfully.')
        return pd.read_csv(file_path)
    except FileNotFoundError:
        logging.error(f'File not found: {file_path}')
        raise


def insert_data_to_db(df: pd.DataFrame):
    logging.info(f'Starting to load data to players_data table')

    try:
        with Session(engine, future=True) as session:
            for _, row in df.iterrows():
                # Convert row to a dictionary and insert into the database
                player_stats_data = row.to_dict()
                new_player_stats = PlayerStatsDB(**player_stats_data)
                session.add(new_player_stats)
            session.commit()
            logging.info("DataFrame loaded into database successfully.")
    except SQLAlchemyError as e:
        print(f"SQLAlchemy error occurred: {e}")
    except Exception as e:
        print(f"An error occurred: {e}")


def load_data_to_tables():
    # Load processed data into dataframe
    print(f"PYTHONPATH is: {os.environ.get('PYTHONPATH')}")
    current_working_directory = os.getcwd()
    print(f"Current working directory is: {current_working_directory}")
    logging.info('Starting the process to load data into tables')
    try:
        # construct the file path
        processed_folder_path = '../data/processed/'
        file_name = get_first_file_name(processed_folder_path)
        processed_file_path = processed_folder_path + file_name

        df = load_data(processed_file_path)

        # Remove index column if it is present to match model definition
        if 'Unnamed: 0' in df.columns:
            df = df.drop(columns=['Unnamed: 0'])
        insert_data_to_db(df)

        # move processed folder to archive after processing
        archive_path = '../data/archive'
        send_file_to_archive(processed_file_path, archive_path)
    except Exception as e:
        logging.error(f'Failed to load data to tables: {e}')


if __name__ == '__main__':
    print('starting loading')
    load_data_to_tables()



