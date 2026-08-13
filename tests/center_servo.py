# This script is for centering servos at their 90-degree positions. This is 
# done to ensure the fishing lines for each finger (flex & extension) are in 
# their proper positions with zero slack.

import board                          # GPIO pins such as SCL and SDA
import busio                          # Used to setup I2C connection
from adafruit_pca9685 import PCA9685 # Servo Driver
from adafruit_motor import servo      # Angle control

class Center:
    def __init__(self):
        i2c = busio.I2C(board.SCL, board.SDA)
        pca = PCA9685(i2c)
        pca.frequency = 50

        self.center = servo.Servo(pca.channels[0], min_pulse = 500, max_pulse = 2500)

    # Move servo to its 90 degree position
    def controller(self):
        self.center.angle = 90

if __name__ == "__main__":
    center = Center()
    center.controller()