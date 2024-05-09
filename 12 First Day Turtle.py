# First Day Turtle
# Mr. Scott
# April 29, 2024
# Basics of Turtle Graphics: movement, color, etc...
#
# NOTE: do NOT save your work as turtle.py

import turtle #looks for a file named "turtle.py" and loads it

# boilerplate code → "startup code for working with turtle"
window = turtle.Screen()
window.bgcolor("lightgreen")


my_turtle = turtle.Turtle() #creates a turtle object, stores in var
my_turtle.color("FireBrick")
my_turtle.pensize(5)
my_turtle.speed(0) #speed 0 is "max" animation speed

# PROGRAM THREEE
import random

colors = ["FireBrick", "MidnightBlue", "PapayaWhip", "Snow" ]
moves = 280
for distance in range(moves): #[0, 1, 2, 3, ...,moves-1]
    my_turtle.color(random.choice(colors))
    my_turtle.forward(distance)
    my_turtle.left(45)

# PROGRAM TWO - a few more instructions
# my_turtle.fd(50)  #.fd() is short for forward()
# my_turtle.lt(37)  #.lt() is short for left()
# my_turtle.fd(202)
# my_turtle.goto(0,0)  #return to origin with goto()


# PROGRAM ONE - basic movement
# my_turtle.forward(100)   # move forward 100 units (pixels)
# my_turtle.right(45)      # turn right 45 degrees
# my_turtle.backward(200)  # backward 200 units


# program end (optional)
window.exitonclick()  # loop waiting for user to click on canvas