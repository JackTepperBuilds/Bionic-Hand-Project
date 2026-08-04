import board
import busio
import time
from adafruit_motor import servo
from adafruit_pca9685 import PCA9685

i2c = busio.I2C(board.SCL, board.SDA)
pca = PCA9685(i2c)
pca.frequency = 50

wrist = servo.Servo(pca.channels[0], min_pulse=500, max_pulse=2500)

for angle in [90, 100, 90, 80, 90]:
    print(angle)
    wrist.angle = angle
    time.sleep(1)