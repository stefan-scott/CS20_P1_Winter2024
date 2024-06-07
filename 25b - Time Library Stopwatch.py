# Microbit and Timer

import random, microbit, time

# time.time() → # of sec
# since Jan 1, 1970   EPOCH
stopwatch_start = time.time()  #5 10
while True:
    stopwatch_current = time.time() # 5 6 7 8 9 10
    elapsed_time = stopwatch_current - stopwatch_start
    print(f"That was {elapsed_time} seconds")
    if microbit.button_a.was_pressed(): #RESET
        stopwatch_start = time.time()
        print("RESET")
    time.sleep(0.1)