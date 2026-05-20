from hand import Hand
from vision import Vision
import threading

gesture = Hand()
camera = Vision()

cam_thread = threading.Thread(target = camera.generator) # Starts the camera output.

print("Closed_Fist, Open_Palm, Victory, Thumb_Up, Pointing_Up, ILoveYou, exit\n")

cam_thread.start() # Runs the camera output (Opens the live window).

while True:
    x = input()
    if x == "exit":
        break
    gesture.run_hand(x)