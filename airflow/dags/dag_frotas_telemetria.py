# ficheiro: airflow/dags/dag_frotas_telemetria.py
from datetime import datetime, timedelta
from airflow import DAG
from airflow.operators.bash import BashOperator

default_args = {
    'owner': 'Gabriel_Master',
    'depends_on_past': False,
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
}

with DAG(
    'processamento_telemetria_frotas',
    default_args=default_args,
    description='Automatiza a limpeza de dados e testes de qualidade do dbt',
    schedule_interval=timedelta(days=1),
    start_date=datetime(2024, 1, 1),
    catchup=False,
    tags=['telemetria', 'dbt', 'qualidade'],
) as dag:

    # O dbt lê os modelos da pasta principal, mas escreve os logs na pasta livre /tmp/ do Linux
    t1 = BashOperator(
        task_id='dbt_run_transformacao',
        bash_command='cd /usr/app/dbt/frotas_dw && dbt run --profiles-dir . --target-path /tmp/target --log-path /tmp/logs',
    )

    t2 = BashOperator(
        task_id='dbt_test_qualidade',
        bash_command='cd /usr/app/dbt/frotas_dw && dbt test --profiles-dir . --target-path /tmp/target --log-path /tmp/logs',
    )

    t1 >> t2