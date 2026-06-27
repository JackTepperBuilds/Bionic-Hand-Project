from hand import Hand
from recognition import Recognize
from vision import Vision
import threading
import cv2 as cv

def main():
    recognizer = Recognize()
    eyes = Vision()
    
    # Event object for controlling the thread (Default = False)
    event = threading.Event()

    x = eyes.generator()
    next(x)
    end_check = 0

    recog_loop = threading.Thread(target = recognizer.recognize, args = (event, eyes))
    recog_loop.start() # Runs the recognizer.

    while True:
        hand_wrapper(recognizer)

        current_frame = next(x)
        cv.imshow('LIVE', current_frame)
        
        if cv.waitKey(20) & 0xFF == ord('d'):
            end_check = 1

        # If user presses 'd' to end camera, set the event (to true) and wait for the recog_loop to end
        # before breaking main loop (.join waits for the thread to stop and clean memory).
        if end_check == 1:
            event.set()
            recog_loop.join()
            eyes.picam2.stop()
            cv.destroyAllWindows() 
            break

# TODO: Thread the run_hand method in the Hand class so that when a gesture runs the camera wont freeze.
# Also check if the thread '.is_alive' to make sure if the gesture is still actuating or not.
# This is to prevent unwanted jittering and conflicts with actuation. 

# Separate running the hand and opening the camera window to remove conflicts.
def hand_wrapper(recognizer: Hand):
    hand = Hand()

    gesture = recognizer.gesture_str

    hand.run_hand(gesture)

# Main guard
if __name__ == "__main__":
    main()