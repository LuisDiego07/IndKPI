from datetime import datetime
from data_simulator.failure_model import FailureModel
from data_simulator.sensor_model import SensorModel
from data_simulator.production_context import ProductionContext
from data_simulator.enums import MachineStatus, EventType
import random


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
        self.status = MachineStatus.RUNNING
        self.failure_model = FailureModel(failure_rate)

    def generate_event(self, timestamp: datetime):

        self.failure_model.degrade()

        if self.failure_model.check_failure():
            self.status = MachineStatus.FAILURE

        context = ProductionContext.generate_context()

        if self.status == MachineStatus.RUNNING:
            sensors = SensorModel.generate_running_metrics(
                self.nominal_cycle_time
            )
            produced = 1
            defective = 1 if random.random() < self.defect_rate else 0
            event_type = EventType.PRODUCTION.value

        else:
            sensors = SensorModel.generate_failure_metrics()
            produced = 0
            defective = 0
            event_type = EventType.FAILURE.value

        return {
            "timestamp": timestamp.isoformat(),
            "machine_id": self.machine_id,
            "machine_type": self.machine_type,
            "status": self.status.value,
            "event_type": event_type,
            "health_index": round(self.failure_model.health_index, 4),
            "produced_units": produced,
            "defective_units": defective,
            **sensors,
            **context
        }