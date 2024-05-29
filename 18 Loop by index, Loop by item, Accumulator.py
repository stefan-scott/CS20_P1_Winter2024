# Looping by index VS Looping by item

transport = ["airplane", "bus", "car", "dogsled", "elevator"]
#               0          1      2        3         4
#               -5         -4    -3       -2        -1
# len(transport) → 5     range(len(transport)) = [0,1,2,3,4]

# LOOP BY ITEM.  Easy to code, but we don't have information
# about "where" the current item resides in the list.
# for method in transport:
#     print(f"you can travel by {method}")

# LOOP BY INDEX. A little longer to code, but we can still
# access each item, and we also know their list positions.
# for index in range(len(transport)): #[0,1,2,3,4...
#     method = transport[index]
#     print(f"item at pos: {index} is {method}")

# use the ACCUMULATOR PATTERN.
#     tries to solve a problem in small chunks.
#     start with an "empty" answer
#          then we add to it/refine it...over and over
#          hopefully by the end of the loop we have
#          correct answer

# Simple Example: "String Copy"
# Take an input string, loop by index, copy all
# characters into a new string...
def copy_string(str): 
    #1. accumulator, make a variable to hold answer
    result = ""
    for i in range(len(str)):
        current_letter = str[i]
        result = result + current_letter
    #when loop is done, we've accumulated correct result
    return result

print(copy_string("I hope this works..."))

# in keyword,  not in keyword
def is_vowel(ch):
    # Boolean Function - returns True if
    # given character is a vowel
    vowels = "aeiou"
    if ch in vowels:
        return True
    else:
        return False


# modulo division...
# i % 2 == 0   #is i even?
# i % 2 == 1   #is i odd?








