# This script is for testing servo movement. This is 
# done to ensure the servos for each finger (flex & extension) are properly 
# pulling each fishing line.

import board                          # GPIO pins such as SCL and SDA
import busio                          # Used to setup I2C connection
from adafruit_pca9685 import PCA9685 # Servo Driver
from adafruit_motor import servo      # Angle control
import time

class Center:
    def __init__(self):
        i2c = busio.I2C(board.SCL, board.SDA)
        pca = PCA9685(i2c)
        pca.frequency = 50

        self.finger = servo.Servo(pca.channels[0], min_pulse = 500, max_pulse = 2500)

    # Move servo to its 90 degree position
    def controller(self):
        for x in range(0, 180, 10):
            self.finger.angle = x
            time.sleep(1)
            print("Degrees: ")

if __name__ == "__main__":
    move_finger = Center()
    move_finger.controller()