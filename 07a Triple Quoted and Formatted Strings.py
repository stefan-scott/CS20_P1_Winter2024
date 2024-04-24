# Triple Quoted and Formatted Strings
# Mr. Scott
# April 19, 2024
# A bit more about working with strings and data

# ----- First, Triple Quoted ------
# four ways to encapsule a string:
# ""   ''   """    '''
my_string = '''"How's it going", he said.'''
print(my_string)

my_string2 = """Down
Down
Down
Down..."""
print(my_string2)

#Escape Sequences
# \t → tab  \n → newline  \" → "  \' → '  \\
my_string3 = "ab\tc\'\n\"de\\f"
print(my_string3)

# Formatted String - joining string + variables
food = "apple"
sport = "soccer"
time_remaining = 20
my_string4 = f"""My Short Story.
It's time for an {food} break.
The {sport} game is nearly done.
There are {time_remaining} minutes left.
"""
print(my_string4)

a = "hello"
   # 01234
   #   -2-1



