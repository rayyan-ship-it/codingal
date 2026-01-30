def get_odd_numbers_upto(n):
    return[i for i in range(1,n) if i%2 !=0]
def get_odd_numbers_step(n):
    return list (range(1,n+1))
def main():
    try:
        user_input=input("enter an integer").strip()
        if not user_input.isdigit():
            print("error please print a positive integer")
            return
        limit=int(user_input)
        if limit<=0:
            print("error: number must be greater than zero")
            return
        odd_list1=get_odd_numbers_upto(limit)
        odd_list2=get_odd_numbers_step(limit)
        print(f"Odd numbers (method 1 - filter): {odd_list1}")
        print(f"Odd numbers (method 2 - step):   {odd_list2}")
    
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()

fruits = ["Apple", "Mango", "Banana", "Orange", "Kiwi"]
first_letters = [f[0].lower() for f in fruits]
print(first_letters)

            


