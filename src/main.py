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

        if recognizer.end_check == 1:
            recog_loop.join()
            break

# Main guard
if __name__ == "__main__":
    main()