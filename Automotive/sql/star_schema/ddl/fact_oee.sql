CREATE TABLE IF NOT EXISTS analytics.fact_oee (
    fact_oee_sk       SERIAL PRIMARY KEY,

    date_sk           INT NOT NULL,
    machine_sk        INT NOT NULL,

    availability      NUMERIC(6,4) NOT NULL,
    performance       NUMERIC(6,4) NOT NULL,
    quality           NUMERIC(6,4) NOT NULL,
    oee               NUMERIC(6,4) NOT NULL,

    planned_time_s    INT NOT NULL,
    operating_time_s  INT NOT NULL,
    downtime_s        INT NOT NULL,

    total_units       INT NOT NULL,
    good_units        INT NOT NULL,

    CONSTRAINT fk_oee_date
        FOREIGN KEY (date_sk)
        REFERENCES analytics.dim_date (date_sk),

    CONSTRAINT fk_oee_machine
        FOREIGN KEY (machine_sk)
        REFERENCES analytics.dim_machine (machine_sk)
);
