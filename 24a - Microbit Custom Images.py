# Microbit Custom Images
# Mr. Scott
# June 6, 2024

import microbit, random

#0 - LED off      9 - LED full power
dice4 ="33333:"  \
       "39093:"  \
       "30003:"  \
       "39093:"  \
       "33333"
dice4 = microbit.Image(dice4)

dice1 ="33333:"  \
       "30003:"  \
       "30903:"  \
       "30003:"  \
       "33333"

dice1 = microbit.Image(dice1)

# Time to Roll!
while True:
    if microbit.button_a.was_pressed():
        choice = random.choice([1,4])
        if choice == 1:
            microbit.display.show(dice1)
        elif choice == 4:
            microbit.display.show(dice4)
        
        
        
        
        
        



