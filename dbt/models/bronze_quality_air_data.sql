{{ config(
    materialized='incremental',
    unique_key='date'
) }}

WITH parsed AS (
  SELECT
    JSON_EXTRACT_STRING(raw_json, '$.data.time.iso') AS date,
    CAST(JSON_EXTRACT(raw_json, '$.data.iaqi.pm25.v') AS DOUBLE) AS pm25,
    CAST(JSON_EXTRACT(raw_json, '$.data.iaqi.pm10.v') AS DOUBLE) AS pm10,
    CAST(JSON_EXTRACT(raw_json, '$.data.iaqi.o3.v') AS DOUBLE) AS o3,
    CAST(JSON_EXTRACT(raw_json, '$.data.iaqi.no2.v') AS DOUBLE) AS no2
  FROM {{ source('raw', 'raw_api_data') }}
)

SELECT
  CAST(date AS DATE) AS date,
  pm25,
  pm10,
  o3,
  no2
FROM parsed
{% if is_incremental() %}
WHERE CAST(date AS DATE) > (SELECT MAX(date) FROM {{ this }})
{% endif %}
