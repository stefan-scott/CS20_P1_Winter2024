# - Work on Turtle Confusion

# - Coding Bats:
#    Pick 2 exercises to try
#    cs20.ca → second Boolean Expression Practice Quiz


# Functions and Variable Scope

my_num = 5  # Global Variable

def add_ten(n):
    result = n + 10
    return result

my_num = add_ten(my_num)
print(my_num)

# We can access globals from in a function
# but NOT modify

# my_num = 5  #global variable
# 
# def add_ten():
#     my_num = 99  #local variable
#     print(f"my_num: {my_num}")
#     #my_num = my_num + 10   #
# 
# add_ten()
# print(my_num)



# Accessing local var after function...doesn't work.

# def add_ten():  #no inputs, no return
#     my_num = 5   #local variable
#     my_num = my_num + 10
# 
# add_ten()
# print(my_num)

