from datetime import datetime
import json
from data_simulator.machine import Machine
from .simulator import TelemetrySimulator

machines = [
    Machine("CNC_01", "CNC", 55, 0.02, 0.01),
    Machine("ROBOT_01", "WELDING_ROBOT", 40, 0.01, 0.005),
    Machine("PRESS_01", "PRESS", 65, 0.03, 0.015),
]

simulator = TelemetrySimulator(machines)

with open("data_telemetry.json", "w") as f:
    for event in simulator.run(datetime.now(), 60):
        f.write(json.dumps(event) + "\n")