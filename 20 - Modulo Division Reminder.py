# Quiz Practice
# Loops, Lists/Strings, Slicing

# Print out all of the numbers from 0 - 100
# which are evenly divisible by 4

# loop by item,  looping by index (for)  (while)
# modulo division:  (%)  "what is the remainder when i divide?"

num = 0
while num <= 100:
    if num % 4 == 0:  # divisible by 4
        print(num)
    num += 1

# Challenge: re-write using a for loop