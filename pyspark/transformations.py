from pyspark.sql.window import Window
from pyspark.sql import functions as F


def calculate_co2_per_capita(df):
    return df.withColumn("co2_per_capita", df["Annual CO₂ emissions"] / df["population"])


def calculate_cumulative_co2(df):
    window_spec = Window.partitionBy("iso_code").orderBy("Year")
    return df.withColumn("cumulative_co2_emissions", F.sum("Annual CO₂ emissions").over(window_spec))


def calculate_shared_global_co2_emissions(df):
    pass


def calculate_land_use_change_co2_emissions(df):
    pass


def calculate_per_capita_cumulative_co2_emissions(df):
    pass