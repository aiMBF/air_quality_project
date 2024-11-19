from dotenv import load_dotenv
import os
from pyspark.sql import SparkSession


load_dotenv(dotenv_path=".secrets")

spark = SparkSession.builder \
    .appName("GCS Read CO2 data") \
    .config("spark.jars", "configs/gcs-connector-hadoop3-latest.jar") \
    .config("spark.hadoop.fs.gs.impl", "com.google.cloud.hadoop.fs.gcs.GoogleHadoopFileSystem") \
    .config("spark.hadoop.google.cloud.auth.service.account.enable", "true") \
    .config("spark.hadoop.google.cloud.auth.service.account.json.keyfile", os.getenv("GOOGLE_APPLICATION_CREDENTIALS")) \
    .getOrCreate()
    
    
# I have to add data loading using the new loading methods