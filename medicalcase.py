medicalcase=input("if the medical condition is yes or no")
attendance=int(input("enter your attendance"))
if medicalcase=="yes":
    print("you are allowed")
else:
    if  medicalcase.strip()=="no" and attendance>=75:
        print("you are allowed in the campus")
    else:
        print("invalid student")


 
