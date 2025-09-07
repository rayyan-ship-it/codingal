#finding the average speed of 3 cyclists
cyclist1=10
cyclist2=20
cyclist3=30
avg=cyclist1+cyclist2+cyclist3/3
print("average speed of cyclist is",avg)
if avg>cyclist1 and avg>cyclist2 and avg>cyclist3:
  print("the average speed is higher than all the riders ")
  if avg>cyclist1 and avg>cyclist2:
    print("the average speed is higher than two of the riders except rider3")
  if avg>cyclist2 and  avg>cyclist3:
    print("the rider1 is slow ")
  else:
    print("the cyclists are slow")
else:
  print("the cyclists speed is 0")
