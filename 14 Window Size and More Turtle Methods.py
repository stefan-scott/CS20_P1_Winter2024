# Window Size + More Turtle Methods
# Mr. Scott
# May 3, 2024
# .setup() method, penup(), pendown(), stamp(), shape()

# Turlte Setup Code

import turtle, random

window = turtle.Screen()
window.setup(1200, 600)  #(width, height)

francis = turtle.Turtle()
francis.color("blue")

def hollow_c(my_turtle):
    long = 150
    short = 30
    for i in range(3):
        my_turtle.fd(long)
        my_turtle.left(90)
    
    my_turtle.fd(short)
    my_turtle.left(90)
    
    my_turtle.fd(long-short)
    my_turtle.right(90)
    
    my_turtle.fd(long- (short*2))
    my_turtle.right(90)
    
    my_turtle.fd(long-short)
    my_turtle.left(90)
    
    my_turtle.fd(short)
    my_turtle.left(90) #return to our starting angle
    
francis.speed(0)
for i in range(120):
    hollow_c(francis)
    francis.left(3)







# Example One - penup, pendown, stamp, shape
# francis.shape("turtle")
# francis.penup()  #penup() | up()
# francis.speed(0)
# 
# for i in range(1000):
#     francis.stamp()  #leave an 'impression' of turtle
#     x = random.randint(-600,600) #depends on canvas size
#     y = random.randint(-300,300)
#     francis.goto(x,y)

window.exitonclick()


