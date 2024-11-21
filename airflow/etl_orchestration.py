from datetime import datetime, timedelta
from airflow import DAG
import os


default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
}

with DAG(
    dag_id='gcs_to_bigquery',
    default_args=default_args,
    description='A simple DAG to load GCS data, transform data and load into BigQuery',
    schedule_interval=timedelta(days=1),
    start_date=datetime(2023, 11, 1),
    catchup=False,
    tags=['gcs', 'bigquery', 'pyspark'],
) as dag:
    
    #TODO: ADD tasks later
    pass