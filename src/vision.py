import cv2 as cv
from picamera2 import Picamera2
from libcamera import Transform
from typing import Iterator
from decimal import Decimal

class Vision:
    # Constructor initializes the camera, sets the config, passes the config to the camera, then starts the camera.
    def __init__(self):
        self.width_frame = 1080
        self.height_frame = 1920

        self.picam2 = Picamera2()
        config = self.picam2.create_preview_configuration({'size': (self.width_frame, self.height_frame), 'format': 'RGB888'}, transform = Transform(hflip = True))
        self.picam2.configure(config)
        self.picam2.start()

        self.frame = None

    def generator(self, recognize) -> Iterator:
        GREEN = (0, 255, 0)
        RED = (0, 0, 255)

        while True:
            self.frame = self.picam2.capture_array()

            if recognize.landmarks["WRIST"] != None:
                if recognize.warn != 1:
                    # Wrist
                    wrist = recognize.landmarks["WRIST"]

                    # Thumb
                    thumb_cmc = recognize.landmarks["THUMB_CMC"]
                    thumb_mcp = recognize.landmarks["THUMB_MCP"]
                    thumb_ip = recognize.landmarks["THUMB_IP"]
                    thumb_tip = recognize.landmarks["THUMB_TIP"]

                    # Index 
                    index_finger_mcp = recognize.landmarks["INDEX_FINGER_MCP"]
                    index_finger_pip = recognize.landmarks["INDEX_FINGER_PIP"]
                    index_finger_dip = recognize.landmarks["INDEX_FINGER_DIP"]
                    index_finger_tip = recognize.landmarks["INDEX_FINGER_TIP"]

                    # Middle
                    middle_finger_mcp = recognize.landmarks["MIDDLE_FINGER_MCP"]
                    middle_finger_pip = recognize.landmarks["MIDDLE_FINGER_PIP"]
                    middle_finger_dip = recognize.landmarks["MIDDLE_FINGER_DIP"]
                    middle_finger_tip = recognize.landmarks["MIDDLE_FINGER_TIP"]

                    # Ring
                    ring_finger_mcp = recognize.landmarks["RING_FINGER_MCP"]
                    ring_finger_pip = recognize.landmarks["RING_FINGER_PIP"]
                    ring_finger_dip = recognize.landmarks["RING_FINGER_DIP"]
                    ring_finger_tip = recognize.landmarks["RING_FINGER_TIP"]

                    # Pinky
                    pinky_mcp = recognize.landmarks["PINKY_MCP"]
                    pinky_pip = recognize.landmarks["PINKY_PIP"]
                    pinky_dip = recognize.landmarks["PINKY_DIP"]
                    pinky_tip = recognize.landmarks["PINKY_TIP"]

                    # Plots thumb lines
                    cv.line(self.frame, wrist, thumb_cmc, GREEN, 5)
                    cv.line(self.frame, thumb_cmc, thumb_mcp, GREEN, 5)
                    cv.line(self.frame, thumb_mcp, thumb_ip, GREEN, 5)
                    cv.line(self.frame, thumb_ip, thumb_tip, GREEN, 5)

                    # Plot index lines
                    cv.line(self.frame, wrist, index_finger_mcp, GREEN, 5)
                    cv.line(self.frame, index_finger_mcp, index_finger_pip, GREEN, 5)
                    cv.line(self.frame, index_finger_pip, index_finger_dip, GREEN, 5)
                    cv.line(self.frame, index_finger_dip, index_finger_tip, GREEN, 5)

                    # Plot middle lines
                    cv.line(self.frame, wrist, middle_finger_mcp, GREEN, 5)
                    cv.line(self.frame, middle_finger_mcp, middle_finger_pip, GREEN, 5)
                    cv.line(self.frame, middle_finger_pip, middle_finger_dip, GREEN, 5)
                    cv.line(self.frame, middle_finger_dip, middle_finger_tip, GREEN, 5)

                    # Plot ring lines
                    cv.line(self.frame, wrist, ring_finger_mcp, GREEN, 5)
                    cv.line(self.frame, ring_finger_mcp, ring_finger_pip, GREEN, 5)
                    cv.line(self.frame, ring_finger_pip, ring_finger_dip, GREEN, 5)
                    cv.line(self.frame, ring_finger_dip, ring_finger_tip, GREEN, 5)

                    # Plot pinky lines
                    cv.line(self.frame, wrist, pinky_mcp, GREEN, 5)
                    cv.line(self.frame, pinky_mcp, pinky_pip, GREEN, 5)
                    cv.line(self.frame, pinky_pip, pinky_dip, GREEN, 5)
                    cv.line(self.frame, pinky_dip, pinky_tip, GREEN, 5)

                    # Plots circles
                    cv.circle(self.frame, wrist, 10, RED, -1)

                    cv.circle(self.frame, thumb_cmc, 10, RED, -1)
                    cv.circle(self.frame, thumb_mcp, 10, RED, -1)
                    cv.circle(self.frame, thumb_ip, 10, RED, -1)
                    cv.circle(self.frame, thumb_tip, 10, RED, -1)

                    cv.circle(self.frame, index_finger_mcp, 10, RED, -1)
                    cv.circle(self.frame, index_finger_pip, 10, RED, -1)
                    cv.circle(self.frame, index_finger_dip, 10, RED, -1)
                    cv.circle(self.frame, index_finger_tip, 10, RED, -1)

                    cv.circle(self.frame, middle_finger_mcp, 10, RED, -1)
                    cv.circle(self.frame, middle_finger_pip, 10, RED, -1)
                    cv.circle(self.frame, middle_finger_dip, 10, RED, -1)
                    cv.circle(self.frame, middle_finger_tip, 10, RED, -1)

                    cv.circle(self.frame, ring_finger_mcp, 10, RED, -1)
                    cv.circle(self.frame, ring_finger_pip, 10, RED, -1)
                    cv.circle(self.frame, ring_finger_dip, 10, RED, -1)
                    cv.circle(self.frame, ring_finger_tip, 10, RED, -1)

                    cv.circle(self.frame, pinky_mcp, 10, RED, -1)
                    cv.circle(self.frame, pinky_pip, 10, RED, -1)
                    cv.circle(self.frame, pinky_dip, 10, RED, -1)
                    cv.circle(self.frame, pinky_tip, 10, RED, -1)

            font = cv.FONT_HERSHEY_SIMPLEX
            font_scale = 1
            thickness = 2

            # Set score as a smaller decimal value and interpolate into string
            if recognize.gesture_score != None:
                score = Decimal(recognize.gesture_score).quantize(Decimal('0.00'))
            else: 
                score = 0
            score_output = f"Confidence: {score}"

            (width, height), baseline = cv.getTextSize(recognize.gesture_str, font, font_scale, thickness)
            (width2, height2), baseline = cv.getTextSize(score_output, font, font_scale, thickness)

            str_location = (self.width_frame - width, 440 - height)
            score_location = (self.width_frame - width2, self.height_frame - height2)

            cv.putText(self.frame, recognize.gesture_str, str_location, font, font_scale, RED, thickness)
            cv.putText(self.frame, score_output, score_location, font, font_scale, RED, thickness)

            yield self.frame