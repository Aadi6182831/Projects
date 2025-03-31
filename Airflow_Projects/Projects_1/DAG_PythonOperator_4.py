from airflow import DAG # type: ignore
from datetime import datetime,timedelta
from airflow.operators.python import PythonOperator # type: ignore


default_args={
    'owner':'Aadi',
    'retries': 4,
    'retry_delay': timedelta(minutes=2), 
}



def greet(ti):
    first_name=ti.xcom_pull(task_ids='get_name',key='first_name')
    last_name=ti.xcom_pull(task_ids='get_name',key='last_name')
    age=ti.xcom_pull(task_ids='get_age',key='age')
    print(f"My name is {first_name} {last_name},"
          f"and I am {age} years old as of today Mar 23,2025")


def getname(ti):
    ti.xcom_push(key='first_name',value='Virat')
    ti.xcom_push(key='last_name',value='Kohli')

def getage(ti):	
	ti.xcom_push(key='age',value=37)


with DAG(
    dag_id='DAG_PythonOperator_v04',
    default_args=default_args,
    description='My Second DAG in Airflow and first one with Python Operator',
    start_date=datetime(2025,3,22),
    schedule_interval='@daily'
    ) as dag:


   task1=PythonOperator(
       task_id='get_age',
       python_callable=getage,
        )
    # task1
   task2=PythonOperator(
        task_id='get_name',
        python_callable=getname,
    )
   task3=PythonOperator(
     task_id='greet',
     python_callable=greet
    )
   
   [task1,task2] >> task3

