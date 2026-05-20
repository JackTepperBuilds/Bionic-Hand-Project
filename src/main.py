from hand import Hand
from vision import Vision

print("Closed_Fist, Open_Palm, Victory, Thumb_Up, Pointing_Up, ILoveYou, exit\n")

gesture = Hand()
camera = Vision()

while True:
    camera.generator()

    x = input()
    if x == "exit":
        break
    gesture.run_hand(x)