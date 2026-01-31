import json
from pathlib import Path
from typing import Union
import pandas as pd

REQUIRED_COLUMNS = [
    "timestamp",
    "machine_id",
    "machine_type",
    "status",
    "cycle_time",
    "produced_units",
    "defective_units",
    "energy_kw",
    "temperature_c",
    "vibration_mm_s"
]

def load_bronze(path: Union[Path, str]) -> pd.DataFrame:
    path = Path(path)

    with open(path, "r", encoding="utf-8") as f:
        data = json.load(f)

    df = pd.DataFrame(data)

    missing = set(REQUIRED_COLUMNS) - set(df.columns)
    if missing:
        raise ValueError(f"Missing columns in bronze layer: {missing}")

    df["timestamp"] = pd.to_datetime(df["timestamp"], errors="coerce")

    numeric_cols = [
        "cycle_time",
        "produced_units",
        "defective_units",
        "energy_kw",
        "temperature_c",
        "vibration_mm_s"
    ]

    for col in numeric_cols:
        df[col] = pd.to_numeric(df[col], errors="coerce")

    return df

def save_bronze(df: pd.DataFrame, output_path: Union[Path, str, None] = None):
    if output_path is None:
        output_path = Path("data_lake/bronze/telemetry_events.parquet")
    else:
        output_path = Path(output_path)

    output_path.parent.mkdir(parents=True, exist_ok=True)

    df.to_parquet(output_path, index=False)
