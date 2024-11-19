from dotenv import load_dotenv
import os
from pyspark.sql import SparkSession
from data_load import load_csv_data, load_json_data


load_dotenv(dotenv_path=".secrets")

spark = SparkSession.builder \
    .appName("GCS Read CO2 data") \
    .config("spark.jars", "configs/gcs-connector-hadoop3-latest.jar") \
    .config("spark.hadoop.fs.gs.impl", "com.google.cloud.hadoop.fs.gcs.GoogleHadoopFileSystem") \
    .config("spark.hadoop.google.cloud.auth.service.account.enable", "true") \
    .config("spark.hadoop.google.cloud.auth.service.account.json.keyfile", os.getenv("GOOGLE_APPLICATION_CREDENTIALS")) \
    .getOrCreate()
    
    
annual_co2_per_country_df = load_csv_data(spark, "gs://co2-data-bucket/data/data/annual-co2-emissions-per-country.csv")
detailled_co2_per_country_df = load_json_data(spark, "gs://co2-data-bucket/data/data/owid-co2-data.json")
