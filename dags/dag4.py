from datetime import datetime, timedelta
from airflow import DAG
from airflow.operators.python import PythonOperator

def fun1(name, city):
    print(f"Hello king {name}, from {city}")

def fun2(message):
    print(f"Second task says: {message}")

with DAG(
    dag_id='Airflow-lab3',
    description='This is our first DAG that we write',
    start_date=datetime(2023, 10, 29, 2),
    schedule_interval='@daily'
) as dag:

    task1 = PythonOperator(
        task_id='first_task',
        python_callable=fun1,
        op_args=['Mohamed', 'Beni-Suef'] 
    )

    task2 = PythonOperator(
        task_id='second_task',
        python_callable=fun2,
        op_kwargs={'message': 'This is a parameterized function!'}
    )

    task1 >> task2
