from hand import Hand

print("Closed_Fist, Open_Palm, Victory, Thumb_Up, Pointing_Up, ILoveYou\n")
x = input()

prev_gesture = "none"
gesture = Hand(prev_gesture, x)
prev_gesture = x

if x == "Closed_Fist":
    gesture.run_hand()
elif x == "Open_Palm":
    gesture.run_hand()
elif x == "Victory":
    gesture.run_hand()
elif x == "Thumb_Up":
    gesture.run_hand()
elif x == "Pointing_Up":
    gesture.run_hand()
elif x == "ILoveYou":
    gesture.run_hand()