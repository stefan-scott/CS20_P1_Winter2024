# Styling Output Text (Colors / Emojis)
import emoji  #library needs to be installed
from colorama import Fore, Back, Style

# Print out some strings with emojis
print(emoji.emojize("A banana :banana:"))
print(emoji.emojize(":snowboarder:  :frog:  :key:"))

# Next, Colorize
print(Fore.RED + "Red text" + Fore.BLUE + "Blue Text")
print(Back.BLACK + "Black background" + Back.YELLOW + "Yellow"+Back.RESET)
print(Style.DIM + "Dim" + Style.BRIGHT + "Bright" + Style.NORMAL + "Normal")