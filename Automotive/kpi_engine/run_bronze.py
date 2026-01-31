from bronze_loader import load_bronze, save_bronze

df_bronze = load_bronze("telemetry_events.json")

save_bronze(df_bronze)