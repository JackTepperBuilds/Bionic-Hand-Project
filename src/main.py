from hand import Hand
from recognition import Recognize
import threading

hand = Hand()
recognizer = Recognize()

recog_loop = threading.Thread(target = recognizer.recognize).start() # Runs the recognizer paired with the camera.

while True:
    gesture = recognizer.gesture_str

    hand.run_hand(gesture)