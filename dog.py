
class Dog:
    species = "Canis familiaris"

    def __init__(self, name, breed):
        if not isinstance(name, str) or not name.strip():
            raise ValueError("Name must be a non-empty string.")
        if not isinstance(breed, str) or not breed.strip():
            raise ValueError("Breed must be a non-empty string.")

        self.name = name.strip()
        self.breed = breed.strip()

    def display_details(self):
        """Display the dog's details."""
        print(f"Name: {self.name}")
        print(f"Breed: {self.breed}")
        print(f"Species: {Dog.species}")
        print("-" * 30)


try:
    dog1 = Dog("Buddy", "Golden Retriever")
    dog2 = Dog("Lucy", "Beagle")
    print("Dog 1 Details:")
    dog1.display_details()

    print("Dog 2 Details:")
    dog2.display_details()

except ValueError as e:
    print(f"Error: {e}")
