from hand import Hand
from vision import Vision

gesture = Hand()
camera = Vision()
camera.generator()

print("Closed_Fist, Open_Palm, Victory, Thumb_Up, Pointing_Up, ILoveYou, exit\n")

while True:
    x = input()
    if x == "exit":
        break
    gesture.run_hand(x)