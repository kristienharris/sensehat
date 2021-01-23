"""
Roll the Dice
A sense hat guessing game where you guess which number will be rolled.
Based on Codecademy Lesson - Learn Python 2
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
dice_1 = [
    R,R,R,R,R,R,R,R,
    R,R,R,R,R,R,R,R,
    R,R,R,R,R,R,R,R,
    R,R,R,W,W,R,R,R,
    R,R,R,W,W,R,R,R,
    R,R,R,R,R,R,R,R,
    R,R,R,R,R,R,R,R,
    R,R,R,R,R,R,R,R,
    ]
dice_2 = [
    R,R,R,R,R,R,R,R,
    R,W,W,R,R,R,R,R,
    R,W,W,R,R,R,R,R,
    R,R,R,R,R,R,R,R,
    R,R,R,R,R,R,R,R,
    R,R,R,R,R,W,W,R,
    R,R,R,R,R,W,W,R,
    R,R,R,R,R,R,R,R,
    ]
dice_3 = [
    R,R,R,R,R,R,R,R,
    R,R,R,R,R,W,W,R,
    R,R,R,R,R,W,W,R,
    R,R,R,W,W,R,R,R,
    R,R,R,W,W,R,R,R,
    R,W,W,R,R,R,R,R,
    R,W,W,R,R,R,R,R,
    R,R,R,R,R,R,R,R,
    ]
dice_4 = [
    R,R,R,R,R,R,R,R,
    R,W,W,R,R,W,W,R,
    R,W,W,R,R,W,W,R,
    R,R,R,R,R,R,R,R,
    R,R,R,R,R,R,R,R,
    R,W,W,R,R,W,W,R,
    R,W,W,R,R,W,W,R,
    R,R,R,R,R,R,R,R,
    ]
dice_5 = [
    R,R,R,R,R,R,R,R,
    R,W,W,R,R,W,W,R,
    R,W,W,R,R,W,W,R,
    R,R,R,W,W,R,R,R,
    R,R,R,W,W,R,R,R,
    R,W,W,R,R,W,W,R,
    R,W,W,R,R,W,W,R,
    R,R,R,R,R,R,R,R,
    ]

dice_6 = [
    R,R,R,R,R,R,R,R,
    R,W,W,R,R,W,W,R,
    R,R,R,R,R,R,R,R,
    R,W,W,R,R,W,W,R,
    R,W,W,R,R,W,W,R,
    R,R,R,R,R,R,R,R,
    R,W,W,R,R,W,W,R,
    R,R,R,R,R,R,R,R,
    ]

# Game variables
guess = 1
number_of_sides = 6
max_val = 12
speed = 0.05
play = True

sense.set_pixels(dice_1)
sleep(.2)
sense.set_pixels(dice_2)
sleep(.2)
sense.set_pixels(dice_3)
sleep(.2)
sense.set_pixels(dice_4)
sleep(.2)
sense.set_pixels(dice_5)
sleep(.2)
sense.set_pixels(dice_6)
sleep(.2)

# Introduction to game and rules
# sense.show_message("Guess total roll dice. 1 - %d. Up or down to guess. Shake to play."  % max_val, speed, W)

while True:
    # Get dice rolls
    first_roll = randint(1,number_of_sides)
    second_roll = randint(1,number_of_sides)
    max_val = number_of_sides * 2
    
    sleep(2)

    # Selection process
    while play:
        # Start selection option at 1
        sense.show_message("%d" % guess, speed, W)
        
        # Register joystick interactino
        for event in sense.stick.get_events():
            # Check if joystick pressed
            if event.action == "pressed":
                # Check direction
                if event.direction == "up":
                    # Add or minus one to guess
                    if guess >= 1 and guess < max_val:
                        guess += 1
                    elif guess == max_val:
                        guess = 1                              
                elif event.direction == "down":
                    if guess <= max_val and guess > 1:
                        guess -= 1
                    elif guess == 1:
                        guess = max_val
        # Stop selection and exit loop on shake        
        acceleration = sense.get_accelerometer_raw()
        
        x = acceleration['x']
        y = acceleration['y']
        z = acceleration['z']
        
        x = abs(x)
        y = abs(y)
        z = abs(z)
        
        if x > 1.2 or y > 1.2 or z > 1.2:
            play = False
        else:
            play = True
                        
    # Play the game
    sense.show_message("Rolling...", speed, W)
    sleep(2)
    
    sense.show_message("1st roll %d" % first_roll, speed, W)
    sleep(1)
    
    sense.show_message("2nd roll %d" % second_roll, speed, W)
    sleep(1)
    
    total_roll = first_roll + second_roll
    sense.show_message("Total %d" % total_roll, speed, W)
    sense.show_message("Result...", speed, W)
    sleep(1)

    # Decide win or lose
    if guess == total_roll:
        sense.show_messsage("You won!", speed, W)
        play = True
    else:
        sense.show_message("You lost, try again", speed, W)
        play = True
