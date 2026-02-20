import random

class SensorModel:

    @staticmethod
    def generate_running_metrics(nominal_cycle_time):
        return {
            "cycle_time": max(0.1, random.gauss(nominal_cycle_time, 3)),
            "energy_kw": round(random.uniform(8, 15), 2),
            "temperature_c": round(random.uniform(60, 75), 2),
            "vibration_mm_s": round(random.uniform(1.5, 3.0), 2),
        }

    @staticmethod
    def generate_failure_metrics():
        return {
            "cycle_time": None,
            "energy_kw": round(random.uniform(2, 4), 2),
            "temperature_c": round(random.uniform(70, 90), 2),
            "vibration_mm_s": round(random.uniform(5.5, 8.0), 2),
        }