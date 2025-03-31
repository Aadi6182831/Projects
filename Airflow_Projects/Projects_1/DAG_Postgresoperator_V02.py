from datetime import datetime,timedelta
from airflow.providers.postgres.operators.postgres import PostgresOperator #type: ignore[import]
from airflow import DAG #type: ignore[import]

default_args = {
    'owner': 'Virat',
    'start_date': datetime(2025,3,29),
    'retries': 2,
    'retry_delay': timedelta(minutes=5),
}

with DAG(
      dag_id='PostgresOperator_DAG_02',
      default_args=default_args,
      description='Postgres Operator DAG',
      start_date=datetime(2025, 3, 29),
      catchup=False,
      schedule_interval='0 0 * * *'
) as dag:
    # Task to create a table in PostgreSQL
    task1 = PostgresOperator(
        task_id='create_postgres_table',
        postgres_conn_id='postgres_localhost',
        sql="""
            create table if not exists dag_runs (
                dt date,
                dag_id character varying,
                primary key (dt, dag_id)
            )
        """
    )

    task2 = PostgresOperator(
        task_id='insert_into_table',
        postgres_conn_id='postgres_localhost',
        sql="""
            insert into dag_runs (dt, dag_id) values ('{{ ds }}', '{{ dag.dag_id }}')
        """
    )

    task1 >> task2