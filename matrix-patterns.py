# A program to try out pixel art for the pi sense hat
# Use the matrix template svg as a starting point for design

from sense_hat import SenseHat
from time import sleep
from random import randint
import time 
sense = SenseHat()

dark = (0,0,0)
white = (255,255,255)
red = (255,0,0)
green = (0,255,0)
blue = (0,0,255)
yellow = (255,255,0)

# Function to generate random colour
def random_colour():
    random_red = randint(0,255)
    random_green = randint(0,255)
    random_blue = randint(0,255)
    return (random_red, random_green, random_blue)

cheese = 1

# Clears display and shows all white
sense.clear(white)
time.sleep(1)

# Set a random matrix of colours
H = random_colour()
matrix = [
    H,H,H,H,H,H,H,H,
    H,H,H,H,H,H,H,H,
    H,H,H,H,H,H,H,H,
    H,H,H,H,H,H,H,H,
    H,H,H,H,H,H,H,H,
    H,H,H,H,H,H,H,H,
    H,H,H,H,H,H,H,H,
    H,H,H,H,H,H,H,H,
    ]
sense.set_pixels(matrix)
sleep(cheese)

# Tick
H = dark
X = green
matrix_tick = [
    H,H,H,H,H,H,H,H,
    H,H,H,H,H,H,H,X,
    H,H,H,H,H,H,X,H,    
    H,H,H,H,H,X,H,H,
    X,H,H,H,X,H,H,H,
    H,X,H,X,H,H,H,H,
    H,H,X,H,H,H,H,H,    
    H,H,H,H,H,H,H,H,
    ]
sense.set_pixels(matrix_tick)
sleep(cheese)

# Cross
X = red
matrix_cross = [
    H,H,H,H,H,H,H,H,
    X,H,H,H,H,H,X,H,
    H,X,H,H,H,X,H,H,    
    H,H,X,H,X,H,H,H,
    H,H,H,X,H,H,H,H,
    H,H,X,H,X,H,H,H,
    H,X,H,H,H,X,H,H,    
    X,H,H,H,H,H,X,H,
    ]
sense.set_pixels(matrix_cross)
sleep(cheese)


# Smiley
H = dark
X = green
matrix_smiley = [
    H,H,H,H,H,H,H,H,
    H,H,H,H,H,H,H,H,
    H,H,X,H,H,X,H,H,
    H,H,H,H,H,H,H,H,
    H,X,H,H,H,H,X,H,
    H,H,X,X,X,X,H,H,
    H,H,H,H,H,H,H,H,
    H,H,H,H,H,H,H,H,
    ]
sense.set_pixels(matrix_smiley)
sleep(cheese)

# Unhappy
H = dark
X = red
matrix_unhappy = [
    H,H,H,H,H,H,H,H,
    H,H,H,H,H,H,H,H,
    H,H,X,H,H,X,H,H,
    H,H,H,H,H,H,H,H,
    H,H,H,H,H,H,H,H,
    H,H,X,X,X,X,H,H,
    H,X,H,H,H,H,X,H,
    H,H,H,H,H,H,H,H,
    ]
sense.set_pixels(matrix_unhappy)
sleep(cheese)

# Show random coloured matrix
while True:
    random_matrix = [
        random_colour(),random_colour(),random_colour(),random_colour(),random_colour(),random_colour(),random_colour(),random_colour(),
        random_colour(),random_colour(),random_colour(),random_colour(),random_colour(),random_colour(),random_colour(),random_colour(),
        random_colour(),random_colour(),random_colour(),random_colour(),random_colour(),random_colour(),random_colour(),random_colour(),
        random_colour(),random_colour(),random_colour(),random_colour(),random_colour(),random_colour(),random_colour(),random_colour(),        
        random_colour(),random_colour(),random_colour(),random_colour(),random_colour(),random_colour(),random_colour(),random_colour(),
        random_colour(),random_colour(),random_colour(),random_colour(),random_colour(),random_colour(),random_colour(),random_colour(),
        random_colour(),random_colour(),random_colour(),random_colour(),random_colour(),random_colour(),random_colour(),random_colour(),
        random_colour(),random_colour(),random_colour(),random_colour(),random_colour(),random_colour(),random_colour(),random_colour(),
        ]
    sense.set_pixels(random_matrix)
    sleep(1)
    sense.flip_h()
    sleep(1)
    sense.flip_v()
