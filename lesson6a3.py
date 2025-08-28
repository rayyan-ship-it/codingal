height=int(input("enter the height in cms"))
weight=int(input("enter the weight in kgs"))
BMI= weight/ (height/100)**2
if BMI<=18:
    print("you are underweight")
elif BMI<=24:
    print("you are in a healthy range")
elif BMI<=29:
    print("you are not in the healthy range")
elif BMI<=34:
    print("you are overweight")
elif BMI<=39:
    print("you are severely obese")
else:
    print("your medical condition is very critical")
