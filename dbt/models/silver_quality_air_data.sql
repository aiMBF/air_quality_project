{{ config(
    materialized='incremental',
    unique_key='date'
) }}

SELECT 
  CAST(date AS DATE) AS date,
  pm25 AS pm25,
  pm10 AS pm10,
  o3 AS o3,
  no2 AS no2
FROM {{ ref('bronze_quality_air_data') }}

{% if is_incremental() %}
WHERE date > (SELECT MAX(date) FROM {{ this }})
{% endif %}
