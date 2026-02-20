from datetime import timedelta

class TelemetrySimulator:

    def __init__(self, machines):
        self.machines = machines

    def run(self, start_time, duration_minutes, interval_seconds=60):

        current_time = start_time
        end_time = start_time + timedelta(minutes=duration_minutes)

        while current_time < end_time:
            for machine in self.machines:
                yield machine.generate_event(current_time)
            current_time += timedelta(seconds=interval_seconds)