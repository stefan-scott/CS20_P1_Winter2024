# Rectangle Area Calculator  (title)
# Mr. Scott (name)
# April 11, 2024 (date)
# Practice using basic I/O + data conversions (1-line desc)

# Input + storing data in variables
#     ***INPUT ALWAYS GIVES US A STRING ***
#      string + string → join two strings together
#      string * string → TypeError
# if we want to do math, must convert str → int/float
# int()  str()   float()   bool()

width = input("Enter a width: ")  #width is a STRING
width = float(width)   #overwrites width with a FLOAT

height = input("Enter a height: ")
height = float(height)

# Output the result result back to the user

area = width * height
#        STR    +  FLOAT
print("Area is: " + str(area) + " units squared.")
