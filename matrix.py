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
def pick_random_colour():
    random_red = randint(0,255)
    random_green = randint(0,255)
    random_blue = randint(0,255)
    return (random_red, random_green, random_blue)

message = "I love Sazz"



# Clears display and shows all white
sense.clear(white)

time.sleep(3)

# Shows a message on the display and loops it forever
# while True:
# 	sense.show_message(message,
# 						text_colour = red,
# 						back_colour = blue,
# 						scroll_speed = .5)

sense.show_message(message,
                    text_colour = red,
                    back_colour = blue,
                    scroll_speed = .05)

# Shows a single caracter
sense.show_letter("K", text_colour = red, back_colour = yellow)
sleep(1)
sense.show_letter("r", blue, yellow)
sleep(.5)
sense.show_letter("i", red)
sleep(.5)
sense.show_letter("s", yellow)
sleep(.5)

sense.clear(dark)

sense.show_letter("H", pick_random_colour(), pick_random_colour())
sleep(1)
sense.show_letter("a",  pick_random_colour())
sleep(.5)
sense.show_letter("r",  pick_random_colour())
sleep(.5)
sense.show_letter("r",  pick_random_colour())
sleep(.5)
sense.show_letter("i",  pick_random_colour())
sleep(.5)
sense.show_letter("s",  pick_random_colour())
sleep(.5)

sense.clear()

# Target indiviual led pixels on the matrix using x y coordinates
# Four corners
sense.set_pixel(0, 0, red)
sense.set_pixel(0, 7, yellow)
sense.set_pixel(7, 0, blue)
sense.set_pixel(7, 7, green)

sleep(3)

sense.clear()



# Smiley Face
sense.set_pixel(2, 2, (0, 0, 255))
sense.set_pixel(4, 2, (0, 0, 255))
sense.set_pixel(3, 4, (100, 0, 0))
sense.set_pixel(1, 5, (255, 0, 0))
sense.set_pixel(2, 6, (255, 0, 0))
sense.set_pixel(3, 6, (255, 0, 0))
sense.set_pixel(4, 6, (255, 0, 0))
sense.set_pixel(5, 5, (255, 0, 0))

sleep(3)

sense.clear()

# Smiley Face
sense.set_pixel(1, 1, (0, 0, 255))
sense.set_pixel(5, 1, (0, 0, 255))
sense.set_pixel(3, 3, (100, 0, 0))
sense.set_pixel(2, 5, (255, 0, 0))
sense.set_pixel(3, 5, (255, 0, 0))
sense.set_pixel(4, 5, (255, 0, 0))
sense.set_pixel(1, 6, (255, 0, 0))
sense.set_pixel(5, 6, (255, 0, 0))

sleep(3)

# Set multiple pixels at once
# Define some colours
g = (0, 255, 0) # Green
b = (0, 0, 0) # Black

# Set up where each colour will display
creeper_pixels = [
    g, g, g, g, g, g, g, g,
    g, g, g, g, g, g, g, g,
    g, b, b, g, g, b, b, g,
    g, b, b, g, g, b, b, g,
    g, g, g, b, b, g, g, g,
    g, g, b, b, b, b, g, g,
    g, g, b, b, b, b, g, g,
    g, g, b, g, g, b, g, g
]

# Display these colours on the LED matrix
sense.set_pixels(creeper_pixels)

sleep(3)
sense.clear()

# Show random coloured matrix

random_matrix = [
    pick_random_colour(), pick_random_colour(), pick_random_colour(), pick_random_colour(), pick_random_colour(), pick_random_colour(), pick_random_colour(), pick_random_colour(),
    pick_random_colour(), pick_random_colour(), pick_random_colour(), pick_random_colour(), pick_random_colour(), pick_random_colour(), pick_random_colour(), pick_random_colour(),
    pick_random_colour(), pick_random_colour(), pick_random_colour(), pick_random_colour(), pick_random_colour(), pick_random_colour(), pick_random_colour(), pick_random_colour(),
    pick_random_colour(), pick_random_colour(), pick_random_colour(), pick_random_colour(), pick_random_colour(), pick_random_colour(), pick_random_colour(), pick_random_colour(),
    pick_random_colour(), pick_random_colour(), pick_random_colour(), pick_random_colour(), pick_random_colour(), pick_random_colour(), pick_random_colour(), pick_random_colour(),
    pick_random_colour(), pick_random_colour(), pick_random_colour(), pick_random_colour(), pick_random_colour(), pick_random_colour(), pick_random_colour(), pick_random_colour(),
    pick_random_colour(), pick_random_colour(), pick_random_colour(), pick_random_colour(), pick_random_colour(), pick_random_colour(), pick_random_colour(), pick_random_colour(),
    pick_random_colour(), pick_random_colour(), pick_random_colour(), pick_random_colour(), pick_random_colour(), pick_random_colour(), pick_random_colour(), pick_random_colour(), 
]

sense.set_pixels(random_matrix)

sleep(3)

# Rotate and flip sense hat display

sense.show_letter("K")

sleep(1)

sense.set_rotation(180)

sleep(2)

sense.flip_h()

sleep(2)

sense.flip_v()

sleep(2)

# Create simple animation by repeat flipping
sense.set_pixels(random_matrix)
while True:
    sleep(1)
    sense.flip_h()
    sense.flip_v()
