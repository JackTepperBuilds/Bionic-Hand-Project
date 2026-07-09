import mediapipe as mp
from mediapipe.tasks import python
from mediapipe.tasks.python import vision
from vision import Vision
import cv2 as cv
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
        
        # The settings of the recognizer. Contains the location of the pretrained gesture models, sets the LIVE,
        # And calls the result method every time a new gesture is recognized.
        self.options = self.GestureRecognizerOptions(base_options = self.BaseOptions('gesture_recognizer.task'),
                                           running_mode = self.VisionRunningMode.LIVE_STREAM,
                                           result_callback = self.print_result)
        
        self.landmarks: dict = {"WRIST": None,
                                "THUMB_CMC": None,
                                "THUMB_MCP": None,
                                "THUMB_IP": None,
                                "THUMB_TIP": None,
                                "INDEX_FINGER_MCP": None,
                                "INDEX_FINGER_PIP": None,
                                "INDEX_FINGER_DIP": None,
                                "INDEX_FINGER_TIP": None,
                                "MIDDLE_FINGER_MCP": None,
                                "MIDDLE_FINGER_PIP": None,
                                "MIDDLE_FINGER_DIP": None,
                                "MIDDLE_FINGER_TIP": None,
                                "RING_FINGER_MCP": None,
                                "RING_FINGER_PIP": None,
                                "RING_FINGER_DIP": None,
                                "RING_FINGER_TIP": None,
                                "PINKY_MCP": None,
                                "PINKY_PIP": None,
                                "PINKY_DIP": None,
                                "PINKY_TIP": None}
        
        self.gesture_str = "Open_Palm"
        self.gesture_score = None
    
        self.no_gesture = 0
        self.warn = 0

    # If a gesture is recognized by the camera the current gesture is set to 'gesture_str', else 'Nothing' is printed 
    # because no gesture is being recognized.
    def print_result(self, result, output_image: mp.Image, timestamp_ms: int) -> None:
        if result.gestures:
            # Set back to 0 when a gesture is recognized
            self.no_gesture = 0 

            self.gesture_str = result.gestures[0][0].category_name
            self.gesture_score = result.gestures[0][0].score
        else:
            self.no_gesture = 1

        if result.hand_landmarks:
            # Set back to 0 when landmarks are recognized
            self.warn = 0

            # Converts MediaPipe (0-1) coordinates to pixel coordinates
            # Wrist
            wrist_x = result.hand_landmarks[0][0].x
            wrist_y = result.hand_landmarks[0][0].y
            pwrist_x = int(wrist_x * 640)
            pwrist_y = int(wrist_y * 480)

            self.landmarks["WRIST"] = (pwrist_x, pwrist_y)
            
            # Thumb
            thumb_cmc_x = result.hand_landmarks[0][1].x
            thumb_cmc_y = result.hand_landmarks[0][1].y
            thumb_mcp_x = result.hand_landmarks[0][2].x
            thumb_mcp_y = result.hand_landmarks[0][2].y
            thumb_ip_x = result.hand_landmarks[0][3].x
            thumb_ip_y = result.hand_landmarks[0][3].y
            thumb_tip_x = result.hand_landmarks[0][4].x
            thumb_tip_y = result.hand_landmarks[0][4].y

            pthumb_cmc_x = int(thumb_cmc_x * 640)
            pthumb_cmc_y = int(thumb_cmc_y * 480)
            pthumb_mcp_x = int(thumb_mcp_x * 640)
            pthumb_mcp_y = int(thumb_mcp_y * 480)
            pthumb_ip_x = int(thumb_ip_x * 640)
            pthumb_ip_y = int(thumb_ip_y * 480)
            pthumb_tip_x = int(thumb_tip_x * 640)
            pthumb_tip_y = int(thumb_tip_y * 480)
            
            self.landmarks["THUMB_CMC"] = (pthumb_cmc_x, pthumb_cmc_y)
            self.landmarks["THUMB_MCP"] = (pthumb_mcp_x, pthumb_mcp_y)
            self.landmarks["THUMB_IP"] = (pthumb_ip_x, pthumb_ip_y)
            self.landmarks["THUMB_TIP"] = (pthumb_tip_x, pthumb_tip_y)
            
            # Pointer Finger
            index_mcp_x = result.hand_landmarks[0][5].x
            index_mcp_y = result.hand_landmarks[0][5].y
            index_pip_x = result.hand_landmarks[0][6].x
            index_pip_y = result.hand_landmarks[0][6].y
            index_dip_x = result.hand_landmarks[0][7].x
            index_dip_y = result.hand_landmarks[0][7].y
            index_tip_x = result.hand_landmarks[0][8].x
            index_tip_y = result.hand_landmarks[0][8].y

            pindex_mcp_x = int(index_mcp_x * 640)
            pindex_mcp_y = int(index_mcp_y * 480)
            pindex_pip_x = int(index_pip_x * 640)
            pindex_pip_y = int(index_pip_y * 480)
            pindex_dip_x = int(index_dip_x * 640)
            pindex_dip_y = int(index_dip_y * 480)
            pindex_tip_x = int(index_tip_x * 640)
            pindex_tip_y = int(index_tip_y * 480)

            self.landmarks["INDEX_FINGER_MCP"] = (pindex_mcp_x, pindex_mcp_y)
            self.landmarks["INDEX_FINGER_PIP"] = (pindex_pip_x, pindex_pip_y)
            self.landmarks["INDEX_FINGER_DIP"] = (pindex_dip_x, pindex_dip_y)
            self.landmarks["INDEX_FINGER_TIP"] = (pindex_tip_x, pindex_tip_y)

            # Middle Finger
            middle_mcp_x = result.hand_landmarks[0][9].x
            middle_mcp_y = result.hand_landmarks[0][9].y
            middle_pip_x = result.hand_landmarks[0][10].x
            middle_pip_y = result.hand_landmarks[0][10].y
            middle_dip_x = result.hand_landmarks[0][11].x
            middle_dip_y = result.hand_landmarks[0][11].y
            middle_tip_x = result.hand_landmarks[0][12].x
            middle_tip_y = result.hand_landmarks[0][12].y

            pmiddle_mcp_x = int(middle_mcp_x * 640)
            pmiddle_mcp_y = int(middle_mcp_y * 480)
            pmiddle_pip_x = int(middle_pip_x * 640)
            pmiddle_pip_y = int(middle_pip_y * 480)
            pmiddle_dip_x = int(middle_dip_x * 640)
            pmiddle_dip_y = int(middle_dip_y * 480)
            pmiddle_tip_x = int(middle_tip_x * 640)
            pmiddle_tip_y = int(middle_tip_y * 480)

            self.landmarks["MIDDLE_FINGER_MCP"] = (pmiddle_mcp_x, pmiddle_mcp_y)
            self.landmarks["MIDDLE_FINGER_PIP"] = (pmiddle_pip_x, pmiddle_pip_y)
            self.landmarks["MIDDLE_FINGER_DIP"] = (pmiddle_dip_x, pmiddle_dip_y)
            self.landmarks["MIDDLE_FINGER_TIP"] = (pmiddle_tip_x, pmiddle_tip_y)

            # Ring Finger
            ring_mcp_x = result.hand_landmarks[0][13].x
            ring_mcp_y = result.hand_landmarks[0][13].y
            ring_pip_x = result.hand_landmarks[0][14].x
            ring_pip_y = result.hand_landmarks[0][14].y
            ring_dip_x = result.hand_landmarks[0][15].x
            ring_dip_y = result.hand_landmarks[0][15].y
            ring_tip_x = result.hand_landmarks[0][16].x
            ring_tip_y = result.hand_landmarks[0][16].y

            pring_mcp_x = int(ring_mcp_x * 640)
            pring_mcp_y = int(ring_mcp_y * 480)
            pring_pip_x = int(ring_pip_x * 640)
            pring_pip_y = int(ring_pip_y * 480)
            pring_dip_x = int(ring_dip_x * 640)
            pring_dip_y = int(ring_dip_y * 480)
            pring_tip_x = int(ring_tip_x * 640)
            pring_tip_y = int(ring_tip_y * 480)

            self.landmarks["RING_FINGER_MCP"] = (pring_mcp_x, pring_mcp_y)
            self.landmarks["RING_FINGER_PIP"] = (pring_pip_x, pring_pip_y)
            self.landmarks["RING_FINGER_DIP"] = (pring_dip_x, pring_dip_y)
            self.landmarks["RING_FINGER_TIP"] = (pring_tip_x, pring_tip_y)

            # Pinky Finger
            pinky_mcp_x = result.hand_landmarks[0][17].x
            pinky_mcp_y = result.hand_landmarks[0][17].y
            pinky_pip_x = result.hand_landmarks[0][18].x
            pinky_pip_y = result.hand_landmarks[0][18].y
            pinky_dip_x = result.hand_landmarks[0][19].x
            pinky_dip_y = result.hand_landmarks[0][19].y
            pinky_tip_x = result.hand_landmarks[0][20].x
            pinky_tip_y = result.hand_landmarks[0][20].y

            ppinky_mcp_x = int(pinky_mcp_x * 640)
            ppinky_mcp_y = int(pinky_mcp_y * 480)
            ppinky_pip_x = int(pinky_pip_x * 640)
            ppinky_pip_y = int(pinky_pip_y * 480)
            ppinky_dip_x = int(pinky_dip_x * 640)
            ppinky_dip_y = int(pinky_dip_y * 480)
            ppinky_tip_x = int(pinky_tip_x * 640)
            ppinky_tip_y = int(pinky_tip_y * 480)

            self.landmarks["PINKY_MCP"] = (ppinky_mcp_x, ppinky_mcp_y)
            self.landmarks["PINKY_PIP"] = (ppinky_pip_x, ppinky_pip_y)
            self.landmarks["PINKY_DIP"] = (ppinky_dip_x, ppinky_dip_y)
            self.landmarks["PINKY_TIP"] = (ppinky_tip_x, ppinky_tip_y)
        else:
            self.warn = 1

    # This method reads the frames from the vision class's generator and uses the built in landmarks for gesture recognition.
    def recognize(self, event: threading.Event, eyes: Vision) -> None:
        recognizer = self.GestureRecognizer.create_from_options(self.options)

        prev_timestamp = 0
        prev_frame = None
        # 'Try' the code and no matter what error arises make sure to 'finally' clean everything up.
        try:
            while not event.is_set():
                frame = eyes.frame

                if frame is None or frame is prev_frame:
                    time.sleep(0.01)
                    continue

                prev_frame = frame

                # Unix epoch time in milliseconds set to an int instead of a float
                frame_timestamp_ms = int(time.monotonic() * 1000)
                
                # Ensure the new frame is ALWAYS after the previous.
                if prev_timestamp >= frame_timestamp_ms:
                    frame_timestamp_ms = prev_timestamp + 1

                prev_timestamp = frame_timestamp_ms

                # OpenCV prefers BGR frames but MediaPipe expects RBG so convert before using.
                mp_frame = cv.cvtColor(frame, cv.COLOR_BGR2RGB)
                mp_image = mp.Image(image_format = mp.ImageFormat.SRGB, data = mp_frame)

                # Contains timestamps of captured frames in milliseconds so that mediapipe internally
                # can drop unnecessary frames for lower latency if needed.
                recognizer.recognize_async(mp_image, frame_timestamp_ms)    

                time.sleep(0.06)
        finally:
            # Close the recognizer.
            recognizer.close()