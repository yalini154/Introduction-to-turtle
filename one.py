import turtle #importing library
turtle.Screen().bgcolor("blue")
turtle.Screen().setup(300,400)
square = turtle.Turtle() #defined variable


num_sides = 4 #variable
side_length = 70
angle = 360.0 / num_sides
#iterate loop for total number of side
for i in range(num_sides):
    square.forward(side_length)
    square.right(angle)
turtle.done()