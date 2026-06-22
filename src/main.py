from hand import Hand
from recognition import Recognize
import threading
import time

def main():
    hand = Hand()
    recognizer = Recognize()

    # Event object for controlling the thread (Default = False)
    event = threading.Event()

    recog_loop = threading.Thread(target = recognizer.recognize, args = (event, ))
    recog_loop.start() # Runs the recognizer paired with the camera.

    while True:
        gesture = recognizer.gesture_str

        hand.run_hand(gesture)

        # If user presses 'd' to end camera, set the event and wait for the recog_loop to end
        # before breaking main loop (.join to clean up threading memory).
        if recognizer.end_check == 1:
            event.set()
            time.sleep(1)
            recog_loop.join()
            print("Thread is closing...")
            break

# Main guard
if __name__ == "__main__":
    main()