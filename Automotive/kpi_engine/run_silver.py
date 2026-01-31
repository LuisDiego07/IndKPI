import pandas as pd
from silver_transformer import enrich_silver, save_silver

bronze_file = "data_lake/bronze/telemetry_events.parquet"

# Read Bronze layer
df_bronze = pd.read_parquet(bronze_file)

# Transform to Silver layer
df_silver = enrich_silver(df_bronze)

# Persist Silver layer
save_silver(df_silver)
