import pandas as pd
from pathlib import Path
from typing import Union
from datetime import datetime

EVENT_INTERVAL_SECONDS = 60


# =========================
# ENRICH SILVER
# =========================
def enrich_silver(df: pd.DataFrame) -> pd.DataFrame:
    df = df.copy()

    # =========================
    # NORMALIZATION
    # =========================
    df = df.sort_values(["machine_id", "timestamp"])

    # Valid physical values
    df["produced_units"] = df["produced_units"].clip(lower=0)
    df["defective_units"] = df["defective_units"].clip(lower=0)
    df["energy_kw"] = df["energy_kw"].clip(lower=0)
    df["temperature_c"] = df["temperature_c"].clip(lower=-50, upper=200)
    df["vibration_mm_s"] = df["vibration_mm_s"].clip(lower=0)

    # =========================
    # OPERATIONAL FLAGS
    # =========================
    df["is_running"] = df["status"] == "RUNNING"
    df["is_failure"] = df["status"] == "FAILURE"
    df["is_idle"] = df["status"] == "IDLE"

    # =========================
    # TIME
    # =========================
    df["planned_time_s"] = EVENT_INTERVAL_SECONDS
    df["operating_time_s"] = df["is_running"] * EVENT_INTERVAL_SECONDS
    df["downtime_s"] = df["is_failure"] * EVENT_INTERVAL_SECONDS
    df["idle_time_s"] = df["is_idle"] * EVENT_INTERVAL_SECONDS

    # =========================
    # PRODUCTION
    # =========================
    df["good_units"] = df["produced_units"] - df["defective_units"]
    df.loc[df["good_units"] < 0, "good_units"] = 0

    # =========================
    # INTERMEDIARY RATES
    # =========================
    df["defect_rate_event"] = df.apply(
        lambda row: (
            row["defective_units"] / row["produced_units"]
            if row["produced_units"] > 0 else 0
        ),
        axis=1
    )

    df["utilization_rate_event"] = (
        df["operating_time_s"] / df["planned_time_s"]
    )

    # =========================
    # ENERGY PER UNIT
    # =========================
    df["energy_per_unit"] = df.apply(
        lambda row: (
            row["energy_kw"] / row["produced_units"]
            if row["produced_units"] > 0 else 0
        ),
        axis=1
    )

    # =========================
    # SILVER METADATA
    # =========================
    df["silver_processed_at"] = datetime.utcnow()

    return df


# =========================
# SAVE SILVER (PARTITIONED)
# =========================
def save_silver(
    df: pd.DataFrame,
    output_root: Union[Path, str] = "data_lake/silver/telemetry_enriched"
):
    output_root = Path(output_root)

    df["year"] = df["timestamp"].dt.year
    df["month"] = df["timestamp"].dt.month
    df["day"] = df["timestamp"].dt.day

    for (year, month, day), group in df.groupby(["year", "month", "day"]):
        partition_path = (
            output_root /
            f"year={year}" /
            f"month={month:02d}" /
            f"day={day:02d}"
        )

        partition_path.mkdir(parents=True, exist_ok=True)

        file_name = f"silver_batch_{datetime.utcnow().timestamp()}.parquet"

        group.drop(columns=["year", "month", "day"]).to_parquet(
            partition_path / file_name,
            index=False
        )