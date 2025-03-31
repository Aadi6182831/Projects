from datetime import datetime,timedelta
from airflow.providers.postgres.operators.postgres import PostgresOperator #type: ignore[import]
from airflow import DAG #type: ignore[import]

default_args = {
    'owner': 'Virat',
    'start_date': datetime(2025,3, 29),
    'retries': 2,
    'retry_delay': timedelta(minutes=5),
}

with DAG(
      dag_id='PostgresOperator_DAG',
      default_args=default_args,
      description='Postgres Operator DAG',
      start_date=datetime(2025, 3, 29),
      catchup=False,
      schedule_interval='0 0 * * *'
) as dag:
    task1 = PostgresOperator(
        task_id='create_table',
        postgres_conn_id='postgres_localhost',
        sql="""
            create table if not exists dag_runs (
                dt date,
                dag_id character varying,
                primary key (dt, dag_id)
            )
        """
    )
    task1