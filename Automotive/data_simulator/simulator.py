from datetime import datetime, timedelta
from typing import List
from Automotive.data_simulator.machine import Machine

class TelemetrySimulator:
    def __init__(self, machines: List[Machine]):
        self.machines = machines

    def run(
        self,
        start_time: datetime,
        duration_minutes: int,
        interval_seconds: int = 60
    ):
        events = []
        current_time = start_time
        end_time = start_time + timedelta(minutes=duration_minutes)

        while current_time < end_time:
            for machine in self.machines:
                event = machine.generate_event(current_time)
                events.append(event)
            current_time += timedelta(seconds=interval_seconds)

        return events
