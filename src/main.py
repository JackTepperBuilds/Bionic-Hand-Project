from hand import Hand
from vision import Vision
import threading

gesture = Hand()
camera = Vision()

thread = threading.Thread(target = camera.generator)

print("Closed_Fist, Open_Palm, Victory, Thumb_Up, Pointing_Up, ILoveYou, exit\n")

while True:
    x = input()
    if x == "exit":
        break
    gesture.run_hand(x)