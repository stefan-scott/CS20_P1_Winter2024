# Loop-and-a-half Demo
# Mr. Scott
# April 17,2024
# "Forever" Loop, break, continue

# create an infinite loop
while True:  #infinite loop
    choice = input("Stop the loop? [yes/no]") #yes Yes YES YEs
    if choice.lower() == "yes":
        confirm = input("You sure? [yes/no]")
        if confirm.upper() == "YES":
            break   # exits the current loop
        else:
            continue #'restarts' the loop...
                     # it goes immediately to the next iteration
    print("let's ask again...")