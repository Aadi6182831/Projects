from airflow.decorators import dag, task # type: ignore
from datetime import datetime,timedelta


default_args={
    'owner':'Aadi',
    'retries': 4,
    'retry_delay': timedelta(minutes=2), 
}

@dag(
    dag_id='Dag_with_TaskflowAPI_V2',
    default_args=default_args,
    description='My Third DAG in Airflow and first one with taskflowAPI Operator',
    start_date=datetime(2025,3,27),
    schedule_interval='@daily'
    )

def hello_world_ETL():

    @task(multiple_outputs=True)
    def get_name():
        return {
            'first_name': 'Virat',
            'last_name': 'Kohli'
        }

    @task()
    def get_age():
        return 37

    @task()
    def greet(first_name, last_name, age):
        print(f"Hello World! My name is {first_name} {last_name} "
              f"and I am {age} years old!")
    
    name_dict = get_name()
    age = get_age()
    greet(first_name=name_dict['first_name'], 
          last_name=name_dict['last_name'],
          age=age)
    

greet=hello_world_ETL()