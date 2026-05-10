import time
import board # For GPIO control (SCL & SDA)
import busio # For I2C control
import adafruit_pca9685 # Servo driver that contains I2C

# innit is the constructor containing the parameters all my gesture methods will need.
# Sets up i2c communication and passes it into the sevo driver (pca) and current_gesture
# tracks what the current gesture being run is.
class Hand:
    def __init__(self, pca, prev_gesture, fingers, finger_list, current_gesture):
        i2c: busio.I2C = busio.I2C(board.SCL, board.SDA)
        self.pca = adafruit_pca9685(i2c)
        self.pca.frequency = 50
        self.prev_gesture = 'open'
        self.current_gesture = 'open'

        # finger_list dictionary that contains every gesture and their respective list of what 
        # fingers whould be up (1) and what fingers should be down (0).
        self.finger_list: dict[str, tuple] = {"Open_Palm": open_hand = (1, 1, 1, 1, 1),
                                            "Closed_Fist": close_hand = (0, 0, 0, 0, 0),
                                            "Victory": peace_sign = (1, 1, 0, 0, 0),
                                            "Thumb_Up": thumbs_up = (0, 0, 0, 0, 1),
                                            "Pointing_Up": pointing = (1, 0, 0, 0, 0),
                                            "ILoveYou": rock_on = (1, 0, 0, 1, 1)}

        # Fingers dictionary containing the channels of each servo on the driver as well as set
        # max and min pulses.
        self.fingers: dict = {"pointer": servo.Servo(self.pca.channels[0], minpulse = 500, maxpulse = 2500), 
                        "middle": servo.Servo(self.pca.channels[1], minpulse = 500, maxpulse = 2500),
                        "ring": servo.Servo(self.pca.channels[2], minpulse = 500, maxpulse = 2500),
                        "pinky": servo.Servo(self.pca.channels[3], minpulse = 500, maxpulse = 2500),
                        "thumb": servo.Servo(self.pca.channels[4], minpulse = 500, maxpulse = 2500)}


    # A method containing a nested for loop with an outer loop that contains a 5 finger array 
    # of the last gesture and an inner loop of a 5 finger array of the gesture I am trying to perform.
    def run_hand(self, pca: adafruit_pca9685, prev_gesture: str, fingers: dict, finger_list: dict, 
                 current_gesture: str) -> None:
        
        # Contains lists of prev_gesture and current_gesture 1's and 0's.
        prev_tuple: list[int] = finger_list[prev_gesture]
        current_tuple: list[int] = finger_list[current_gesture]

        # Contains a list of finger names based on their respective indexes.
        finger_names: list[str] = fingers.keys

        for x in range(5):
            for y in range(5):
                if prev_tuple[x] == current_tuple[y]:
                    continue
                elif prev_tuple[x] != current_tuple[y]:
                    finger_name: str = finger_names[y]

                    if y == 0:
                        for j in range(180, -2, -2):
                            fingers[finger_name].angle = j
                            time.sleep(0.02)

                    elif y == 1:
                        for m in range(0, 182, 2):
                            fingers[finger_name].angle = m
                            time.sleep(0.02)

                    prev_tuple: list[int] = current_tuple: list[int]