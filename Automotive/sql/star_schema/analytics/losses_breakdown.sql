SELECT
    m.machine_id,
    ROUND(1 - AVG(f.availability), 3) AS availability_loss,
    ROUND(1 - AVG(f.performance), 3)  AS performance_loss,
    ROUND(1 - AVG(f.quality), 3)      AS quality_loss
FROM analytics.fact_oee f
JOIN analytics.dim_machine m
    ON f.machine_sk = m.machine_sk
GROUP BY m.machine_id;
