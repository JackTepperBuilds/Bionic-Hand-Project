from hand import Hand
from recognition import Recognize
from vision import Vision
import threading
import cv2 as cv

def main():
    hand = Hand()
    recognizer = Recognize()
    eyes = Vision()
    
    # Event object for controlling the thread (Default = False)
    event = threading.Event()

    current_frame = eyes.frame
    x = eyes.generator()
    end_check = 0

    recog_loop = threading.Thread(target = recognizer.recognize, args = (event, ))
    recog_loop.start() # Runs the recognizer.

    while True:
        gesture = recognizer.gesture_str

        hand.run_hand(gesture)

        current_frame = next(x)
        cv.imshow('LIVE', current_frame)
        recognizer.recognize(current_frame)
        
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

# Main guard
if __name__ == "__main__":
    main()