class IntegerToRoman:
    """
    A class to convert integers to Roman numerals.
    Supports values from 1 to 3999.
    """
    _roman_map = [
        (1000, "M"), (900, "CM"), (500, "D"), (400, "CD"),
        (100, "C"), (90, "XC"), (50, "L"), (40, "XL"),
        (10, "X"), (9, "IX"), (5, "V"), (4, "IV"), (1, "I")
    ]

    def __init__(self, number):
        """
        Initialize with an integer number.
        Raises ValueError if number is out of range.
        """
        if not isinstance(number, int):
            raise TypeError("Input must be an integer.")
        if number <= 0 or number > 3999:
            raise ValueError("Number must be between 1 and 3999.")
        self.number = number

    def convert(self):
        """
        Convert the integer to a Roman numeral string.
        """
        num = self.number
        roman_numeral = ""

        for value, symbol in self._roman_map:
            while num >= value:
                roman_numeral += symbol
                num -= value

        return roman_numeral
if __name__ == "__main__":
    try:
        user_input = input("Enter an integer (1-3999): ").strip()
        if not user_input.isdigit():
            raise ValueError("Invalid input. Please enter a positive integer.")

        number = int(user_input)
        converter = IntegerToRoman(number)
        print(f"Roman numeral: {converter.convert()}")

    except (ValueError, TypeError) as e:
        print(f"Error: {e}")
