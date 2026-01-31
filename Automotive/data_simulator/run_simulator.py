from datetime import datetime
import json
from Automotive.data_simulator.machine import Machine
from simulator import TelemetrySimulator

machines = [
    Machine("CNC_01", "CNC", nominal_cycle_time=55, defect_rate=0.02, failure_rate=0.01),
    Machine("ROBOT_01", "WELDING_ROBOT", nominal_cycle_time=40, defect_rate=0.01, failure_rate=0.005),
    Machine("PRESS_01", "PRESS", nominal_cycle_time=65, defect_rate=0.03, failure_rate=0.015),
]

simulator = TelemetrySimulator(machines)

events = simulator.run(
    start_time=datetime.now(),
    duration_minutes=60,   # 1 hora
    interval_seconds=60    # evento por minuto
)

# Exemplo: salvar em JSON (Data Lake Bronze)
with open("telemetry_events.json", "w") as f:
    json.dump(events, f, indent=2)

print(f"{len(events)} eventos gerados.")
