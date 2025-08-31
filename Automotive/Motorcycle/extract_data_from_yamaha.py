from pathlib import Path
import pandas as pd
from deltalake.writer import write_deltalake

# Path depends on "data" directory on project
data_dir = Path(__file__).parent / "data"
path_crosser_150_2025 = data_dir / "raw/specifications_yamaha_crosser_150_2025.csv"
path_factor_125_2025 = data_dir / "raw/specifications_yamaha_factor_125_2025.csv"

df_crosser_150_2025 = pd.read_csv(path_crosser_150_2025)
df_crosser_150_2025["modelo"] = "XTZ 150cc Crosser"
df_crosser_150_2025["ano"] = "2025"

df_factor_125_2025 = pd.read_csv(path_factor_125_2025)
df_factor_125_2025["modelo"] = "YBR 125cc Factor"
df_factor_125_2025["ano"] = "2025"

df_yamaha_data = pd.concat([df_crosser_150_2025, df_factor_125_2025], ignore_index=True)

output_file = data_dir / "silver" / "tech_data_yamaha.csv"

output_file.parent.mkdir(parents=True, exist_ok=True)
df_yamaha_data.to_csv(output_file, index=False, encoding="utf-8")