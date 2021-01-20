from sense_hat import SenseHat
from time import sleep
sense = SenseHat()

# Define colours 
X = (0,0,0)
H = (55,200,171)

# Clear the screen and check our colour
sense.clear(H)

# Define matrix patterns for chevron direction
xU = [
    X,X,X,X,X,X,X,X,
    X,X,X,H,H,X,X,X,
    X,X,H,X,X,H,X,X,
    X,H,X,X,X,X,H,X,
    X,X,X,H,H,X,X,X,
    X,X,H,X,X,H,X,X,
    X,H,X,X,X,X,H,X,
    X,X,X,X,X,X,X,X,    
    ]

xD = [
    X,X,X,X,X,X,X,X,
    X,H,X,X,X,X,H,X,
    X,X,H,X,X,H,X,X,
    X,X,X,H,H,X,X,X,
    X,H,X,X,X,X,H,X,
    X,X,H,X,X,H,X,X,
    X,X,X,H,H,X,X,X,
    X,X,X,X,X,X,X,X,
    ]

xL = [
    X,X,X,X,X,X,X,X,
    X,X,X,H,X,X,H,X,
    X,X,H,X,X,H,X,X,
    X,H,X,X,H,X,X,X,
    X,H,X,X,H,X,X,X,
    X,X,H,X,X,H,X,X,
    X,X,X,H,X,X,H,X,
    X,X,X,X,X,X,X,X,
    ]    

xR = [
    X,X,X,X,X,X,X,X,
    X,H,X,X,H,X,X,X,
    X,X,H,X,X,H,X,X,
    X,X,X,H,X,X,H,X,
    X,X,X,H,X,X,H,X,
    X,X,H,X,X,H,X,X,
    X,H,X,X,H,X,X,X,
    X,X,X,X,X,X,X,X, 
    ]

xM = [
    X,X,X,X,X,X,X,X,
    X,H,X,X,X,X,H,X,
    X,X,H,X,X,H,X,X,
    X,X,X,H,H,X,X,X,
    X,X,X,H,H,X,X,X,
    X,X,H,X,X,H,X,X,
    X,H,X,X,X,X,H,X,
    X,X,X,X,X,X,X,X,  
    ]

"""
Joystick Letter Example
When joystick is pressed display letter showing direction

(un-comment this code then comment out the following code to try out the chevrons)
"""
# def dirLetter(letter):
#     sense.show_letter(letter, H, X)

# while True:
#     for event in sense.stick.get_events():
#         # Check if joystick pressed
#         if event.action == "pressed":
#             
#             # Check which direction
#             if event.direction == "up":
#                 dirLetter("U")
#             elif event.direction == "down":
#                 dirLetter("D")
#             elif event.direction == "left":
#                 dirLetter("L")
#             elif event.direction == "right":
#                 dirLetter("R")
#             elif event.direction == "middle":
#                 dirLetter("M")
#             # Wait a bit then
#             sleep(0.5)
#             sense.clear()
#         
#         print(event.direction, event.action)

# Show cheveron patterns for different directions 
while True:
    for event in sense.stick.get_events():
        # Check if joystick pressed
        if event.action == "pressed":
           


            # Check which direction
            if event.direction == "up":
                sense.set_pixels(xU)
            elif event.direction == "down":
                sense.set_pixels(xD)
            elif event.direction == "left":
                sense.set_pixels(xL)
            elif event.direction == "right":
                sense.set_pixels(xR)
            elif event.direction == "middle":
                sense.set_pixels(xM)
            # Wait a bit then
            sleep(0.5)
            sense.clear()
        
        print(event.direction, event.action)        
