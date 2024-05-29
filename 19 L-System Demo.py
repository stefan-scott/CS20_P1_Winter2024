# L-System Demo
# Mr. Scott
# May 29, 2024

# Turtle Setup Code Here...
import turtle
t = turtle.Turtle()    #creation of Turtle and Screen
wn = turtle.Screen()
wn.setup(700,700)

t.speed(0)     #set the speed

t.up()            #move to initial position
t.goto(-350,0)
t.down()

turtle.tracer(False) #turns OFF animation

# Define L-System Here...

def apply_rules(ch):
    #Apply our L-System Rules to a single character
    if ch == "F":
        return "F-F++F-F"
#     elif ch == "B":
#         return "AB"
    else: #if there is no rule to match ch
        return ch

def process_string(original_str):   # "ABBA"
    # Use accumulator pattern to compute the next generation
    # one character at a time
    next_str = ""
    for c in original_str:
        next_str = next_str + apply_rules(c)
    return next_str
    
def create_L_system(num_generations, axiom):
    #Run the L-system for a set number of generations
    start_string = axiom
    end_string = ""
    for i in range(num_generations):
        end_string = process_string(start_string)    
        start_string = end_string
    return end_string
    
# Time to drive the Turtle
def draw_L_system(instructions, angle, distance):
    #interpret our L-system with the Turtle
    for cmd in instructions:
        if cmd == "F":
            t.fd(distance)
        elif cmd == "B":
            t.bk(distance)
        elif cmd == "+":
            t.rt(angle)
        elif cmd == "-":
            t.lt(angle)
    
#MAIN CODE HERE
commands = create_L_system(6, "F")
print(commands)
draw_L_system(commands, 60, 3)

turtle.update()    #redraw the screen        
    