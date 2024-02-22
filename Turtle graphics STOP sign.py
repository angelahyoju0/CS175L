#Angela An
#Stop Sign
#CS 175L
#Professor Eckert

import math
import turtle

#Names constants
window_width = 400
window_height = 400
num_sides = 8
length = 115
angle = 45

# Size the window
turtle.setup(window_width, window_height)

# Initialize the turtle
turtle.penup()
turtle.goto(-50,100)
turtle.pendown()
turtle.shape('turtle')

turtle.pensize(10)
turtle.color('red')
turtle.begin_fill()


for stop in range(num_sides):
    turtle.pendown()
    turtle.forward(length)
    turtle.right(angle)
turtle.end_fill()

length = 100

turtle.pensize(12)
turtle.goto(-43,84)
turtle.color('white')
turtle.fillcolor('red')
turtle.begin_fill()

for stop in range(num_sides):
    turtle.pendown()
    turtle.forward(length)
    turtle.right(angle)
turtle.end_fill()

turtle.penup()
turtle.goto(-65, -70)
turtle.color("white")
turtle.write("STOP", font=("Arial",55, 'bold'))
turtle.hideturtle()
