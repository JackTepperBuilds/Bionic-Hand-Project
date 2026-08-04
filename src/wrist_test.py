import board  # GPIO & I2C control
import busio  # Set up I2C communication protocol.
import time
from adafruit_motor import servo
from adafruit_pca9685 import PCA9685

current_pointer = 4
current_wrist = 4

i2c: busio.I2C = busio.I2C(board.SCL, board.SDA)
pca: PCA9685 = PCA9685(i2c)
pca.frequency = 50

wrist = servo.Servo(pca.channels[0], min_pulse=500, max_pulse=2500)
pointer = servo.Servo(pca.channels[1], min_pulse=500, max_pulse=2500)

wrist.angle = 90
pointer.angle = 90

print("0: Wrist Down, 1: Wrist Up, 2: Finger Right, 3: Finger Left, 4: Exit")

while True:
    print("How would you like to move the wrist?")
    inp_wrist: int = int(input())

    print("How would you like to move the pointer finger?")
    inp_pointer: int = int(input())

    if inp_wrist == 0:
        if current_wrist == 0:
            pass

        elif current_wrist == 1:
            for i in range(180, 0, -2):
                wrist.angle = i
                time.sleep(0.01)

        elif current_wrist in (2, 4):
            for i in range(90, 0, -2):
                wrist.angle = i
                time.sleep(0.01)

        current_wrist = 0

    elif inp_wrist == 1:
        if current_wrist == 1:
            pass

        elif current_wrist == 0:
            for i in range(0, 180, 2):
                wrist.angle = i
                time.sleep(0.01)

        elif current_wrist in (2, 4):
            for i in range(90, 180, 2):
                wrist.angle = i
                time.sleep(0.01)

        current_wrist = 1

    if inp_pointer == 2:
        if current_pointer == 2:
            pass

        elif current_pointer in (3, 4):
            for i in range(90, 0, -2):
                pointer.angle = i
                time.sleep(0.01)

        current_pointer = 2

    elif inp_pointer == 3:
        if current_pointer == 3:
            pass

        elif current_pointer in (2, 4):
            for i in range(90, 180, 2):
                pointer.angle = i
                time.sleep(0.01)

        current_pointer = 3

    if inp_wrist == 4 and inp_pointer == 4:
        if current_wrist == 0:
            for i in range(0, 90, 2):
                wrist.angle = i
                time.sleep(0.01)

        elif current_wrist == 1:
            for i in range(180, 90, -2):
                wrist.angle = i
                time.sleep(0.01)

        if current_pointer == 2:
            for i in range(0, 90, 2):
                pointer.angle = i
                time.sleep(0.01)

        elif current_pointer == 3:
            for i in range(180, 90, -2):
                pointer.angle = i
                time.sleep(0.01)

        break