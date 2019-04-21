#!/usr/bin/python3

import piglow, time

#Tuple containing the different arms
arms = ("top", "left", "right")
#Tuple containing the different colours
colours = ("red", "orange", "yellow", "green", "blue", "white")

#Create an instance of the piglow object called pg
pg = piglow.piglow()

#Print some explanatory text
print("\narms_dem.py\n\nA script which sequentially turns all LEDs in each\
 arm to on and prints the name of that arm.  This is designed to illustrate\
 which LEDs belong to which arm group.\n\n")

#Main script begins here
try:
    #Do this continuously
    while True:
        #Set all LEDs in the same arm to brightness 20 and wait 1 second
        for arm in arms:
            print(arm.capitalize() + " LEDs")
            for colour in colours:
                pg.set_LED(arm, colour, 20)
            pg.show()
            time.sleep(1)
        #Set all LEDs in the same arm to brightness 0 and wait 1 second
            for colour in colours:
                pg.set_LED(arm, colour, 0)
            pg.show()
#When Ctrl+C is pressed turn all of the LEDs off
except KeyboardInterrupt:
    pg.blank()
    pg.show()
