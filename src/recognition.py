import mediapipe as mp
from mediapipe.tasks import python
from mediapipe.tasks.python import vision
from vision import Vision
import time

class Recognize:
    def __init__(self):
        self.BaseOptions = mp.tasks.BaseOptions
        self.GestureRecognizer = mp.tasks.vision.GestureRecognizer
        self.GestureRecognizerOptions = mp.tasks.vision.GestureRecognizerOptions
        self.GestureRecognizerResult = mp.tasks.vision.GestureRecognizerResult
        self.VisionRunningMode = mp.tasks.vision.RunningMode

        self.gesture_str = "Open_Palm"
        
        # The settings of the recognizer. Contains the location of the pretrained gesture models, sets the LIVE,
        # And calls the result method every time a new gesture is recognized.
        self.options = GestureRecognizerOptions(base_options = self.BaseOptions('gesture_recognizer.task'),
                                           running_mode = self.VisionRunningMode.LIVE_STREAM,
                                           result_callback = self.result)

    # Grabs the current gesture that the recognizer captured and sets it to the gesture instance variable.
    def result(self, result: GestureRecognizerResult, output_image: mp.Image, timestamp_ms: int) -> None:
        self.gesture_str = result.gestures[0][0].categoryName

    # This method reads the frames from the vision class's generator and uses the built in landmarks for gesture
    # recognition.
    def recognize(self) -> None:
        with GestureRecognizer.create_from_options(self.options) as recognizer:
            camera = Vision()
            x = camera.generator()

            # Unix epoch time in milliseconds set to an int instead of a float
            frame_timestamp_ms = int(time.time() * 1000)

            frame = next(x) # Runs the generator up to yield and the returns the frame.
            mp_image = mp.Image(image_format = mp.ImageFormat.SRGB, data = frame)

            # Contains timestamps of captured frames in milliseconds so that mediapipe internally
            # can drop unnecessary frames for lower latency if needed.
            recognizer.recognize_async(mp_image, frame_timestamp_ms)