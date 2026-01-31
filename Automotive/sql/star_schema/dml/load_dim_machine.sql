INSERT INTO analytics.dim_machine (machine_id, machine_type)
SELECT DISTINCT
    machine_id,
    machine_type
FROM staging.gold_oee
ON CONFLICT (machine_id) DO NOTHING;
