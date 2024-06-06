# Microbit Images and Animation
# Mr. Scott
# June 5th, 2024
# Looking at the built-in Images


# install library:  Tools → Package Manager → cs20-microbitio
# "Could not get a prompt":  press physical reset button. run

import microbit, time
print(microbit.Image.STD_IMAGE_NAMES)

# Put an Image on the display:  use SHOW
microbit.display.show(microbit.Image.SNAKE)

# Loop through all clock images to animate
# for current_hour in microbit.Image.ALL_CLOCKS:
#     microbit.display.show(current_hour)
#     time.sleep(0.2)

# Continual Animation + Speed Control
# image list has 12 images   0-11, 12
current_index = 0
animation_delay = 0.1   #0.01 - 0.4
while True:
    clock_image = microbit.Image.ALL_CLOCKS[current_index]
    microbit.display.show(clock_image)
    current_index += 1
    if current_index > 11: #time to wrap around
        current_index = 0
    
    if microbit.button_a.is_pressed():
        animation_delay -= 0.01
        if animation_delay < 0.01: #check for min
            animation_delay = 0.01
            
    if microbit.button_b.is_pressed():
        animation_delay += 0.01
        if animation_delay > 0.4:  #check for max
            animation_delay = 0.4
        
    time.sleep(animation_delay)
