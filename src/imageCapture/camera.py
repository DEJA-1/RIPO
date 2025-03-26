import cv2
import os
from datetime import datetime

class CameraHandler:
    SAVE_DIR = os.path.join(os.path.dirname(__file__), '..', 'data', 'model')
    HELP_TEXT = "Make photo - 's'    Quit - 'q'"
    WINDOW_NAME = "Preview"
    FRAME_WIDTH = 1280
    FRAME_HEIGHT = 720

    def __init__(self):
        os.makedirs(self.SAVE_DIR, exist_ok=True)
        self.cap = cv2.VideoCapture(0)
        self.cap.set(cv2.CAP_PROP_FRAME_WIDTH, self.FRAME_WIDTH)
        self.cap.set(cv2.CAP_PROP_FRAME_HEIGHT, self.FRAME_HEIGHT)

    def _is_opened(self):
        return self.cap.isOpened()

    def _save_frame(self, frame):
        filename = os.path.join(
            self.SAVE_DIR, f"wzorzec_{datetime.now().strftime('%Y%m%d_%H%M%S')}.jpg")
        cv2.imwrite(filename, frame)
        print(f"Saved: {filename}")

    def start(self):
        if not self._is_opened():
            print("Can't open the camera.")
            return

        while True:
            success, frame = self.cap.read()
            if not success:
                print("Error while fetching frame.")
                break

            cv2.putText(frame, self.HELP_TEXT, (10, 25),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 0, 255), 2)
            cv2.imshow(self.WINDOW_NAME, frame)

            key = cv2.waitKey(1) & 0xFF
            if key == ord('q'):
                break
            elif key == ord('s'):
                self.save_frame(frame)

        self.cap.release()
        cv2.destroyAllWindows()
