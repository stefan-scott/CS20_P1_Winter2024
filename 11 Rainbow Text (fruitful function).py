# Rainbow Text Generator
# Mr. Scott
# April 26, 2024
# A recap on functions with inputs and
# return values...

from colorama import Fore, Back, Style #modify text color, highlight color, style

def rainbow_text(src_text):
    # src_text → string to apply a rainbow coloring to
    foregrounds = [Fore.RED, Fore.YELLOW, Fore.GREEN, Fore.BLUE, Fore.MAGENTA] 
    #                 0           1            2          3        4             len(foregrounds)
    color_index = 0 
    result_text = Back.BLACK + Style.BRIGHT
    for letter in src_text:
        result_text += foregrounds[color_index]
        result_text = result_text + letter
        # advance color_index to the next value
        color_index += 1
        if color_index >= len(foregrounds):
            color_index = 0
    result_text += Back.RESET
    return result_text

#Test out our function
print(rainbow_text("Here is some testing text to turn into a rainbow style"))
    





def func_a(a, b, c):
    # a, b, c → string inputs
    # joins a,b,c and prints the result
    # non-fruitful function
    print(f"{a}{b}{c}")

def func_b(a, b, c):
    # same as above, but returns the result
    # this time, fruitful function
    return (f"{a}{b}{c}")

# func_a("a","b","c")  #prints "abc"
# result = func_b("a","b","c")