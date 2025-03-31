from airflow.decorators import dag, task # type: ignore
from datetime import datetime,timedelta


default_args={
    'owner':'Aadi',
    'retries': 4,
    'retry_delay': timedelta(minutes=2), 
}

@dag(
    dag_id='Dag_with_TaskflowAPI',
    default_args=default_args,
    description='My Third DAG in Airflow and first one with taskflowAPI Operator',
    start_date=datetime(2025,3,27),
    schedule_interval='@daily'
    )


def hello_world_ETL():

    @task()
    def getname():
        return 'Kohli'

    @task()
    def getage():
        return 29  

    @task()
    def greet(name:str,age:int):
        print(f"My name is {name},"
              f"and I am {age} years old")

    name=getname()
    age=getage()
    greet(name,age)


greet=hello_world_ETL()