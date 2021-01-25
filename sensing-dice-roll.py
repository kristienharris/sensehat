"""
Roll the Dice
A sense hat guessing game where you guess which number will be rolled.
Based on Codecademy Lesson - Learn Python 2
"""
from sense_hat import SenseHat
from random import randint, uniform
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
    for i in range(randint(1,3)):
        for side in dice:
            sense.set_pixels(dice[randint(0,number_of_sides - 1)])
            sleep(time)

while True:
    sense.show_message("Shake to roll", message_speed, W)
    # Shake to fire your die
    while play:      
        acceleration = sense.get_accelerometer_raw()
        
        x = acceleration['x']
        y = acceleration['y']
        z = acceleration['z']
        
        x = abs(x)
        y = abs(y)
        z = abs(z)
        
        if x > 1.2 or y > 1.2 or z > 1.2:
            # Roll the dice
            roll_dice_animation(roll_speed)
