things = []   #CREATION

for i in range(5):  #ADDITION
    user_thing = input("enter a thing: ")
    things.append(user_thing)
print(things)

for i in range(2):  #REMOAL 
    pos_to_remove = int(input(f"pos to delete (0-{len(things)-1})"))
    things.pop(pos_to_remove)

print(things)

#  "sask"   len ->  4
#   0123

# #LIST CREATION (empty list)
# fav_places = []
# 
# #MODIFY - addition
# fav_places.append("SK")
# fav_places.append("Iceland")
# fav_places.append("The Forest")
# fav_places.append("Ski Trails")
# 
# #Access - pos1, pos3
# print(fav_places[1])
# print(fav_places[3])
