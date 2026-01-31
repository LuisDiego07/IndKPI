INSERT INTO analytics.dim_date (date, year, month, day)
SELECT DISTINCT
    DATE(timestamp) AS date,
    EXTRACT(YEAR  FROM timestamp)::INT,
    EXTRACT(MONTH FROM timestamp)::INT,
    EXTRACT(DAY   FROM timestamp)::INT
FROM staging.gold_oee
ON CONFLICT (date) DO NOTHING;
