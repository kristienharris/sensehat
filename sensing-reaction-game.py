from sense_hat import SenseHat
from time import sleep
from random import choice

# Initialise sense hat instance
sense = SenseHat()

# Colours
W = (255,255,255)
R = (255,0,0)
G = (0,255,0)
D = (0,0,0)

# Arrows
arrow = [
    D,D,D,W,W,D,D,D,
    D,D,W,W,W,W,D,D,
    D,W,D,W,W,D,W,D,
    D,D,D,W,W,D,D,D,
    D,D,D,W,W,D,D,D,
    D,D,D,W,W,D,D,D,
    D,D,D,W,W,D,D,D,
    D,D,D,W,W,D,D,D,
    ]

arrow_green = [
    D,D,D,G,G,D,D,D,
    D,D,G,G,G,G,D,D,
    D,G,D,G,G,D,G,D,
    D,D,D,G,G,D,D,D,
    D,D,D,G,G,D,D,D,
    D,D,D,G,G,D,D,D,
    D,D,D,G,G,D,D,D,
    D,D,D,G,G,D,D,D,
    ]
   
arrow_red = [
    D,D,D,R,R,D,D,D,
    D,D,R,R,R,R,D,D,
    D,R,D,R,R,D,R,D,
    D,D,D,R,R,D,D,D,
    D,D,D,R,R,D,D,D,
    D,D,D,R,R,D,D,D,
    D,D,D,R,R,D,D,D,
    D,D,D,R,R,D,D,D,
    ]

# Game variables
pause = 3
score = 0
angle = 0
play = True
msg = "Keep the arrow pointing up"

sense.show_message(msg, scroll_speed=0.05, text_colour=[100,100,100])

while play:
    
    # Choose a random angle
    last_angle = angle
    while angle == last_angle:
        angle = choice([0,90,180,270])
        
    sense.set_rotation(angle)
    
    # Display white arrow
    sense.set_pixels(arrow)
    
    sleep(pause)
    
    # Get axis readings
    o = sense.get_orientation()
    pitch = o["pitch"]
    roll = o["roll"]
    yaw = o["yaw"]
    
    # Which way up using axis readings
    acceleration = sense.get_accelerometer_raw()
    x = acceleration['x']
    y = acceleration['y']
    z = acceleration['z']
    
    # Round values to nearest whole number to get G force reading
    x = round(x,0)
    y = round(y,0)
    
    print("angle: " + str(angle))
    print("x: " + str(x))
    print("y: " + str(y))
    
    # IF orientation matches the arrow...
    if y == -1 and angle == 180:
        # ADD a point and turn the arrow green
        sense.set_pixels(arrow_green)
        score += 1
    elif y == 1 and angle == 0:
      sense.set_pixels(arrow_green)
      score += 1
    elif x == -1 and angle == 90:
      sense.set_pixels(arrow_green)
      score += 1
    elif x == 1 and angle == 270:
      sense.set_pixels(arrow_green)
      score += 1
    else:
      # SET play to `False` and DISPLAY the red arrow
      sense.set_pixels(arrow_red)
      play = False
    
    # Shorten pause duration for difficulty
    pause = pause * 0.95

    # Wait for next arrow
    sleep(0.5)

# When loop is exited display score
msg = "Your score was %s" % score
sense.set_rotation(0)
sense.show_message(msg, scroll_speed=0.05, text_colour=[100,100,100])

 

