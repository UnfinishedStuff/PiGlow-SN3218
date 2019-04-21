import SN3218, time

class piglow:
    def __init__(self):
        #Create a SN3218 object to control the board
        self.sn3218 = SN3218.SN3218()

        #Create dictionaries describing the LEDs
        #Piglow has 3 "arms" with fixed LED colours
        #One dict. for each arm containing the register address of that LED

        self.arms = ("top", "left", "right")
        self.colours = ("red", "orange", "yellow", "green", "blue", "white")

        self.left = {"red": 0x01, \
                    "orange":0x02, \
                    "yellow":0x03, \
                    "green":0x04, \
                    "blue":0x0F, \
                    "white":0x0D}

        self.right = {"red": 0x12, \
                    "orange":0x11, \
                    "yellow":0x10, \
                    "green":0x0E, \
                    "blue":0x0C, \
                    "white":0x0B}

        self.top = {"red": 0x07, \
                    "orange":0x08, \
                    "yellow":0x09, \
                    "green":0x06, \
                    "blue":0x05, \
                    "white":0x0A}

        #Blank the LEDs
        for x in range (0x01,0x12):
            self.sn3218.set_LED(x, 0)
        self.sn3218.show()

    #Function to control the shutdown register
    def shutdown(self, mode):
        if (mode == 0x01) or (mode == 0x00):
            self.sn3218.shutdown(mode)
        else:
            print("Error!  The shutdown mode must be  an int of 0 or 1. \
 Was given " + str(mode))

    #Function to enable or disable the 3 LED banks
    #There are three banks of LEDs, each representing 6 LEDs.
    #LEDs are activated by a binary 1 in the register, using values 0-63
    def enable(self, bank, value):
        if isinstance(bank, int) and (bank >= 0) and (bank <= 2):
            if (value >= 0) and (value <= 63) and isinstance(value, int):
                self.sn3218.enable(bank, value)
            else:
                print("Error!  Value must be an integer between 0 and 63.\
 Was given " + str(value))
        else:
            print("Error! Bank must be an integer between 0 and 2. \
 Was given " + str(bank))

    #Function to set the brightness of individual LEDs
    def set_LED(self, arm, colour, brightness):
        if arm == "top":
            arm = self.top
        elif arm == "left":
            arm = self.left
        elif arm == "right":
            arm = self.right
        else:
            print("Error!  Arm must be 'top', 'left' or 'right'.  Was\
 given " + str(arm))
            return

        if colour in self.colours:
            if isinstance(brightness, int) and (brightness >= 0)\
 and (brightness <= 255):
                self.sn3218.set_LED(arm[colour], brightness)
            else:
                print("Error! Brightness must be an integer between\
 0 and 255.  Was given " + str(brightness))
        else:
            print("Error! Colour must be one of 'red', 'orange', 'yellow',\
 'green', 'blue' or 'white'.  Was given " + str(colour))

    #Function to refresh the LEDs (writing values does nothing, this
    #must be called for anything to actually show)
    def show(self):
        self.sn3218.show()

    #Function to blank the display
    def blank(self):
        for colour in self.colours:
                self.sn3218.set_LED(self.top[colour], 0)
                self.sn3218.set_LED(self.left[colour], 0)
                self.sn3218.set_LED(self.right[colour], 0)

