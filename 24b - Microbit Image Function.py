# Microbit LED Functions
# Mr. Scott
# June 6, 2024

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


# Try some animations!
# 1. Fading Animation
while True:
    #fade in:
    for i in range(10):  #0, 1, 2, 3, 4, 5, 6, 7, 8, 9
        set_all(i)
        time.sleep(0.05)
    for i in range(8, 0, -1):   #8, 7, 6, 5, 4, 3, 2, 1
        set_all(i)
        time.sleep(0.05)
