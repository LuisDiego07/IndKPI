from pathlib import Path
from bronze_loader import load_bronze, save_bronze

# Resolve project root (IndKPIs/)
PROJECT_ROOT = Path(__file__).resolve().parents[1]

# Input from simulator
json_path = PROJECT_ROOT / "data_telemetry.json"

# Load Bronze
df_bronze = load_bronze(json_path)

# Persist Bronze
save_bronze(df_bronze)
