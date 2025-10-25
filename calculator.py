def add(a,b):
    return a+b
def subtract(a,b):
    return a-b
def multiply(a,b):
    return a*b
def divide(a,b):
    return a/b
print("select the output")
print("a.add the number")
print("b.subtract the number")
print("c.multiplication")
print("d.division")
choice = input("select the choice:")
num1=int(input("enter the number"))
num2=int(input("enter the second number"))
if choice=="a":
    print(num1,"+",num2,"=",add(num1,num2))
elif choice=="b":
    print(num1,"-",num2,"=",subtract(num1,num2))
elif choice=="c":
    print(num1,"*",num2,"=",multiply(num1,num2))
elif choice=="d":
    print(num1,"/",num2,"=",divide(num1,num2))
else:
    print("invalid input")