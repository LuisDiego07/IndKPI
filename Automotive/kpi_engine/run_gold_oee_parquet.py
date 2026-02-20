from pathlib import Path
import pandas as pd
from gold_oee import calculate_oee_gold, save_gold_parquet


# =========================
# CONFIG
# =========================
IDEAL_CYCLE_TIME = {
    "CNC_01": 55,
    "ROBOT_01": 40,
    "PRESS_01": 65
}

SILVER_ROOT = Path("data_lake/silver/telemetry_enriched")


# =========================
# LOAD SILVER (PARTITIONED)
# =========================
def load_all_silver(root: Path) -> pd.DataFrame:
    parquet_files = list(root.rglob("*.parquet"))

    if not parquet_files:
        raise FileNotFoundError("No Silver parquet files found.")

    dfs = [pd.read_parquet(file) for file in parquet_files]

    return pd.concat(dfs, ignore_index=True)


# =========================
# MAIN
# =========================
def main():
    print("Loading Silver layer...")
    df_silver = load_all_silver(SILVER_ROOT)
    print(f"Loaded {len(df_silver)} records from Silver.")

    print("Calculating Gold KPIs...")
    df_gold = calculate_oee_gold(
        df_silver,
        IDEAL_CYCLE_TIME,
        aggregation_level="day"
    )

    print("Saving Gold layer (partitioned)...")
    save_gold_parquet(df_gold)

    print("Gold layer successfully updated.")


if __name__ == "__main__":
    main()