# Microbit and Turtle Control
# Mr. Scott
# June 4, 2024
# Also: recap functions (param, return)

# tools → package manager → search: cs20-microbitio
import turtle, microbit, time, random

# Set up turtle(s)
racer_a = turtle.Turtle()
racer_a.color("blue")

racer_b = turtle.Turtle()
racer_b.color("red")

judge = turtle.Turtle()

wn = turtle.Screen()
wn.setup(800,400)

def horizontal_tilt(sensitivity):
    # return x-tilt state of the microbit (left, right, flat)
    # sensitivity → number used for tilt threshold
    x = microbit.accelerometer.get_x()
    if x < sensitivity *-1: #L
        return "left"
    elif x > sensitivity: #R
        return "right"
    else:
        return "flat"

#Set up the Race
judge.up()
judge.goto(350,-175)
judge.down()
judge.goto(350,175)

racer_a.up()
racer_a.shape("turtle")
racer_a.goto(-300,50)

racer_b.up()
racer_b.shape("turtle")
racer_b.goto(-300,-50)


#Conduct the Race
    
#CPU vs CPU
for i in range(100):
    racer_a.fd(random.randint(4,6))
    racer_b.fd(random.randint(4,6))



wn.exitonclick()
    
    
    
    
    