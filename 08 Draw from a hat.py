#Get a random item from in a list
import random

nouns = []
verbs = []

occupations = ["","",""]
fruit = ["apple", "banana", "cantaloupe", "durien"]
#           0        1           2           3 (len-1)
#           -4       -3          -2         -1

length_of_list = len(fruit)  #len() tells us how many items

# way one: generate random index
# index = random.randint(0, length_of_list-1)  #0 to (len-1)
# print(fruit[index])

# way two:
item = random.choice(fruit) #picks an item at random from list
print(item)