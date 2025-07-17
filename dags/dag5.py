from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime

def Stud_grade(name, score):
    print(f"Student: {name}")
    print(f"Scores: {score}")
    avg = sum(score) / len(score)
    if avg > 50:
        print("Pass")
        print(f"Avg: {avg}")
    else:
        print("Failed")

with DAG(
    dag_id="Lab3-Task3",
    start_date=datetime(2025, 7, 16),
    catchup=False,
) as dag:

    task1 = PythonOperator(
        task_id="Grade",
        python_callable=Stud_grade,
        op_kwargs={'name': 'Mohamed Hamed', 'score': [80, 75, 90]}
    )
