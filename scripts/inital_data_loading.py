import duckdb as db 

DB_PATH = "data/air_quality.duckdb"
DATA_FILE = 'data/paris-air-quality.csv'


conn = db.connect(DB_PATH)
#  Create raw table data to store data from WAQI API. Data are transformed before moved to silver table
conn.execute("CREATE SCHEMA IF NOT EXISTS raw;")

conn.execute("""
    CREATE TABLE IF NOT EXISTS raw.raw_api_data (
        ingestion_time TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
        raw_json TEXT);""")


# Create and load the silver table that will contain historical transformed data from
conn.execute(
    """
    CREATE TABLE IF NOT EXISTS quality_air_data (
        date DATE PRIMARY KEY,
        pm25 FLOAT,
        pm10 FLOAT,
        o3 FLOAT,
        no2 FLOAT)""")

existing_rows = conn.execute("SELECT COUNT(*) FROM quality_air_data").fetchone()[0]
if existing_rows==0:
    print("Chargement des donnees ")
    conn.execute(f"""
    INSERT INTO quality_air_data(date, pm25, pm10, o3, no2)
    SELECT CAST(date AS DATE),
    CASE WHEN TRIM(pm25) IN ('', 'N/A', 'NA', 'null') THEN NULL ELSE CAST(TRIM(pm25) AS FLOAT) END,
    CASE WHEN TRIM(pm10) IN ('', 'N/A', 'NA', 'null') THEN NULL ELSE CAST(TRIM(pm10) AS FLOAT) END,
    CASE WHEN TRIM(o3)   IN ('', 'N/A', 'NA', 'null') THEN NULL ELSE CAST(TRIM(o3) AS FLOAT) END,
    CASE WHEN TRIM(no2)  IN ('', 'N/A', 'NA', 'null') THEN NULL ELSE CAST(TRIM(no2) AS FLOAT) END
    FROM read_csv_auto('{DATA_FILE}')
    """)
    conn.close()
else:
    print("Donnees deja existantes")