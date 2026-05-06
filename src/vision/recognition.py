import mediapipe as mp
import time
from mediapipe.tasks import python
from mediapipe.tasks.python import vision
from camera import frame_stream, setup, picam

current_state = "None"

# To pass filepath containing pretrained gesture models.
BaseOptions = mp.tasks.BaseOptions

# Contains the detector and landscapes for recognition.
GestureRecognizer = mp.tasks.vision.GestureRecognizer

# Used to set the settings for GestureRecognizer.
GestureSettings = mp.tasks.vision.GestureRecognizerOptions

# Used to display gesture results (required for LIVE_STREAM).
GestureResults = mp.tasks.vision.GestureRecognizerResult

# Used to set the mode (ex: Image, Video, Live Stream).
VisionMode = mp.tasks.vision.RunningMode

# Required listener function when using LIVE_STREAM mode, with type hints for 
# each parameter.
# Checks if a gesture was detected and prints detected hand.
# First index for num hands, second index for highest likelihood gesture.
def print_result(result: GestureResults, output_image: mp.Image, timestamp_ms: int):
    global current_state
    
    if result.gestures:
        current_state = result.gestures[0][0].category_name

# Sets the settings for the recognizer.
# Such as, filepath to models, VisionMode, and print_result.
settings = GestureSettings(base_options = BaseOptions('gesture_recognizer.task'),
                           running_mode = VisionMode.LIVE_STREAM,
                           result_callback = print_result)

# Using with makes it so that I dont need to manually close the recognizer.
# Passes the settings into the GestureRecognizer and gives the 
# alias 'recognizer'
def recognize_frame(settings):
    setup()

    with GestureRecognizer.create_from_options(settings) as recognizer:
        f = frame_stream(picam) # Initialize/Declare the camera function.

        while True:
            frame = next(f) # Grab the frame.
            
            # Get the Unix epoch time for the frame, convert to milliseconds, 
            # convert to an int.
            frame_timestamp_ms = int(time.time() * 1000)

            # Converts the frame from raspberry camera to a MediaPipe image.
            mp_frame = mp.Image(image_format = mp.ImageFormat.SRGB, data = frame)
            # Runs the recognizer with the converted MediaPipe frame.
            recognizer.recognize_async(mp_frame, frame_timestamp_ms)
