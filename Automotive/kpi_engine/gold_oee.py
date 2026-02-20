import pandas as pd
from pathlib import Path
from typing import Union, Dict
from datetime import datetime


# =========================
# GOLD KPI CALCULATION
# =========================
def calculate_oee_gold(
    df: pd.DataFrame,
    ideal_cycle_time: Dict[str, float],
    aggregation_level: str = "day"
) -> pd.DataFrame:

    df = df.copy()

    if aggregation_level == "day":
        df["period"] = df["timestamp"].dt.date
    elif aggregation_level == "hour":
        df["period"] = df["timestamp"].dt.floor("H")
    else:
        raise ValueError("aggregation_level must be 'day' or 'hour'")

    results = []

    for (machine_id, period), group in df.groupby(["machine_id", "period"]):

        planned_time = group["planned_time_s"].sum()
        operating_time = group["operating_time_s"].sum()
        downtime = group["downtime_s"].sum()

        total_units = group["produced_units"].sum()
        good_units = group["good_units"].sum()

        ideal_ct = ideal_cycle_time.get(machine_id, 0)

        # =========================
        # OEE COMPONENTS
        # =========================
        availability = (
            operating_time / planned_time
            if planned_time > 0 else 0
        )

        performance = (
            (ideal_ct * total_units) / operating_time
            if operating_time > 0 else 0
        )

        performance = min(performance, 1.0)

        quality = (
            good_units / total_units
            if total_units > 0 else 0
        )

        oee = availability * performance * quality

        # =========================
        # MTBF / MTTR
        # =========================
        failures = group["is_failure"].sum()

        mtbf = (
            operating_time / failures
            if failures > 0 else operating_time
        )

        mttr = (
            downtime / failures
            if failures > 0 else 0
        )

        results.append({
            "machine_id": machine_id,
            "period": period,
            "availability": round(availability, 4),
            "performance": round(performance, 4),
            "quality": round(quality, 4),
            "oee": round(oee, 4),
            "mtbf_s": round(mtbf, 2),
            "mttr_s": round(mttr, 2),
            "planned_time_s": planned_time,
            "operating_time_s": operating_time,
            "downtime_s": downtime,
            "total_units": int(total_units),
            "good_units": int(good_units),
            "gold_processed_at": datetime.utcnow()
        })

    return pd.DataFrame(results)


# =========================
# SAVE GOLD (PARTITIONED)
# =========================
def save_gold_parquet(
    df: pd.DataFrame,
    output_root: Union[Path, str] = "data_lake/gold/oee_metrics"
):
    output_root = Path(output_root)

    if df.empty:
        return

    df["year"] = pd.to_datetime(df["period"]).dt.year
    df["month"] = pd.to_datetime(df["period"]).dt.month
    df["day"] = pd.to_datetime(df["period"]).dt.day

    for (year, month, day), group in df.groupby(["year", "month", "day"]):

        partition_path = (
            output_root /
            f"year={year}" /
            f"month={month:02d}" /
            f"day={day:02d}"
        )

        partition_path.mkdir(parents=True, exist_ok=True)

        file_name = f"gold_batch_{datetime.utcnow().timestamp()}.parquet"

        group.drop(columns=["year", "month", "day"]).to_parquet(
            partition_path / file_name,
            index=False
        )