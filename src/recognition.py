import mediapipe as mp
from mediapipe.tasks import python
from mediapipe.tasks.python import vision

class Recognize:
    def __init__(self):
        self.BaseOptions = mp.tasks.BaseOptions
        self.GestureRecognizer = mp.tasks.vision.GestureRecognizer
        self.GestureRecognizerOptions = mp.tasks.vision.GestureRecognizerOptions
        self.GestureRecognizerResult = mp.tasks.vision.GestureRecognizerResult
        self.VisionRunningMode = mp.tasks.vision.RunningMode

        

        options = GestureRecognizerOptions(base_options = self.BaseOptions('gesture_recognizer.task'),
                                           running_mode = self.VisionRunningMode.LIVE_STREAM,
                                           result_callback = print_result)

    def result(self):
