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
    
    
    
    
    
    
    