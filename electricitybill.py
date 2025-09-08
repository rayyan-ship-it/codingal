#checking the tax for given electricity bill
units=int(input("enter the units consumed"))
print("since the units used is",units)
if units<=50:
    charge=25
    perunit=2.60
    supercharge=(units*2.6)+25
    print("the supercharge will be",supercharge)
elif units>50 and units<=100:
    charge=35
    perunit=3.25
    supercharge=(units*3.25)+35
    print("the supercharge will be",supercharge)
elif units>100 and units<=200:
    charge=45
    perunit=5.26
    supercharge=(units*5.26)+45
    print("the supercharge will be",supercharge)
else:
    units>200
    charge=75
    perunit=8.45
    supercharge=(units*8.45)+75
    print("the supercharge will be,supercharge",supercharge)  
