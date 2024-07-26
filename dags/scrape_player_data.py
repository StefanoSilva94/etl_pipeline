from airflow.operators.python import PythonOperator
from airflow import DAG
from datetime import datetime, timedelta
from src.scrape_player_data import scrape_player_data


default_args = {
    'owner': 'airflow',
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
}


with DAG(
        dag_id='scrape_player_data',
        default_args=default_args,
        schedule_interval='0 8 * * 2',
        catchup=False,
        start_date=datetime(2024, 7, 20)
         ) as dag:

    scrape_player_data_task = PythonOperator(
        task_id='scrape_player_data_task',
        python_callable=scrape_player_data
    )

