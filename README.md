# PiGlow-SN3218

This is a home-made library for Pimoroni's [PiGlow](https://shop.pimoroni.com/products/piglow) board, mostly written for fun and practice.

The PiGlow is a board with 18 single-colour LEDs in a mixture of colours controlled by an SN3218 chip.  This repo contains four files:  

* `SN3218.py` is the module which controls the SN3218 chip, and should be useful for any board with an SN3218 chip.  If you're using this repo to control a PiGlow board you shouldn't ever need to interact with this module directly.
* `piglow.py` is the module which controls the SN3218 chip in a context which makes sense for the PiGlow board.  If you're using a PiGlow board this is the module you'll import and use.
* `spiral.py` is an example script which shows off the capabilities of the board.
* `arms_demo.py` is an example script which turns all LEDs in the same "arm" of the PiGlow on and prints the name of the arm.  This is to clarify the way which the PiGlow library controls the board and is explained more below.

The PiGlow board has 18 LEDs in groups of 6.  Each group is an "arm" of a three-armed spiral, and contains LEDs of six colours in the same order: red, orange, yellow, green, blue and white, with red at the tip of each "arm" and white at the centre of the spiral.  To control the LEDs you have to tell the PiGlow library which colour of LED on which "arm" you want to set, and then give it a brightness value from 0 to 255 inclusive.

You can see which LEDs are part of which "arm", and the order of the LEDs, in the image below:

![annotated_board](/annotated_board.jpg)

# Using the module

Begin by importing `piglow.py` and creating an instance to control the board:

```
import piglow
piglow = piglow.piglow()
```

To set an LED you need to provide 3 things:  
* The arm the LED is on.  Valid arm values are strings of `top`, `left` and `right`.
* The colour of LED to be set.  Valid values are strings of `red`, `orange`, `yellow`,`green`, `blue`, and `white`.  Remember, each arm only has one LED of each colour and the arms have the LED colourss in the same order.
* A brightness value which the LED should be set to.  Valid values are integers from 0 to 255 inclusive.

Use the `set_LED(arm, colour, brightness)` function to set the LED with colour `colour` on arm `arm` to the specified brightness value.

This will set the LED state on the chip, but nothing will actually show on the board until the `show()` function is called.

To turn an LED off use `set_LED` with a brightness of `0`.  Alternatively, use `blank()` to zero all LEDs at the same time.  Don't forget to use `show()` afterwards.  

That's about it!  It's a very simple board.
