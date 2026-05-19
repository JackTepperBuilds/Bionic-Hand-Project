import cv2 as cv
from picamera2 import Picamera2
from libcamera import transform

class Vision:
    # Constructor initializes the camera, sets the config, passes the config to the camera, then starts the camera.
    def __init__(self):
        self.picam2 = Picamera2()
        config = picam2.create_preview_configuration({'size': (640, 480), 'format': 'RGB888'}, transform = Transform(hflip = True))
        picam2.configure(config)
        picam2.start()

    def generator(self):
        While True:
            frame = self.picam2.capture_array()

            cv.imshow("Live Feed", frame)
            yield frame