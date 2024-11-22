# CO2 Emissions Data Processing Project

## Project Overview
This project is designed to process and analyze CO2 emissions data from various countries over time. The main goal is to ingest raw data stored in Google Cloud Storage (GCS), transform it using PySpark to add meaningful insights, and store the processed data in BigQuery for efficient querying and reporting.

The project uses Apache Airflow to orchestrate the data pipeline, enabling automation and scalability and Looker Studio for data visualization.

Technologies Used
`Google Cloud Platform (GCP)`:
- `GCS`: Storing raw and processed data files.
- `BigQuery`: Hosting the transformed data for analysis.
- `Apache Airflow`: Workflow orchestration for data ingestion, transformation, and loading.
- `PySpark`: Manipulating and transforming data.
- `CSV Format`: Input data format.