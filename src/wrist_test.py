import board # GPIO & I2C control
import busio # Set up I2C communication protocol.
import time
from adafruit_motor import servo
from adafruit_pca9685 import PCA9685

# Frequency works by sending continuous waves to the servos in this case every 333Hz (3.09ms). 
# these continous waves are set to a certain pulse width (1.5ms in a lot of cases) and
# when code runs to move a servo 180 degrees like 'servo.angle = 180', under the hood
# the angle is converted to a pulse width (In my case for DS3225 its 2.0ms). This 
# becomes the new pulse width that moves the servo.
i2c: busio.I2C = busio.I2C(board.SCL, board.SDA)
pca: PCA9685 = PCA9685(i2c)
pca.frequency = 333

# Sets wrist to channel zero and sets its min and max pulses.
wrist = servo.Servo(pca.channels[0], min_pulse = 500, max_pulse = 2500)

wrist.angle = 90
#print("0: Up, 1: Down")
#x = input()

#if (x == 1):
    #for i in range(0, 90, 2):
        #wrist.angle = i
        #time(0.2)
#elif (x == 1):
    #for i in range(90, 0, -2):
        #wrist.angle = i
        #time(0.2)