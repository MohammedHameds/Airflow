from airflow import DAG
from airflow.providers.postgres.operators.postgres import PostgresOperator
from datetime import datetime

default_args = {
    'start_date': datetime(2025, 7, 16),
    'catchup': False
}

with DAG(
    dag_id='student_workflow_dag',
    schedule_interval=None,
    default_args=default_args,
    description='Manage student data with PostgresOperator',
    tags=['postgres', 'students'],
) as dag:

    create_table = PostgresOperator(
        task_id='create_table',
        postgres_conn_id='my_postgres_conn',
        sql="""
            CREATE TABLE IF NOT EXISTS students (
                id SERIAL PRIMARY KEY,
                name VARCHAR(50),
                age INT,
                city VARCHAR(50)
            );
        """
    )

    insert_records = PostgresOperator(
        task_id='insert_records',
        postgres_conn_id='my_postgres_conn',
        sql="""
            INSERT INTO students (name, age, city) VALUES
            ('Mohamed Hamed', 25, 'Beni-Suef'),
            ('Sara', 22, 'Giza'),
            ('Youssef', 27, 'Alexandria'),
            ('Mariam', 29, 'Mansoura'),
            ('Tarek', 25, 'Tanta');
        """
    )

    delete_students = PostgresOperator(
        task_id='delete_students',
        postgres_conn_id='my_postgres_conn',
        sql="""
            DELETE FROM students WHERE age > 26;
        """
    )

    create_table >> insert_records >> delete_students
