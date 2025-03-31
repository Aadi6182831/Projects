from airflow import DAG # type: ignore
from datetime import datetime,timedelta
from airflow.operators.python import PythonOperator # type: ignore


default_args={
    'owner':'Aadi',
    'retries': 4,
    'retry_delay': timedelta(minutes=2), 
}

def get_name():
    return 'kohli'


with DAG(
    dag_id='DAG_PythonOperator_v02',
    default_args=default_args,
    description='My Second DAG in Airflow and first one with Python Operator',
    start_date=datetime(2025,3,22),
    schedule_interval='@daily'
    ) as dag:


   # task1=PythonOperator(
    #    task_id='My_first_python_task',
     #   python_callable=greet,
      #  op_kwargs={'name':'Gautham','age':29}
    #)
    
    # task1
    task2=PythonOperator(
        task_id='getname',
        python_callable=get_name,
    )

