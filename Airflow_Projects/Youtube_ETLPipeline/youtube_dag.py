from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime, timedelta
from youtube_etl import run_youtube_etl

# Default arguments for the DAG
default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'start_date': datetime(2024, 4, 1),
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
}

# Define DAG
dag = DAG(
    'youtube_etl_dag',
    default_args=default_args,
    description='YouTube ETL with Airflow',
    schedule_interval='@daily',  # Runs dailyPp
)

# Define task
run_etl_task = PythonOperator(
    task_id='run_youtube_etl',
    python_callable=run_youtube_etl,
    dag=dag,
)

run_etl_task
