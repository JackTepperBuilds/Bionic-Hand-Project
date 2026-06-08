from hand import Hand
from recognition import Recognize
import threading

def main():
    hand = Hand()
    recognizer = Recognize()

    recog_loop = threading.Thread(target = recognizer.recognize)
    recog_loop.start() # Runs the recognizer paired with the camera.

    while True:
        gesture = recognizer.gesture_str

        hand.run_hand(gesture)

# Main guard
if __name__ == "__main__":
    main()