from hand import Hand
from vision import Vision
from recognition import Recognize
import threading

gesture = Hand()
camera = Vision()
recognizer = Recognize()

recog_loop = threading.Thread(target = recognizer.recognize).start() # Runs the recognizer paired with the camera.

while True:
    