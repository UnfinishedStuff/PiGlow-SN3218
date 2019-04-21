#!/usr/bin/python3

import SN3218 as piglow
import time

pg = piglow.SN3218()

pg.shutdown(0x01)

colours = ["Red", "Orange", "Yellow", "Green", "Blue", "White"]

try:
    while True:
        for colour in colours:
            pg.set_LED("top", colour, 0x05)
            pg.set_LED("left", colour, 0x05)
            pg.set_LED("right", colour, 0x05)
            pg.show()

            time.sleep(0.1)

        for colour in colours:
            pg.set_LED("top", colour, 0x00)
            pg.set_LED("left", colour, 0x00)
            pg.set_LED("right", colour, 0x00)
            pg.show()

            time.sleep(0.1)

except KeyboardInterrupt:
    for x in range (0,19):
        pg.brightness(x,0x00)
    pg.show()
