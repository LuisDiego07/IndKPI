CREATE TABLE IF NOT EXISTS analytics.dim_machine (
    machine_sk   SERIAL PRIMARY KEY,
    machine_id   VARCHAR(50) NOT NULL UNIQUE,
    machine_type VARCHAR(50) NOT NULL
);
