import requests, os, duckdb, datetime
from dotenv import load_dotenv


 
load_dotenv(dotenv_path='.secrets')
TOKEN=os.getenv("TOKEN")


def load_from_api():
    conn = duckdb.connect("data/air_quality.duckdb")
    response = requests.get(f"https://api.waqi.info/feed/@5722/?token={TOKEN}&city=Paris")
    # if response.status_code == 200:
    #     print("Connecting to DuckDB...")
    #     data = response.json()
    #     # conn.execute("INSERT INTO raw_api_data (raw_json) VALUES (?)", (data,))
    #     # conn.close()
    # else:
    #     print(f"Failed to fetch data: {response.status_code}")