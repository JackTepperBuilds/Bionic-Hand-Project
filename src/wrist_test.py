import board # GPIO & I2C control
import busio # Set up I2C communication protocol.
import time
from adafruit_motor import servo
from adafruit_pca9685 import PCA9685

current_gesture = 4
current_wrist = 4

# Frequency works by sending continuous waves to the servos in this case every 50Hz (20ms). 
# these continous waves are set to a certain pulse width (1.5ms in a lot of cases) and
# when code runs to move a servo 180 degrees like 'servo.angle = 180', under the hood
# the angle is converted to a pulse width (In my case for DS3225 its 2.0ms). This 
# becomes the new pulse width that moves the servo.
i2c: busio.I2C = busio.I2C(board.SCL, board.SDA)
pca: PCA9685 = PCA9685(i2c)
pca.frequency = 50

# Sets wrist to channel zero and sets its min and max pulses.
wrist = servo.Servo(pca.channels[0], min_pulse = 500, max_pulse = 2500)
pointer = servo.Servo(pca.channels[1], min_pulse = 500, max_pulse = 2500)

# To make sure wrist is centered before getting input from user.
wrist.servo = 90
pointer.servo = 90

print("0: Down, 1: Up, 2: FingerR, 3: FingerL, 4: Exit")

while True:
    print("How would you like to move the wrist?")
    inp_wrist: int = int(input())

    print("How would you like to move the pointer finger")
    pointer: int = int(input())

    if (inp_wrist == 0):
        if (current_wrist == 0):
            continue

        elif (current_wrist == 1):
            for i in range(180, 0, -2):
                wrist.angle = i
                time.sleep(0.01)

        elif (current_wrist == 2):
            for i in range(90, 0, -2):
                wrist.angle = i
                time.sleep(0.01)

        current_wrist = 0

    elif (inp_wrist == 1):
        if (current_wrist == 1):
            continue

        elif (current_wrist == 0):
            for i in range(0, 180, 2):
                wrist.angle = i
                time.sleep(0.01)

        elif (current_wrist == 2):
            for i in range(90, 180, 2):
                wrist.angle = i
                time.sleep(0.01)

        current_wrist = 1

    elif (pointer == 2):
        if (current_gesture == 2):
            continue

        elif (current_gesture == 3):
            for i in range(180, 0, -2):
                pointer.angle = i
                time.sleep(0.01)

        current_gesture = 2

    elif (pointer == 3):
        if (current_gesture == 3):
            continue

        elif (current_gesture == 2):
            for i in range(0, 180, 2):
                pointer.angle = i
                time.sleep(0.01)

        current_gesture = 3

    # When ending the program the servo is set back to its center position.
    elif (inp_wrist == 4 and pointer == 4):
        if (current_wrist == 0):
            for i in range(0, 90, 2):
                wrist.angle = i
                time.sleep(0.01)

        if (current_wrist == 1):
            for i in range(180, 90, -2):
                wrist.angle = i
                time.sleep(0.01)

        if (current_gesture == 2):
            for i in range(180, 90, -2):
                pointer.angle = i
                time.sleep(0.01)

        if (current_gesture == 3):
            for i in range(0, 90, 2):
                pointer.angle = i
                time.sleep(0.01)

        break