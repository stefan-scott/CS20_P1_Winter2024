# Functions Practice and Walking Turtles
# Mr. Scott
# June 10, 2024

import turtle, time, random
# Set up Turtle and Window

t = turtle.Turtle()
t.speed(0)
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
t.color(random.choice(colors))
speed = 10

wn = turtle.Screen()
wn.setup(600,600)

#Boolean Function to detect going "offscreen"
def is_on_screen(current_turtle):
    #check if this turtle is still on the canvas
    #return True is so, False if not.
    # Boolean Function: returns True or False
    if t.xcor() > -300 and t.xcor() < 300:
        if t.ycor() > -300 and t.ycor() < 300:
            return True
    return False
    
turtle.tracer(False) #turn off automatic animation
# Implement the Random Walker Algorithm
while True:
    roll = random.randint(0,3) #0, 1, 2, 3
    if roll == 0:
        t.setheading(0) #EAST
    elif roll == 1:
        t.setheading(90) #NORTH
    elif roll == 2:
        t.setheading(180) #WEST
    else:
        t.setheading(270) #SOUTH
    
    t.fd(speed)
    
    if not is_on_screen(t):
        #time to reset the turtle back to origin
        t.up()
        t.goto(0,0)
        t.down()
        t.color(random.choice(colors))
        speed = random.randint(2,10)
        
    turtle.update()





















# # S I G N A T U R E
# #     name   (parameter list)
# def triple_string(str):
#     # return the original string, tripled
#     # "abc" → "abcabcabc"
#     # str → string: the string to be tripled
#     return str*3
#         # return exits function, and sends
#         # data back to the line that called
#         # the function in the first place
# 
# result = triple_string("abc")
# print(result)
# print(triple_string("yxe"))
# print(triple_string(triple_string("a")))


