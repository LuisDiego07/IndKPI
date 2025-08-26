import pandas as pd
import numpy as np
from datetime import datetime, timedelta
import random

# Número de registros simulados
n = 1000

# Função para gerar timestamps sequenciais
def generate_timestamps(start, n, delta_minutes=1):
    return [start + timedelta(minutes=i*delta_minutes) for i in range(n)]

start_time = datetime.now()
timestamps = generate_timestamps(start_time, n)

# Tipos de veículos
vehicle_types = ['car', 'motorcycle']
brands = ['Honda', 'Toyota', 'BMW', 'Yamaha', 'Kawasaki']
models = ['Model A', 'Model B', 'Model C', 'Model D', 'Model E']
engine_types = ['combustion', 'electric', 'hybrid']
gear_positions = ['N', '1', '2', '3', '4', '5', '6']

# Criando o DataFrame simulado
df = pd.DataFrame({
    'timestamp': timestamps,
    'vehicle_id': [f'VEH{str(i).zfill(4)}' for i in range(n)],
    'vehicle_type': [random.choice(vehicle_types) for _ in range(n)],
    'brand': [random.choice(brands) for _ in range(n)],
    'model': [random.choice(models) for _ in range(n)],
    'year': [random.randint(2015, 2025) for _ in range(n)],
    'engine_type': [random.choice(engine_types) for _ in range(n)],
    'engine_capacity': [round(random.uniform(0.6, 3.5),1) for _ in range(n)],
    'transmission_type': [random.choice(['manual','automatic','CVT']) for _ in range(n)],
    'speed': [round(random.uniform(0, 180),1) for _ in range(n)],
    'rpm': [random.randint(500, 6000) for _ in range(n)],
    'throttle_position': [round(random.uniform(0,100),1) for _ in range(n)],
    'brake_status': [random.choice([0,1]) for _ in range(n)],
    'gear_position': [random.choice(gear_positions) for _ in range(n)],
    'fuel_level': [round(random.uniform(0,100),1) for _ in range(n)],
    'battery_voltage': [round(random.uniform(11,14),1) for _ in range(n)],
    'fuel_consumption_rate': [round(random.uniform(5,15),2) for _ in range(n)], # km/l
    'energy_consumption': [round(random.uniform(0,2),2) for _ in range(n)], # kWh/km
    'co2_emission': [round(random.uniform(50,250),1) for _ in range(n)],
    'engine_temperature': [round(random.uniform(70,120),1) for _ in range(n)],
    'oil_pressure': [round(random.uniform(20,80),1) for _ in range(n)],
    'tire_pressure': [round(random.uniform(28,36),1) for _ in range(n)],
    'fault_code': [random.choice(['P0010','P0020','P0030','', '']) for _ in range(n)],
    'fault_flag': [0 if f=='' else 1 for f in [random.choice(['P0010','P0020','P0030','', '']) for _ in range(n)]],
    'maintenance_due': [random.randint(0,12) for _ in range(n)], # meses
    'operational_status': [random.choice(['OK','Warning','Failure']) for _ in range(n)],
    'decision_label': [random.choice(['Normal','Check Engine','Reduce Speed']) for _ in range(n)],
    'ambient_temperature': [round(random.uniform(-10,40),1) for _ in range(n)],
    'road_condition': [random.choice(['dry','wet','off-road']) for _ in range(n)],
    'altitude': [round(random.uniform(0,3000),1) for _ in range(n)],
    'traffic_condition': [random.choice(['light','moderate','heavy']) for _ in range(n)]
})

# Visualizar as primeiras linhas
print(df.head())

# Número de linhas e colunas
print(f"Linhas: {df.shape[0]}, Colunas: {df.shape[1]}")

# Colunas do DataFrame
print("Colunas:", df.columns.tolist())

# Exemplo: filtrar apenas registros com falha
falhas = df[df['fault_flag']==1]
print(f"\nTotal de registros com falha: {falhas.shape[0]}")
print(falhas.head())

# Caminho de destino do CSV
output_path = r"C:\Users\diego.oliveira_sense\Downloads\sample_data.csv"

# Salva o DataFrame em CSV
df.to_csv(output_path, index=False)

print(f"\nArquivo CSV gerado em: {output_path}")