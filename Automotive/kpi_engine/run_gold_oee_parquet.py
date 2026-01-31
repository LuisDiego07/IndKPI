import pandas as pd
from pathlib import Path
from gold_oee import calculate_oee_gold, save_gold_parquet

IDEAL_CYCLE_TIME = {
    "CNC_01": 55,
    "ROBOT_01": 40,
    "PRESS_01": 65
}

# Definição de paths
SILVER_PATH = Path("data_lake/silver/telemetry_enriched.parquet")
GOLD_PATH = Path("data_lake/gold/oee.parquet")

# Leitura da Silver
df_silver = pd.read_parquet(SILVER_PATH)

# Cálculo da Gold
df_gold = calculate_oee_gold(df_silver, IDEAL_CYCLE_TIME)

# Persistência da Gold
save_gold_parquet(df_gold, GOLD_PATH)
