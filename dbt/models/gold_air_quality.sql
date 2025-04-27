SELECT 
  date,
  AVG(pm25) AS avg_pm25,
  AVG(pm10) AS avg_pm10,
  AVG(o3)   AS avg_o3,
  AVG(no2)  AS avg_no2
FROM {{ ref('silver_quality_air_data') }}
GROUP BY date
