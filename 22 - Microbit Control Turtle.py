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
    
#CPU vs CPU    finish line at x=350
# turtle.tracer(False)  #manage the animation ourselves...
# while racer_a.xcor() < 350 and racer_b.xcor() < 350:
#     racer_a.fd(random.randint(4,6))
#     racer_b.fd(random.randint(4,6))
#     time.sleep(0.02) #50 fps
#     turtle.update() #refresh the screen after both moves are decided
# if racer_a.xcor() > racer_b.xcor():
#     print("Racer A wins!!")
# else:
#     print("Racer B wins!!")


last_move = "flat"

#HUMAN vs CPU
while racer_a.xcor() < 350 and racer_b.xcor() < 350:
    racer_a.fd(random.randint(2,3)) #CPU
    #Human Control - accelerometer, buttons
    
#     x = microbit.accelerometer.get_x()  #-1000 to 1000
#     speed = x/100
    
#     if microbit.button_a.was_pressed():
#         speed = 5
#     else:
#         speed = 1.5

#Challenge: "Handcars, Pump Trolley" Movement
#           move each time the microbit flips from Left to Right
#           or Right to Left
    current_move = horizontal_tilt(300) #"right" "left" "flat"
    if current_move != last_move and current_move != "flat":
        speed = 15
        last_move = current_move
    else:
        speed = 0
        
    racer_b.fd(speed)
    
wn.exitonclick()
    
    
    
    
    