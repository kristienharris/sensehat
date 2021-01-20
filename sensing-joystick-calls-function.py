from sense_hat import SenseHat
from random import randint

sense = SenseHat()

# Define some functions for each direction
def red():
    sense.clear((255,0,0))
    
def green():
    sense.clear((0,255,0))
    
def blue():
    sense.clear((0,0,255))
    
def yellow(event):
    sense.clear((255,255,0))
                
def random_colour(event): # Functions triggered can have event passed to them
    r = randint(0,255)
    g = randint(0,255)
    b = randint(0,255)
    sense.clear((r,g,b))

    print(event) # Unformatted event data printed

    if event.action == 'pressed': # Using the event we can pretty print our own feedback
        print('You pressed me')
        if event.direction == 'up':
            print('Up')
        elif event.direction == 'down':
            print('Down')
    elif event.action == 'released':
        print('You released me')
    
    
# Tell the program which function to associate with which direction
# sense.stick.direction_up = red
# sense.stick.direction_down = blue
# sense.stick.direction_left = green
# sense.stick.direction_right = yellow
# sense.stick.direction_middle = sense.clear

# Use of the direction_any triggers all directions
sense.stick.direction_any = random_colour

while True:
    pass # This keeps the program runningto recieve joystick events
