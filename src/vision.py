import cv2 as cv
from picamera2 import Picamera2
from libcamera import Transform
from typing import Iterator

class Vision:
    # Constructor initializes the camera, sets the config, passes the config to the camera, then starts the camera.
    def __init__(self):
        self.picam2 = Picamera2()
        config = self.picam2.create_preview_configuration({'size': (640, 480), 'format': 'RGB888'}, transform = Transform(hflip = True))
        self.picam2.configure(config)
        self.picam2.start()

        self.frame = None
        self.end_program = 0

    def generator(self) -> Iterator:
        while True:
            self.frame = self.picam2.capture_array()

            yield self.frame