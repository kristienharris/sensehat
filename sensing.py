from sense_hat import SenseHat
from time import sleep
import time
sense = SenseHat()

dark = (0,0,0)
white = (255,255,255)
red = (255,0,0)
green = (0,255,0)
blue = (0,0,255)
yellow = (255,255,0)

sense.clear()

while True:
    
    # Take readings from all three sensors
    t = sense.get_temperature_from_pressure()
    p = sense.get_pressure()
    h = sense.get_humidity()
    
    # Round the values to one decimal place
    t = round(t,1)
    p = round(p,1)
    h = round(h,1)
    
    # Create the message
    # str() converts the value to a string type so it can be concatenated
    message = "T:" + str(t) + " P:" + str(p) + " H:" + str(h)
    
    # Test if temp is within ISS range
    if t >= 18.3 and t <= 26.7:
        bg = green
    else:
        bg = red
        
    # Test if pressure is within ISS range
    if p >= 979 and p <= 1027:
        bg = green
    else:
        bg = red
    
    # Test if humidity is within ISS range
    if h > 60:
        bg = green
    else:
        bg = red
    
    # Display the scrolling message
    sense.show_message(message, scroll_speed=0.05, back_colour = bg)
    print ("Temp: " + str(t) + " Pressure: " + str(p) + " Humidity: " + str(h))
    
    # Using IMU
    # Get axis readings
    o = sense.get_orientation()
    pitch = o["pitch"]
    roll = o["roll"]
    yaw = o["yaw"]

    print("Pitch: {0} Roll: {1} Yaw: {2}".format(pitch,roll,yaw))
    
    # Which way up using accelerometer 
    acceleration = sense.get_accelerometer_raw()
    x = acceleration['x']
    y = acceleration['y']
    z = acceleration['z']
    
    # Round values to nearest whole number to get G force reading
    x=round(x,0)
    y=round(y,0)
    z=round(z,0)
    
    print("x={0}, y={1}, z={2}".format(x,y,z))
    
    # Update rotation of display depending on orientation
    if x == -1:
        sense.set_rotation(90)
    elif y == 1:
        sense.set_rotation(0)
    elif y == -1:
        sense.set_rotation(180)
    else:
        sense.set_rotation(0)
