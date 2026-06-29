from hand import Hand
from recognition import Recognize
from vision import Vision
import threading
import cv2 as cv

def main():
    recognizer = Recognize()
    eyes = Vision()
    hand = Hand()
    
    # Event object for controlling the thread (Default = False)
    event = threading.Event()

    x = eyes.generator()
    next(x)
    end_check = 0

    recog_loop = threading.Thread(target = recognizer.recognize, args = (event, eyes))
    recog_loop.start() # Runs the recognizer.

    while True:
        hand_wrapper(recognizer, hand)

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

# Separate running the hand and opening the camera window to remove conflicts.
def hand_wrapper(recognizer: Recognize, hand: Hand) -> None:
    gesture = recognizer.gesture_str

    # Since the controller constantly runs and stops unlike the recognizer that constantly runs
    # a new thread must be created each time with the new gesture data.
    if hand.actuation.is_alive():
        return
    else:
        hand.actuation = threading.Thread(target = hand.run_hand, args = (gesture,))
        hand.actuation.start()

# Main guard
if __name__ == "__main__":
    main()