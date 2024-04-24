# Functions with Inputs + Return Values
# Mr. Scott
# April 18, 2024
# Looking at functions and information passing

def add_three(num1, num2, num3):  #variable in brackets is a local variable
    # Takes three numbers, adds them together
    # num1, num2, num3 → integers/floats
   return num1 + num2 + num3
        # return exits the function → sends data back to the line
        # that called the function in the first place

sum1 = add_three(2,4,6)  #store result in variable
print(add_three(1,3,5))  #print result directly

    