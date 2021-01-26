"""
Dice Roll
A small program to simulate the rolling of a 6 sided die
Activated by shaking the pi after the message is displayed
"""
from sense_hat import SenseHat
from random import randint
from time import sleep

sense = SenseHat()

# Colours
W = (255,255,255)
R = (255,0,0)
G = (0,255,0)
D = (0,0,0)

# Dice
dice = [
    [
    R,R,R,R,R,R,R,D,
    R,R,R,R,R,R,R,D,
    R,R,R,R,R,R,R,D,
    R,R,R,W,R,R,R,D,
    R,R,R,R,R,R,R,D,
    R,R,R,R,R,R,R,D,
    R,R,R,R,R,R,R,D,
    D,D,D,D,D,D,D,D,
    ],
    [
    R,R,R,R,R,R,R,D,
    R,W,R,R,R,R,R,D,
    R,R,R,R,R,R,R,D,
    R,R,R,R,R,R,R,D,
    R,R,R,R,R,R,R,D,
    R,R,R,R,R,W,R,D,
    R,R,R,R,R,R,R,D,
    D,D,D,D,D,D,D,D,
    ],
    [
    R,R,R,R,R,R,R,D,
    R,R,R,R,R,W,R,D,
    R,R,R,R,R,R,R,D,
    R,R,R,W,R,R,R,D,
    R,R,R,R,R,R,R,D,
    R,W,R,R,R,R,R,D,
    R,R,R,R,R,R,R,D,
    D,D,D,D,D,D,D,D,
    ],
    [
    R,R,R,R,R,R,R,D,
    R,W,R,R,R,W,R,D,
    R,R,R,R,R,R,R,D,
    R,R,R,R,R,R,R,D,
    R,R,R,R,R,R,R,D,
    R,W,R,R,R,W,R,D,
    R,R,R,R,R,R,R,D,
    D,D,D,D,D,D,D,D,
    ],
    [
    R,R,R,R,R,R,R,D,
    R,W,R,R,R,W,R,D,
    R,R,R,R,R,R,R,D,
    R,R,R,W,R,R,R,D,
    R,R,R,R,R,R,R,D,
    R,W,R,R,R,W,R,D,
    R,R,R,R,R,R,R,D,
    D,D,D,D,D,D,D,D,
    ],
    [
    R,R,R,R,R,R,R,D,
    R,W,R,R,R,W,R,D,
    R,R,R,R,R,R,R,D,
    R,W,R,R,R,W,R,D,
    R,R,R,R,R,R,R,D,
    R,W,R,R,R,W,R,D,
    R,R,R,R,R,R,R,D,
    D,D,D,D,D,D,D,D,
    ],
]

number_of_sides = 6
message_speed = 0.04
roll_speed = 0.15
play = True

def roll_dice_animation(time):
    for i in range(7):
        sense.set_pixels(dice[randint(0,number_of_sides - 1)])
        sleep(time)
    sleep(3)
    sense.clear(D)      

while True:
    sense.show_message("Shake to roll", message_speed, W)
    # Shake to fire die
    while play:      
        acceleration = sense.get_accelerometer_raw()
        
        x = acceleration['x']
        y = acceleration['y']
        z = acceleration['z']
        
        x = abs(x)
        y = abs(y)
        z = abs(z)
        
        # Shake logic
        if x > 1.2 or y > 1.2:
            # Roll the dice
            roll_dice_animation(roll_speed)
