import random

class FailureModel:

    def __init__(self, base_failure_rate: float):
        self.base_failure_rate = base_failure_rate
        self.health_index = 1.0

    def degrade(self):
        self.health_index -= random.uniform(0.001, 0.005)
        self.health_index = max(self.health_index, 0)

    def check_failure(self):
        probability = self.base_failure_rate * (1 + (1 - self.health_index))
        return random.random() < probability