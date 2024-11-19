#Loading data to BigQuery

def write_to_bigquery(df, table_name):
    df.write.format("bigquery").option("table", table_name).save()