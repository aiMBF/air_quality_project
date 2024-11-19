def load_csv_data(spark, filename):
    return spark.read.format("csv").option("header", "true").load(filename)
    

def load_json_data(spark, filename):
    return spark.read.format("json").load(filename)
