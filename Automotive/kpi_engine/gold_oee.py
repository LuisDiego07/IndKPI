import pandas as pd
from pathlib import Path
from typing import Union

def calculate_oee_gold(
    df: pd.DataFrame,
    ideal_cycle_time: dict
) -> pd.DataFrame:

    results = []

    for machine_id, group in df.groupby("machine_id"):

        planned_time = group["planned_time_s"].sum()
        operating_time = group["operating_time_s"].sum()
        downtime = group["downtime_s"].sum()

        total_units = group["produced_units"].sum()
        good_units = group["good_units"].sum()

        ideal_ct = ideal_cycle_time.get(machine_id, 0)

        availability = (
            (planned_time - downtime) / planned_time
            if planned_time > 0 else 0
        )

        performance = (
            (ideal_ct * total_units) / operating_time
            if operating_time > 0 else 0
        )

        quality = (
            good_units / total_units
            if total_units > 0 else 0
        )

        oee = availability * performance * quality

        results.append({
            "machine_id": machine_id,
            "availability": round(availability, 4),
            "performance": round(performance, 4),
            "quality": round(quality, 4),
            "oee": round(oee, 4),
            "planned_time_s": planned_time,
            "operating_time_s": operating_time,
            "downtime_s": downtime,
            "total_units": int(total_units),
            "good_units": int(good_units)
        })

    return pd.DataFrame(results)

def save_gold_parquet(
    df: pd.DataFrame,
    output_path: Union[Path, str]
):
    output_path = Path(output_path)
    output_path.parent.mkdir(parents=True, exist_ok=True)

    df.to_parquet(output_path, index=False)