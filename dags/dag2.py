from airflow import DAG
from airflow.operators.bash import BashOperator
from datetime import datetime

with DAG(
    'Airflow-lab1',
    schedule_interval="@daily",
    catchup=False,
    start_date=datetime(2025, 7, 13)) as dag:

    task1 = BashOperator(
        task_id='task1',
        bash_command='echo "Hello Task1"'
    )

    task2 = BashOperator(
        task_id='task2',
        bash_command='echo "Hello Task2"'
    )

    task3 = BashOperator(
        task_id='task3',
        bash_command='echo "Hello Task3"'
    )

    task1 >> [task2, task3]
