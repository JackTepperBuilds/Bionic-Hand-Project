import mediapipe as mp
from mediapipe.tasks import python
from mediapipe.tasks.python import vision
from vision import Vision
import time
import threading

class Recognize:
    def __init__(self):
        # Sets references to MediaPipes recognizer classes.
        self.GestureRecognizer = mp.tasks.vision.GestureRecognizer
        self.GestureRecognizerOptions = mp.tasks.vision.GestureRecognizerOptions

        # Sets references to MediaPipes configuration classes.
        self.BaseOptions = mp.tasks.BaseOptions
        self.VisionRunningMode = mp.tasks.vision.RunningMode

        self.gesture_str = "Open_Palm"
        
        # The settings of the recognizer. Contains the location of the pretrained gesture models, sets the LIVE,
        # And calls the result method every time a new gesture is recognized.
        self.options = self.GestureRecognizerOptions(base_options = self.BaseOptions('gesture_recognizer.task'),
                                           running_mode = self.VisionRunningMode.LIVE_STREAM,
                                           result_callback = self.print_result)

    # If a gesture is recognized by the camera the current gesture is set to 'gesture_str', else 'Nothing' is printed 
    # because no gesture is being recognized.
    def print_result(self, result, output_image: mp.Image, timestamp_ms: int) -> None:
        if result.gestures:
            self.gesture_str = result.gestures[0][0].category_name
            print(self.gesture_str)
        else:
            print("Nothing")

        if result.hand_landmarks:
            print(result.hand_landmarks[0][4])
        else:
            print("NO LANDMARKS")

    # This method reads the frames from the vision class's generator and uses the built in landmarks for gesture recognition.
    def recognize(self, event: threading.Event, end_check: int, frame) -> None:
        recognizer = self.GestureRecognizer.create_from_options(self.options)
        camera = Vision()

        # 'Try' the code and no matter what error arises make sure to 'finally' clean everything up.
        try:
            while not event.is_set():
                # Unix epoch time in milliseconds set to an int instead of a float
                frame_timestamp_ms = int(time.time() * 1000)

                mp_image = mp.Image(image_format = mp.ImageFormat.SRGB, data = frame)

                # Contains timestamps of captured frames in milliseconds so that mediapipe internally
                # can drop unnecessary frames for lower latency if needed.
                recognizer.recognize_async(mp_image, frame_timestamp_ms)    
        finally:
            # Terminate the generator and camera after recognizer ends.
            recognizer.close()
            camera.picam2.stop()