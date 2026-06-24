import cv2 as cv
from picamera2 import Picamera2
from libcamera import Transform
from typing import Iterator
import threading

class Vision:
    # Constructor initializes the camera, sets the config, passes the config to the camera, then starts the camera.
    def __init__(self):
        self.picam2 = Picamera2()
        config = self.picam2.create_preview_configuration({'size': (640, 480), 'format': 'RGB888'}, transform = Transform(hflip = True))
        self.picam2.configure(config)
        self.picam2.start()

        self.end_program = 0

    def generator(self, event: threading.Event) -> Iterator:
        while not event.is_set():
            frame = self.picam2.capture_array()

            cv.imshow('Live Feed', frame)
            yield frame

            # TODO: make a conditional for 'event.is_set()' so that the camera loop ends when the recognition
            # thread ends instead of ending abruptly.
            if cv.waitKey(20) & 0xFF == ord('d'):
                self.end_program = 1
                
        self.picam2.stop()
        cv.destroyAllWindows()