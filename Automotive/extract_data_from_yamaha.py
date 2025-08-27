from pathlib import Path
import pandas as pd

# Caminho relativo dentro do projeto
data_dir = Path(__file__).parent / "data"
path_crosser_150_2025 = data_dir / "specifications_yamaha_crosser_150_2025.csv"

df_crosser_150_2025 = pd.read_csv(path_crosser_150_2025)
df_crosser_150_2025["modelo"] = "XTZ 150cc Crosser"
df_crosser_150_2025["ano"] = "2025"
