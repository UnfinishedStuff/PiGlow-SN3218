#!/usr/bin/python3

#Import the libraries for using the i2c bus
import os, fcntl

class SN3218:
    #Constructor for setting up the class
    def __init__ (self):
        #Set the i2c address
        self.address = 0x54
        self.slave = 0x0703

        #Create a i2c objects for read/writing as a file object
        self.fd = os.open("/dev/i2c-1", os.O_RDWR)
        fcntl.ioctl(self.fd, self.slave, self.address)

        #The SN3218 starts in shutdown mode.  Activate it.
        os.write(self.fd, b'\x00\x01')

        #Turn on all 3 banks of LEDs
        self.enable(0x13, 0xff)
        self.enable(0x14, 0xff)
        self.enable(0x15, 0xff)

        #Blank the LEDs
        for x in range (0x01, 0x13):
            self.set_LED(x, 0)
        self.show()

    #Function to control the shutdown register
    def shutdown(self, mode):
        os.write(self.fd, bytearray([0x00, mode]))

    def enable(self, register, value):
        os.write(self.fd, bytearray([register, value]))

    def brightness(self, register, brightness):
        os.write(self.fd, bytearray([register, brightness]))

    def show(self):
        os.write(self.fd, bytearray([0x16, 0xff]))

    def set_LED(self, register, brightness):
        os.write(self.fd, bytearray([register, brightness]))
