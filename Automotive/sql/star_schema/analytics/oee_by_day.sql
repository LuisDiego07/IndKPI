SELECT
    d.date,
    ROUND(AVG(f.oee), 3) AS avg_oee
FROM analytics.fact_oee f
JOIN analytics.dim_date d
    ON f.date_sk = d.date_sk
GROUP BY d.date
ORDER BY d.date;
