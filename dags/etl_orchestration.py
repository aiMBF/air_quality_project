from airflow import DAG
from datetime import datetime, timedelta                    
from airflow.operators.python import PythonOperator
from airflow.operators.bash import BashOperator
import requests, os, duckdb, subprocess, json
from dotenv import load_dotenv

load_dotenv(dotenv_path='.secrets')
TOKEN = os.getenv("TOKEN")

    
    
def load_from_api():
    url = f"https://api.waqi.info/feed/@5722/?token={TOKEN}&city=Paris&offset=1&limit=10"

    result = subprocess.run(["curl", "-s", url], capture_output=True,  text=True, check=True)
    response_text = result.stdout
    data = json.loads(response_text)
    print("Connecting to DuckDB...")
    conn = duckdb.connect("data/air_quality.duckdb")
    conn.execute("INSERT INTO raw_api_data (raw_json) VALUES (?)", (data,))
    conn.close()


default_args = {
    "owner": "air_quality_team",
    "retries": 1,
    "retry_delay": timedelta(minutes=5),
}

with DAG(
    dag_id="air_quality_dag",
    description="Load air‑quality data from API, run dbt, then dbt tests",
    default_args=default_args,
    schedule_interval=timedelta(days=1),
    start_date=datetime(2024, 11, 1),
    catchup=False,
    tags=["air_quality", "dbt", "duckdb"],
) as dag:
     
    ingest_task = PythonOperator(
        task_id="load_data_from_api",
        python_callable=load_from_api,
    )

    dbt_run = BashOperator(
        task_id="dbt_run",
        bash_command="cd /Users/baldita/Desktop/Projects/Personnel_Projects/energy_consumption/dbt && dbt run --no-write-json",
    )

    dbt_test = BashOperator(
        task_id="dbt_test",
        bash_command="cd /Users/baldita/Desktop/Projects/Personnel_Projects/energy_consumption/dbt && dbt test",
    )

    ingest_task >> dbt_run >> dbt_test
