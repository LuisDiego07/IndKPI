from bronze_loader import load_bronze
from silver_transformer import enrich_silver
from gold_oee import calculate_oee_gold

IDEAL_CYCLE_TIME = {
    "CNC_01": 55,
    "ROBOT_01": 40,
    "PRESS_01": 65
}

df_bronze = load_bronze("telemetry_events.json")
df_silver = enrich_silver(df_bronze)
df_gold = calculate_oee_gold(df_silver, IDEAL_CYCLE_TIME)

print(df_gold)
