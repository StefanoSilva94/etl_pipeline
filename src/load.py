import logging
import pandas as pd
from sqlalchemy.exc import SQLAlchemyError
from models import PlayerStatsDB
from database import engine
from sqlalchemy.orm import Session


logging.basicConfig(
    format='%(asctime)s - %(levelname)s - %(message)s',
    level=logging.INFO
)


def load_data(file_path: str) -> pd.DataFrame:
    logging.info(f'Loading data from {file_path}')
    return pd.read_csv(file_path)


def insert_data_to_db(df: pd.DataFrame):
    # table_name = 'player_stats'
    try:
        with Session(engine, future=True) as session:
            for _, row in df.iterrows():
                # Convert row to a dictionary and insert into the database
                player_stats_data = row.to_dict()
                new_player_stats = PlayerStatsDB(**player_stats_data)
                session.add(new_player_stats)
            session.commit()
            print("DataFrame loaded into database successfully.")
    except SQLAlchemyError as e:
        print(f"SQLAlchemy error occurred: {e}")
    except Exception as e:
        print(f"An error occurred: {e}")


def load_data_to_tables():
    # Load processed data into dataframe
    processed_file_path = '../data/processed/fb_ref_players_processed.csv'
    df = load_data(processed_file_path)

    # Remove index column if it is present to match model definition
    if 'Unnamed: 0' in df.columns:
        df = df.drop(columns=['Unnamed: 0'])
    insert_data_to_db(df)


if __name__ == '__main__':
    print('starting loading')
    load_data_to_tables()



