

import random
import string

def generate_password(length):
    if not isinstance(length, int) or length < 3:
        raise ValueError("Password length must be an integer of at least 3.")

    lowercase = string.ascii_lowercase
    uppercase = string.ascii_uppercase
    digits = string.digits
    password_chars = [
        random.choice(lowercase),
        random.choice(uppercase),
        random.choice(digits)
    ]
    all_chars = lowercase + uppercase + digits
    password_chars += random.choices(all_chars, k=length - 3)

    random.shuffle(password_chars)

    return ''.join(password_chars)

if __name__ == "__main__":
    try:
        length = int(input("Enter desired password length (min 3): "))
        password = generate_password(length)
        print("Generated Password:", password)
    except ValueError as e:
        print("Error:", e)

