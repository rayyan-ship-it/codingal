class Vehicle:
    def __init__(self, name, seating_capacity):
        self.name = name
        self.seating_capacity = seating_capacity

    def fare(self):
        return self.seating_capacity * 100

class Bus(Vehicle):
    def fare(self):
        base_fare = super().fare()
        maintenance_charge = base_fare * 0.10 
        return base_fare + maintenance_charge

school_bus = Bus("School Volvo", 50)
print(f"Total Bus Fare: {school_bus.fare()} Rs")
