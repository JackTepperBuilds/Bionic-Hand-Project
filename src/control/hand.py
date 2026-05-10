import time
import board # For GPIO control (SCL & SDA)
import busio # For I2C control
import adafruit_pca9685 # Servo driver that contains I2C

# innit is the constructor containing the parameters all my gesture methods will need.
# Sets up i2c communication and passes it into the sevo driver (pca) and current_gesture
# tracks what the current gesture being run is.
class Hand:
    def __init__(self, pca, prev_gesture):
        i2c: busio.I2C = busio.I2C(board.SCL, board.SDA)
        self.pca = adafruit_pca9685(i2c)
        self.prev_gesture = 'open'

    # Dont forget frequency. May need to put that into the constructor.
    def open_hand(self, pca, prev_gesture):
