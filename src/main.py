from hand import Hand
from recognition import Recognize
from vision import Vision
import threading

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

        # If user presses 'd' to end camera, set the event (to true) and wait for the recog_loop to end
        # before breaking main loop (.join waits for the thread to stop and clean memory).
        if recognizer.end_check == 1:
            event.set()
            print("Thread is closing...")
            recog_loop.join()
            Vision(False)
            break

# Main guard
if __name__ == "__main__":
    main()