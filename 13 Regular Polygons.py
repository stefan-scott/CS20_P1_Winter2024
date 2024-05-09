# Regular Polygons
# Mr. Scott
# April 30, 2024
# Looking for Patterns + drawing with turtle

# Turtle Boilerplate/Setup
import turtle, random

window = turtle.Screen() #create a window
#window.bgcolor("yourColorHere")

roscoe = turtle.Turtle() #create a turtle
roscoe.pensize(3)       #line thickness
# roscoe.speed(0)         #fast animation
roscoe.color("coral")   #line color

anna = turtle.Turtle()
anna.color("blue")

# Functions
def triangle():
    for i in range(3):  #repeat 3
        roscoe.fd(100)
        roscoe.left(120)

def square(my_turtle, length):
    # my_turtle → a turtle object
    # length → integer: length of each side
    for i in range(4):
        my_turtle.fd(length)
        my_turtle.left(90)

def pentagon(my_turtle, length):
    # my_turtle → a turtle object
    # length → integer: length of each side
    for i in range(5):
        my_turtle.fd(length)
        my_turtle.left(72)

def r_poly(my_turtle, num_sides, length):
    # my_turtle → a turtle object
    # num_sides → integer: number of polygon sides
    # length → integer: length of each side
    for i in range(num_sides):
        my_turtle.fd(length)
        my_turtle.left(360/num_sides)

# Main Code Here
anna.speed(0)
for n in range(3, 50): #[3, 4, 5, 6, ..., 19]
    r_poly(anna, n, 20)

# for i in range(50,150,10): #[50, 60, 70, 80..., 140]
#     pentagon(roscoe, i)

# triangle()
 
# square(roscoe, 150)
# square(anna, 75)




# End our program
window.exitonclick()
