from airflow.operators.python import PythonOperator
from airflow import DAG
from datetime import datetime, timedelta

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

    clean_data_task = PythonOperator(
        task_id='scrape_player_data_task',
        python_callable=clean_player_data
    )

    load_player_data_task = PythonOperator(
        task_id='load_player_data_task',
        python_callable=load_player_data
    )


clean_data_task >> clean_data_task

