from gestures import *
from recognition import recognize_frame, settings
import recognition
import camera
import threading

def main():
    servos = setup()

    # Creates a thread for recognize_frame so that new states are captured
    # from its loop, while also looping the gesture control in main.
    threading.Thread(target = recognize_frame, args=(settings,)).start()

    prev_state = 'None'

    while True:
        state = recognition.current_state

        if state != prev_state:
            print(state)

        # Make the prev_state equal to the gesture before state is changed.
        prev_state = state

        # If the keyboard button 'd' was pressed end camera and MediaPipe.
        if camera.End_Live == 'yes':
            break

        if state == 'None':
            continue
        elif state == 'Closed_Fist':
            close_hand(servos)
        elif state == 'Open_Palm':
            open_hand(servos)
        elif state == 'Victory':
            peace_sign(servos)
        elif state == 'Thumb_Up':
            thumbs_up(servos)
        elif state == 'Pointing_Up':
            pointing(servos)
        elif state == 'ILoveYou':
            rock_on(servos)

# main_guard
if __name__ == "__main__":
    main() 