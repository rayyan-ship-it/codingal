lower=int(input("enter the lower case number"))
upper=int(input("enter the upper case number"))
print("prime numbers between",lower,"and",upper,"are")
for i in range(lower,upper+1):
 if i>1:
  for x in range(2,i):
   if i%x==0:
    break
  else:
   print(i)
 