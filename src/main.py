from hand import Hand
from recognition import Recognize
from vision import Vision
import threading

def main():
    hand = Hand()
    recognizer = Recognize()
    eyes = Vision()

    recog_loop = threading.Thread(target = recognizer.recognize)
    recog_loop.start() # Runs the recognizer paired with the camera.

    while True:
        gesture = recognizer.gesture_str

        hand.run_hand(gesture)

        # If end == 1, end the main loop while the vision generator ends.
        if eyes.end == 1:
            break

# Main guard
if __name__ == "__main__":
    main()