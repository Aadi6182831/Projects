from airflow import DAG # type: ignore
from datetime import datetime,timedelta
from airflow.operators.python import PythonOperator # type: ignore


default_args={
    'owner':'Aadi',
    'retries': 4,
    'retry_delay': timedelta(minutes=2), 
}

def getname():
    return 'Kohli'   

def greet(age,ti):
    name=ti.xcom_pull(task_ids='get_name')
    print(f"My name is {name},"
          f"and I am {age} years old")

with DAG(
    dag_id='DAG_PythonOperator_v03',
    default_args=default_args,
    description='My Second DAG in Airflow and first one with Python Operator',
    start_date=datetime(2025,3,22),
    schedule_interval='@daily'
    ) as dag:


   task1=PythonOperator(
       task_id='greet',
       python_callable=greet,
      op_kwargs={'age':29}
    )
    # task1
   task2=PythonOperator(
        task_id='get_name',
        python_callable=getname,
    )
   
   task2 >> task1

