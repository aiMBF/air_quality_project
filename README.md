# Air Quality Data Pipeline — Airflow, DBT & DuckDB

## Overview

This project implements a full end-to-end data pipeline to collect, transform, and orchestrate air quality data for Paris. Using DBT’s bronze-silver-gold layer architecture and **incremental models** for data transformation, DuckDB for efficient local storage, and Apache Airflow for orchestration, the pipeline ensures reliable ingestion, optimized transformations, and continuous updates of air quality datasets.

## Tech Stack

- **Apache Airflow** — Workflow orchestration
- **DBT (Data Build Tool)** — Data modeling with incremental loading
- **DuckDB** — Lightweight embedded analytical database
- **Python** — ETL scripting
- **WaQI API** — Data source for real-time air quality information

## Project Structure

```
.
├── dags/
│   └── etl_orchestration.py           # Airflow DAG to orchestrate the ETL pipeline
├── data/
│   ├── air_quality.duckdb             # DuckDB database file
│   └── paris-air-quality.csv          # Raw backup data
├── dbt/
│   ├── dbt_project.yml                 # DBT project config
│   ├── models/
│   │   ├── bronze_quality_air_data.sql # Bronze layer: raw ingestion (incremental model)
│   │   ├── silver_quality_air_data.sql # Silver layer: cleaned data (incremental model)
│   │   ├── gold_air_quality.sql        # Gold layer: analytics-ready data (incremental model)
│   │   └── sources/                    # DBT sources
│   ├── profiles.yml                    # DBT connection profiles
│   └── target/                         # Compiled DBT artifacts
├── scripts/
│   ├── __init__.py
│   └── initial_data_loading.py         # Script for initial data ingestion
├── logs/                               # Airflow logs
├── airflow.cfg                         # Airflow configuration
├── airflow.db                          # Airflow metadata database
└── README.md                           # Project documentation
```

## How It Works

1. **Data Ingestion**:  
   A Python script (`initial_data_loading.py`) fetches the latest air quality data from the WaQI API and stores it into DuckDB.

2. **DBT Transformations (Incremental Models)**:  
   Data flows through **bronze**, **silver**, and **gold** layers in DBT, using **incremental models** to only process new or changed records:
   - **Bronze**: Raw ingestion of air quality measurements.
   - **Silver**: Data cleaning, filtering, and enrichment.
   - **Gold**: Aggregated, analytics-ready datasets for visualization and reporting.

3. **Workflow Orchestration**:  
   Airflow DAG (`etl_orchestration.py`) automates the entire process, from ingestion to incremental DBT transformations, scheduled to run daily.

4. **Storage**:  
   DuckDB is used for fast local analytical queries with minimal overhead.

## Installation & Setup

1. Clone the repository:

```bash
git clone https://github.com/aiMBF/co2-emissions-project.git
cd co2-emissions-project
```

2. Install dependencies:

```bash
pip install apache-airflow dbt-duckdb duckdb
```

3. Initialize Airflow:

```bash
airflow db init
```

4. Launch Airflow components:

```bash
airflow webserver --port 8080
airflow scheduler
```

5. Open Airflow UI at `http://localhost:8080` and trigger the `air_quality_dag`.

6. Run DBT transformations manually if needed:

```bash
cd dbt
dbt run
```
