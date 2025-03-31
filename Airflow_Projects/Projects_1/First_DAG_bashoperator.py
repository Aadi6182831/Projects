from airflow import DAG # type: ignore
from datetime import datetime,timedelta
from airflow.operators.bash_operator import BashOperator # type: ignore


default_args = {
    'owner':'Aadi',
   # 'depends_on_past': False,
    'email': ['ramineni1828@gmail.com','adivenkat31@gmail.com'],
   # 'start_date':datetime(2025,3,22),
   # 'email_on_failure': False,
   # 'email_on_retry': False,
    'retries': 4,
    'retry_delay': timedelta(minutes=2),
}

with DAG(
    dag_id='First_DAG_V5',
    default_args=default_args,
    description='My First DAG in Airflow',
    schedule_interval='@daily',
    start_date=datetime(2025,3,22,16,25)
    ) as dag:

    task1=BashOperator(
    task_id='My_first_task',
    bash_command='echo hello world, this is my first task in DAGS'
)
    
    task2=BashOperator(
    task_id="My_Second_Task",
    bash_command='echo hello world, this is my second task in DAGS and should run after task1 only'
)
    
    task3=BashOperator(
    task_id="My_Third_Task",
    bash_command='echo hello world, this is my third task in DAGS and should run after task1 and at the same time of task2'
)
    # Task Dependency method 1
    # task1.set_downstream(task2)
    # task1.set_downstream(task3)

    # Task Dependency method 2
    # task1 >> task2
    # task1 >> task3

    # Task Dependency method 3
    task1 >> [task2,task3]