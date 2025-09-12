print("they are two different types of vehicles")
print("cars and bikes")
print("1.bikes")
print("2.cars")
choice=int(input("enter your choice"))
if choice==1:
    print("1.scooty?")
    print("2.scooter?")
    choice2=int(input("enter your choice for type of bike"))
    if choice2==1:
        print("you have selected scooty")
    else:
        print("you have seleceted scooter ")
elif choice==2:
    print("1.suv")
    print("2.sedan")
    choice3=int(input("enter you car type"))
    if choice3==1:
        print("you have selceted suv")
    else:
        print("you have selected sedan")
else:
    print("invalid input") 


     

    
