#!/usr/bin/python3

import piglow, time

#Tuple containing the different arms
arms = ("top", "left", "right")
#Tuple containing the different colours
colours = ("red", "orange", "yellow", "green", "blue", "white")

#Create an instance of the piglow object called pg
pg = piglow.piglow()

#Print some explanatory text
print("\nSpiral.py\n\nA script which gradually turns each colour of LED on,\
 and when all LEDs are on gradually turns each colour of LED off.  This will\
 run infinitely until Ctrl+C is pressed, at which point it will turn all LEDs\
 off and exit.\n\n")

#Main script begins here
try:
    #Do this continuously
    while True:
        #Sequentially turn all LEDs of the same colour to brightness 20,
        # waiting 0.1s between each colour
        for colour in colours:
            for arm in arms:
                pg.set_LED(arm, colour, 20)
                pg.show()
            time.sleep(0.1)
        #Sequentially turn all LEDs of the same colour to brightness 0,
        # waiting 0.1s between each colour
        for colour in colours:
            for arm in arms:
                pg.set_LED(arm, colour, 0)
                pg.show()
            time.sleep(0.1)
#When Ctrl+C is pressed turn all of the LEDs off
except KeyboardInterrupt:
    pg.blank()
    pg.show()
