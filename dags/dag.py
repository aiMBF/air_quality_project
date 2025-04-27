from airflow import DAG
from datetime import datetime, timedelta                    
from airflow.operators.python import PythonOperator
from airflow.operators.bash import BashOperator
import requests, os, duckdb, subprocess


def say_hello():
    print("Hello World !!")

def load_from_api():
    url = "https://api.waqi.info/feed/@5722/?token=8876300b97be85ed1baab3f7e85c83d0b1983a2c&city=Paris&offset=1&limit=10"

    result = subprocess.run(["curl", "-s", url], capture_output=True,  text=True, check=True)
    response_text = result.stdout
    data = json.loads(response_text)



default_args = {
    "owner": "air_quality_team",
    "retries": 1,
    "retry_delay": timedelta(minutes=5),
}

with DAG(
    dag_id="hello",
    description="Load air‑quality data from API, run dbt, then dbt tests",
    default_args=default_args,
    schedule_interval=timedelta(days=1),
    start_date=datetime(2024, 11, 1),
    catchup=False,
    tags=["air_quality", "dbt", "duckdb"],
) as dag:
    
    hello_task = PythonOperator(
        task_id="say_hello",
        python_callable=say_hello,
    )

    dbt_run = BashOperator(
        task_id="dbt_run",
        bash_command="cd /dbt && dbt run --no-write-json",
    )

    dbt_test = BashOperator(
        task_id="dbt_test",
        bash_command="cd /dbt && dbt test",
    )

    hello_task >> dbt_run >> dbt_test
