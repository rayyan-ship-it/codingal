# Program to generate squares of numbers in a given range
# and separate them into even and odd lists

def get_integer(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Invalid input. Please enter an integer.")

def generate_squares(start, end):
    return [num ** 2 for num in range(start, end + 1)]

def separate_even_odd(numbers):
    even = [n for n in numbers if n % 2 == 0]
    odd = [n for n in numbers if n % 2 != 0]
    return even, odd

def main():
    print("=== Squares Generator and Separator ===")
    
    start = get_integer("Enter start of range: ")
    end = get_integer("Enter end of range: ")

    if start > end:
        print("Swapping values so start <= end.")
        start, end = end, start

    squares = generate_squares(start, end)

    even_squares, odd_squares = separate_even_odd(squares)

    # Display results
    print(f"\nNumbers: {list(range(start, end + 1))}")
    print(f"Squares: {squares}")
    print(f"Even Squares: {even_squares}")
    print(f"Odd Squares: {odd_squares}")

if __name__ == "__main__":
    main()
