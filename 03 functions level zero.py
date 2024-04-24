# Fortune Teller Simulator

# Function "lvl 0" - no inputs, no outputs
# Primary purpose is just for organization/reuse
import random

def fortune_one():
    # Simple function, to print out a fixed fortune
    print("Today will be a fortuitous day...")

def fortune_two():
    print("Don't step on a crack...")

def fortune_three():
    print("Your lucky number is 41")
 
#simulate rolling a 3-sided die, to randomly choose a fortune
chance = random.randint(0,2) #0, 1, 2
if chance == 0:
    fortune_one()
elif chance == 1:
    fortune_two()
else:
    fortune_three()