CREATE TABLE IF NOT EXISTS analytics.dim_date (
    date_sk  SERIAL PRIMARY KEY,
    date     DATE NOT NULL UNIQUE,
    year     INT  NOT NULL,
    month    INT  NOT NULL,
    day      INT  NOT NULL
);
