from dotenv import load_dotenv
import os
from pyspark.sql import SparkSession


load_dotenv(dotenv_path=".secrets")

gcs_key_path = os.getenv("GOOGLE_APPLICATION_CREDENTIALS")

spark = SparkSession.builder \
    .appName("GCS Read Example") \
    .config("spark.jars", "../configs/gcs-connector-hadoop3-latest.jar") \
    .config("spark.hadoop.google.cloud.auth.service.account.enable", "true") \
    .config("spark.hadoop.google.cloud.auth.service.account.json.keyfile", gcs_key_path) \
    .getOrCreate()
