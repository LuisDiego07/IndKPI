from enum import Enum

class MachineStatus(Enum):
    RUNNING = "RUNNING"
    FAILURE = "FAILURE"
    MAINTENANCE = "MAINTENANCE"
    IDLE = "IDLE"

class EventType(Enum):
    PRODUCTION = "PRODUCTION"
    FAILURE = "FAILURE_EVENT"
    MAINTENANCE = "MAINTENANCE_EVENT"
    SETUP = "SETUP"