import time
import board # For GPIO control (SCL & SDA)
import busio # For I2C control
import adafruit_pca9685 # Servo driver that contains I2C

# innit is the constructor containing the parameters all my gesture methods will need.
# Sets up i2c communication and passes it into the sevo driver (pca) and current_gesture
# tracks what the current gesture being run is.
class Hand:
    def __init__(self, pca, prev_gesture, fingers):
        i2c: busio.I2C = busio.I2C(board.SCL, board.SDA)
        self.pca = adafruit_pca9685(i2c)
        self.pca.frequency = 50
        self.prev_gesture = 'open'

        self.fingers: dict = {"pointer": servo.Servo(pca.channels[0], minpulse = 500, maxpulse = 2500), 
                        "middle": servo.Servo(pca.channels[1], minpulse = 500, maxpulse = 2500),
                        "ring": servo.Servo(pca.channels[2], minpulse = 500, maxpulse = 2500),
                        "pinky": servo.Servo(pca.channels[3], minpulse = 500, maxpulse = 2500),
                        "thumb": servo.Servo(pca.channels[4], minpulse = 500, maxpulse = 2500)}

    def open_hand(self, pca: adafruit_pca9685, prev_gesture: str) -> None:
        
