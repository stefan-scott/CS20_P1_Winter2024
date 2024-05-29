# L-System Demo
# Mr. Scott
# May 29, 2024

# Turtle Setup Code Here...



# Define L-System Here...

def apply_rules(ch):
    #Apply our L-System Rules to a single character
    if ch == "A":
        return "B"
    elif ch == "B":
        return "AB"
    else: #if there is no rule to match ch
        return ch

def process_string(original_str):   # "ABBA"
    # Use accumulator pattern to compute the next generation
    # one character at a time
    next_str = ""
    for c in original_str:
        next_str = next_str + apply_rules(c)
    return next_str
    
    
    
    