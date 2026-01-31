INSERT INTO analytics.fact_oee (
    date_sk,
    machine_sk,
    availability,
    performance,
    quality,
    oee,
    planned_time_s,
    operating_time_s,
    downtime_s,
    total_units,
    good_units
)
SELECT
    d.date_sk,
    m.machine_sk,
    g.availability,
    g.performance,
    g.quality,
    g.oee,
    g.planned_time_s,
    g.operating_time_s,
    g.downtime_s,
    g.total_units,
    g.good_units
FROM staging.gold_oee g
JOIN analytics.dim_date d
    ON d.date = DATE(g.timestamp)
JOIN analytics.dim_machine m
    ON m.machine_id = g.machine_id;
