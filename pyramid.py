print("the pyramid will be right angled")
n=int(input("enter the rows required"))
for i in range(n):
 for j in range(i+1):
    print("*",end="")
 print()