import logging
import pandas as pd
from sqlalchemy import create_engine
from sqlalchemy.exc import SQLAlchemyError
from airflow.models import Variable
from database import engine


logging.basicConfig(
    format='%(asctime)s - %(levelname)s - %(message)s',
    level=logging.INFO
)


def load_data(file_path: str) -> pd.DataFrame:
    """Load data from a CSV file into a pandas DataFrame."""
    logging.info(f'Loading data from {file_path}')
    return pd.read_csv(file_path)


def insert_data_to_db(df: pd.DataFrame):
    """Insert data into the PostgreSQL database."""
    table_name = 'player_stats'

    try:
        logging.info('Connecting to the database')
        df.to_sql(table_name, con=engine, if_exists='append', index=False)
        logging.info('Data inserted into the database successfully')
    except SQLAlchemyError as e:
        logging.error(f'Error inserting data into database: {e}')
        raise


def main():
    # Load processed data into dataframe
    processed_file_path = '../data/processed/fb_ref_players_processed.csv'
    df = load_data(processed_file_path)
    insert_data_to_db(df)


if __name__ == '__main__':
    main()
