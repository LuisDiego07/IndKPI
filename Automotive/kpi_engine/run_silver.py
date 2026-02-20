from pathlib import Path
import pandas as pd
from silver_transformer import enrich_silver, save_silver


BRONZE_ROOT = Path("data_lake/bronze/telemetry_events")


def load_all_bronze(root: Path) -> pd.DataFrame:

    parquet_files = list(root.rglob("*.parquet"))

    if not parquet_files:
        raise FileNotFoundError("No Bronze parquet files found.")

    dfs = [pd.read_parquet(file) for file in parquet_files]

    return pd.concat(dfs, ignore_index=True)


def main():
    print("Loading Bronze layer...")
    df_bronze = load_all_bronze(BRONZE_ROOT)

    print(f"Loaded {len(df_bronze)} records from Bronze.")

    print("Transforming to Silver...")
    df_silver = enrich_silver(df_bronze)

    print("Saving Silver layer...")
    save_silver(df_silver)

    print("Silver layer successfully updated.")


if __name__ == "__main__":
    main()