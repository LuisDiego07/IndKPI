import pandas as pd

EVENT_INTERVAL_SECONDS = 60

def enrich_silver(df: pd.DataFrame) -> pd.DataFrame:

    df = df.copy()

    # Flags operacionais
    df["is_running"] = df["status"] == "RUNNING"
    df["is_failure"] = df["status"] == "FAILURE"

    # Tempo por evento
    df["planned_time_s"] = EVENT_INTERVAL_SECONDS
    df["operating_time_s"] = df["is_running"] * EVENT_INTERVAL_SECONDS
    df["downtime_s"] = df["is_failure"] * EVENT_INTERVAL_SECONDS

    # Produção
    df["good_units"] = df["produced_units"] - df["defective_units"]

    # Sanidade
    df.loc[df["good_units"] < 0, "good_units"] = 0

    return df
