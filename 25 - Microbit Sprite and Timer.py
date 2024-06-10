# Microbit Sprite and Timer
# Mr. Scott
# June 7, 2024

#Re-use our Microbit image "library" functions...
import microbit, time, random

#2D List
grid = [ [0, 0, 0, 0, 0], 
         [0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0] ]

# LED Helper Functions
def print_grid():
    #print out the contents of grid (easy-to-read)
    for row in grid:
        print(row)

def show_grid():
    #convert our 2D list into a string, and display
    result = ""
    for row in grid:
        for pixel in row:
            result = result + str(pixel)
        result = result + ":"
    result = result[0:-1]
    print(result)
    microbit.display.show(microbit.Image(result))

def set_pixel(x,y,intensity):
    # set pixel at (x,y) to brightness: intensity (0-9)
    grid[y][x] = intensity
    show_grid()
    
def plot(x,y):
    # full power pixel at x,y
    set_pixel(x,y,9)
    
def unplot(x,y):
    # remove pixel at x,y
    set_pixel(x,y,0)

def queue_pixel(x,y,intensity):
    # update grid at x,y without redrawing the screen
    grid[y][x] = intensity
    
def set_all(intensity):
    #turn all pixels to a particular intensity
    for x in range(5):  #0,1,2,3,4
        for y in range(5):  #0,1,2,3,4
            queue_pixel(x,y,intensity)
    show_grid()



# --------------------------------------- #
#        Today's Demo Starts Here         #
# --------------------------------------- #

# Movable Character
show_grid()  # clear the screen

player_x = 2
player_y = 2

plot(player_x, player_y)

while True: # main loop / game loop
    queue_pixel(player_x, player_y,0)
    x = microbit.accelerometer.get_x() #-1000  1000
    if x < -300: # LEFT
        player_x -= 1
        if player_x < 0:  #constrains to min
            player_x = 0
    
    elif x > 300: # RIGHT
        player_x += 1
        if player_x > 4:
            player_x = 4 #constrain to max
    
    y = microbit.accelerometer.get_y()
    if y < -300: #forward
        player_y -= 1
        if player_y < 0:
            player_y = 0
        
    if y > 300: #backward
        player_y +=1
        if player_y > 4:
            player_y = 4
    plot(player_x, player_y)
    time.sleep(0.01)