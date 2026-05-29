import board # GPIO & I2C control
import busio # Set up I2C communication protocol.
import time
from adafruit_motor import servo
from adafruit_pca9685 import PCA9685

current_gesture = 3

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

print("0: Up, 1: Down, 3: Exit")

while True:
    x: int = int(input())

    if (x == 0):
        if (current_gesture == 0):
            continue

        elif (current_gesture == 1):
            for i in range(90, 0, -2):
                wrist.angle = i
                time.sleep(0.02)

        current_gesture = 0

    elif (x == 1):
        if (current_gesture == 1):
            continue

        elif (current_gesture == 0):
            for i in range(90, 180, 2):
                wrist.angle = i
                time.sleep(0.02)

        current_gesture = 1

    # When ending the program the servo is set back to its center position.
    elif (x == 3):
        if (current_gesture == 0):
            for i in range(0, 90, 2):
                wrist.angle = 90
                time.sleep(0.02)

        elif (current_gesture == 1):
            for i in range(180, 90, -2):
                wrist.angle = i
                time.sleep(0.02)
        break