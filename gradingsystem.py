
mark1=int(input("enter the marks out of 100"))
mark2=int(input("enter the marks out of 100"))
mark3=int(input("enter the marks out of 100"))
mark4=int(input("enter the marks out of 100"))
mark5=int(input("enter the marks out of 100"))
average=(mark1+mark2+mark3+mark4+mark5)/5
if average>=90 and average<98:
    print("your grade is A1")
elif average>=85 and average<89:
    print("your grade is A2")
elif average>=75 and average<84:
    print("your grade is B2")
elif average>=68 and average<74:
    print("your grade is B1")
elif average>=55 and average<58:
    print("your grade is C1")
elif average>=50 and average<55:
    print("your grade is C2")
else:
    print("your marks are not good")