class BMW:
    """BMW car class with fuel type and max speed methods."""
    def fuel_type(self):
        return "Petrol"

    def max_speed(self):
        return "250 km/h"


class Ferrari:
    """Ferrari car class with fuel type and max speed methods."""
    def fuel_type(self):
        return "Petrol (High Octane)"

    def max_speed(self):
        return "340 km/h"


def car_details(car):
    """
    Function demonstrating polymorphism.
    Accepts any object that has fuel_type() and max_speed() methods.
    """
    try:
        print(f"{car.__class__.__name__} Fuel Type: {car.fuel_type()}")
        print(f"{car.__class__.__name__} Max Speed: {car.max_speed()}")
        print("-" * 40)
    except AttributeError:
        print(f"Error: {car.__class__.__name__} does not have required methods.")


if __name__ == "__main__":
    # Create objects
    bmw_car = BMW()
    ferrari_car = Ferrari()

    # Demonstrate polymorphism
    for vehicle in (bmw_car, ferrari_car):
        car_details(vehicle)

