import random

class ProductionContext:

    VEHICLE_MODELS = ["SEDAN_X", "SUV_Y", "TRUCK_Z"]
    SHIFTS = ["A", "B", "C"]

    @staticmethod
    def generate_context():
        return {
            "shift": random.choice(ProductionContext.SHIFTS),
            "vehicle_model": random.choice(ProductionContext.VEHICLE_MODELS),
            "operator_id": f"OP_{random.randint(1,50):03}",
            "production_order_id": f"PO_{random.randint(1000,9999)}"
        }