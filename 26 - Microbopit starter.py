# Micro:bop:it Starter
# Mr. Scott
# June 13, 2024

import microbit, time, random

# Set up action-related data
choices = ["A", "B", "S"]  #later, add L / R
target_action = random.choice(choices)

# Set up time-related data
start_time = time.time()
time_limit = 2 #amount of seconds to complete action

while True:
    elapsed_time = time.time() - start_time
    
    # Show target action on micro:bit
    if target_action == "S":
        microbit.display.show(microbit.Image.SKULL)
    else:
        microbit.display.show(target_action)
    
    # Check for a user action (A, B, ← , → )
    # 1. check for a SHAKE
    motion = microbit.accelerometer.get_z()
    if motion > 1300 or motion < -1300:
        print("SHAKE")
        time.sleep(0.5) #no shake buffer time
        
        #Now, determine if this action was correct
        if target_action == "S":
            # user was correct. Display an animation/icon
            # showing they were right...
            print("Correct")
            target_action = random.choice(choices)
            start_time = time.time() #reset timer to 0
            # increase our score by 1.
        else:
            # user made a mistake...game over
            print("Incorrect - Game over")
            break
        
    #2. Check for Button A press
    
    #3. Check for Button B press
        
    #4. Check for left tilt
        
    #5. Check for right tilt
        
    #6. Check if the user is out of time...
            
            
            
        
    
    
    
    
    
    
    
    
    
    