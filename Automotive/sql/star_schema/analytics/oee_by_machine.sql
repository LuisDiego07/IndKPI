SELECT
    m.machine_id,
    ROUND(AVG(f.oee), 3) AS avg_oee,
    ROUND(AVG(f.availability), 3) AS availability,
    ROUND(AVG(f.performance), 3)  AS performance,
    ROUND(AVG(f.quality), 3)      AS quality
FROM analytics.fact_oee f
JOIN analytics.dim_machine m
    ON f.machine_sk = m.machine_sk
GROUP BY m.machine_id
ORDER BY avg_oee DESC;
