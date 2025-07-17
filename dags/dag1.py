from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime

def say_hello():
    print("Hello, Mohamed! Your first DAG ran successfully.")

default_args = {
    'start_date': datetime(2024, 1, 1),
}

with DAG(
    dag_id='hello_world_dag',
    default_args=default_args,
    schedule_interval='@daily',
    catchup=False,
    tags=['example'],
) as dag:

    task1 = PythonOperator(
        task_id='say_hello_task',
        python_callable=say_hello,
    )
