from airflow import DAG
from airflow.providers.postgres.operators.postgres import PostgresOperator
from datetime import datetime

default_args = {
    'start_date': datetime(2024, 1, 1),
    'catchup': False
}

with DAG(
    dag_id='postgres_test_dag',
    schedule_interval=None,
    default_args=default_args,
    description='Run SQL in Postgres via Airflow',
    tags=['postgres']
) as dag:

    create_table = PostgresOperator(
        task_id='create_table',
        postgres_conn_id='my_postgres_conn',
        sql="""
            CREATE TABLE IF NOT EXISTS test_table (
                id SERIAL PRIMARY KEY,
                name VARCHAR(50),
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            );
        """
    )
