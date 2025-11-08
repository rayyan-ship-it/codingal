#using try and except
try:
    number=int(input("enter the number"))
    print("the value of the number is",number)
except ValueError as d:
    print("exception:",d)