from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime

def first_function(**kwargs):
    x = 3
    kwargs['ti'].xcom_push(key='number', value=x)

def calculation_function(**kwargs):
    my_number = kwargs['ti'].xcom_pull(key='number', task_ids='get_the_number')
    result = (my_number * my_number) + 1
    print(f"The final result is {result}")

with DAG(
    dag_id='Lab3_Task4',
    start_date=datetime(2025, 1, 1),
    schedule_interval='@daily',
    catchup=False
) as dag:

    task1 = PythonOperator(
        task_id='get_the_number',
        python_callable=first_function,
    )
    
    task2 = PythonOperator(
        task_id='calculation',
        python_callable=calculation_function,
    )
    
    task1 >> task2
