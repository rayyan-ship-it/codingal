import turtle
turtle.Screen().bgcolor("red")
turtle.Screen().setup(300,400)
polygon=turtle.Turtle()

num_sides=8
side=70
angle=360/num_sides
for i in range(num_sides):
    polygon.forward(side)
    polygon.right(angle)
turtle.done()