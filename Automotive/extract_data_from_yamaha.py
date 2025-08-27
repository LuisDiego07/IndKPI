import pandas as pd

path_crosser_150_2025 = r"C:\Users\diego.oliveira_sense\Downloads\specifications_yamaha_crosser_150_2025.csv"

df_crosser_150_2025 = pd.read_csv(path_crosser_150_2025)
df_crosser_150_2025["modelo"] = "XTZ 150cc Crosser"
df_crosser_150_2025["ano"] = "2025"

print(df_crosser_150_2025)

#Loads Data into Postgre SQL

