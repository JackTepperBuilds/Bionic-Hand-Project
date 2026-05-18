from hand import Hand

print("Closed_Fist, Open_Palm, Victory, Thumb_Up, Pointing_Up, ILoveYou, exit\n")

gesture = Hand()

while True:
    x = input()
    gesture.run_hand(x)

    if x == "exit":
        break