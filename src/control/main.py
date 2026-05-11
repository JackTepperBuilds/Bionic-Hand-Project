from hand import Hand

print("1: Close, 2: Open, 3: Peace, 4: Thumb, 5: Pointing, 6: Rock\n")
x = input()

gesture = Hand()
if x == 1:
    gesture.