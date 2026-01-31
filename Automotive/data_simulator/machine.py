import random
from datetime import datetime

class Machine:
    def __init__(
        self,
        machine_id: str,
        machine_type: str,
        nominal_cycle_time: float,
        defect_rate: float,
        failure_rate: float
    ):
        self.machine_id = machine_id
        self.machine_type = machine_type
        self.nominal_cycle_time = nominal_cycle_time
        self.defect_rate = defect_rate
        self.failure_rate = failure_rate
        self.status = "RUNNING"

    def generate_event(self, timestamp: datetime) -> dict:
        # Simula falha
        if random.random() < self.failure_rate:
            self.status = "FAILURE"
        elif self.status == "FAILURE" and random.random() < 0.3:
            self.status = "RUNNING"

        if self.status == "RUNNING":
            cycle_time = random.gauss(self.nominal_cycle_time, 3)
            produced_units = 1
            defective_units = 1 if random.random() < self.defect_rate else 0
            energy_kw = random.uniform(8, 15)
            temperature_c = random.uniform(60, 75)
            vibration = random.uniform(1.5, 3.0)
        else:
            cycle_time = None
            produced_units = 0
            defective_units = 0
            energy_kw = random.uniform(2, 4)
            temperature_c = random.uniform(50, 60)
            vibration = random.uniform(5.5, 7.5)

        return {
            "timestamp": timestamp.isoformat(),
            "machine_id": self.machine_id,
            "machine_type": self.machine_type,
            "status": self.status,
            "cycle_time": cycle_time,
            "produced_units": produced_units,
            "defective_units": defective_units,
            "energy_kw": round(energy_kw, 2),
            "temperature_c": round(temperature_c, 2),
            "vibration_mm_s": round(vibration, 2),
        }
