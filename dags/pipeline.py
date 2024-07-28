from airflow.operators.python import PythonOperator
from airflow import DAG
from datetime import datetime, timedelta
from src.clean_and_transform import clean_and_transform_data
from src.load import load_data_to_tables

default_args = {
    'owner': 'airflow',
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
}

with DAG(
        dag_id='pipeline',
        default_args=default_args,
        schedule_interval='0 8 * * 2',
        catchup=False,
        start_date=datetime(2024, 7, 20)
) as dag:

    clean_data_task = PythonOperator(
        task_id='clean_data_task',
        python_callable=clean_and_transform_data
    )

    load_player_data_task = PythonOperator(
        task_id='load_player_data_task',
        python_callable=load_data_to_tables
    )

    clean_data_task >> load_player_data_task
