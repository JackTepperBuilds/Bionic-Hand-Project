import time
import board # For GPIO control (SCL & SDA)
import busio # For I2C control
from adafruit_pca9685 import PCA9685 # Servo driver that contains I2C
from adafruit_motor import servo

# innit is the constructor containing the parameters all my gesture methods will need.
# Sets up i2c communication and passes it into the sevo driver (pca) and current_gesture
# tracks what the current gesture being run is.
class Hand:
    def __init__(self):
        i2c: busio.I2C = busio.I2C(board.SCL, board.SDA)
        pca: PCA9685 = PCA9685(i2c)
        pca.frequency = 50 #Hz
        self.prev_gesture = "Open_Palm"
        self.current_gesture = "Open_Palm"

        # gesture_list dictionary that contains every gesture and their respective tuple of what 
        # fingers whould be up (180 degrees) and what fingers should be down (0 degrees).
        self.gesture_list: dict[str, tuple] = {"Open_Palm": (180, 180, 180, 180, 180),
                                            "Closed_Fist": (0, 0, 0, 0, 0),
                                            "Victory": (180, 180, 0, 0, 0),
                                            "Thumb_Up": (0, 0, 0, 0, 180),
                                            "Pointing_Up": (180, 0, 0, 0, 0),
                                            "ILoveYou": (180, 0, 0, 180, 180)}

        # Fingers dictionary containing the channels of each servo on the driver as well as set
        # max and min pulses.
        self.fingers: dict = {"pointer": servo.Servo(pca.channels[0], min_pulse = 500, max_pulse = 2500), 
                        "middle": servo.Servo(pca.channels[1], min_pulse = 500, max_pulse = 2500),
                        "ring": servo.Servo(pca.channels[4], min_pulse = 500, max_pulse = 2500),
                        "pinky": servo.Servo(pca.channels[3], min_pulse = 500, max_pulse = 2500),
                        "thumb": servo.Servo(pca.channels[2], min_pulse = 500, max_pulse = 2500)}


    # A method containing a nested for loop with an outer loop that contains a 5 finger array 
    # of the last gesture and an inner loop of a 5 finger array of the gesture I am trying to perform.
    def run_hand(self, new_gesture) -> None:
        self.current_gesture = new_gesture

        # Skips the gesture if "None" is recognized.
        if self.current_gesture not in self.gesture_list:
            return
        else:
            # Contains tuples of prev_gesture and current_gesture degrees.
            prev_tuple: tuple[int] = self.gesture_list[self.prev_gesture]
            current_tuple: tuple[int] = self.gesture_list[self.current_gesture]

            # Contains a list of finger names based on their respective indexes.
                # Wrapped the iterable list of keys using list() so that it can then be 
                # subscriptable later using finger_names[y].
            finger_names: list[str] = list(self.fingers.keys())

            # Wraps prev and current tuples in lists and stores it to calculate error
            current_position: list = list(prev_tuple)
            target_position: list = list(current_tuple)
            while True:
                done: bool = True # True if 

                # Calculates the error (displacement) from where the finger currently is and the target position.
                # The servo is then stepped up or down by 2 degrees continuously until the desired angle is reached.
                for x in range(5):
                    error = target_position[x] - current_position[x]

                    # If the margin of error (less than or equal to 2 degrees) is reached
                    # continue because the finger is in target position.
                    if error <= 2:
                        continue
                    else:
                        done = False
                        finger_name: str = finger_names[x]

                        if current_tuple[x] == 180:
                            self.fingers[finger_name].angle = current_position + 2
                            current_position += 2
                            time.sleep(0.015)

                        elif current_tuple[x] == 0:
                            self.fingers[finger_name].angle = current_position - 2
                            current_position -= 2
                            time.sleep(0.015)

                # If all fingers are done moving break the loop.
                if done == True:
                    break

                self.prev_gesture = self.current_gesture
            