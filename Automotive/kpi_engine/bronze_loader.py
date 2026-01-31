import json
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

def load_bronze(path: str) -> pd.DataFrame:
    with open(path) as f:
        data = json.load(f)

    df = pd.DataFrame(data)

    # Validação mínima
    missing = set(REQUIRED_COLUMNS) - set(df.columns)
    if missing:
        raise ValueError(f"Missing columns: {missing}")

    df["timestamp"] = pd.to_datetime(df["timestamp"])

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
