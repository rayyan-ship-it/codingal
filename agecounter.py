

def get_valid_age():
    try:       
        age_input = input("Enter your age: ").strip()

        age = int(age_input)
        if age < 0:
            raise ValueError("Age cannot be negative.")
        elif age > 120:
            raise ValueError("Age seems unrealistic. Please enter a valid age.")

        return age

    except ValueError as e:
        print(f"Invalid input: {e}")
        return None


if __name__ == "__main__":
    age = get_valid_age()
    if age is not None:
        print(f"Your age ({age}) is valid.")
    else:
        print("Please try again with a valid age.")
