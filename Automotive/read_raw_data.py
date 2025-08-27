import pandas as pd

path_arquivo_csv = r"C:\Users\diego.oliveira_sense\Downloads\industrial_iot_sensor_data_repository\industrial_iot_sensor_data_repository.csv"

df = pd.read_csv(path_arquivo_csv)
print(df.columns)

#print(len(df))