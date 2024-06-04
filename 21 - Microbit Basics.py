# A look at the basic components
# User Input (buttons, microphone)
# Output (Speaker, LED Grid)
# Sensor (Accelerometer/Compass/Temp)

import microbit, time, random  #library for working with micro:bit

# DISPLAY TEXT (show, scroll)

#SHOW - once character at a time
# for letter in "SASKATCHEWAN":
#     microbit.display.show(letter)  #creates a static character on the grid
#     time.sleep(0.3)  #wait 0.3 seconds

#SCROLL - slide text right to left
# microbit.display.scroll("SASKATCHEWAN")


# BUTTON PRESSES
# a_presses = 0
# b_presses = 0
# while a_presses < 20 and b_presses < 20:
#     if microbit.button_a.is_pressed():
#         a_presses += 1
#         print(f"a: {a_presses} \t b: {b_presses}")
#     if microbit.button_b.was_pressed():
#         b_presses += 1
#         print(f"a: {a_presses} \t b: {b_presses}")

# ACCELEROMETER - orientation information
while True:
    x = microbit.accelerometer.get_x()  #ROLL
    if x < -300:
        print("LEFT")
    elif x > 300:
        print("RIGHT")
    else:
        print("FLAT")   
    #print(x)    # 0 - FLAT    > 300  RIGHT     < -300 LEFT
    time.sleep(0.05)
    
    
    
    
    
    
    

