import cv2

class Screen:

    def __init__(self, width=1280, height=720):
        self.width = width
        self.height = height
        self.cap = cv2.VideoCapture(0)  # Open webcam
        self.cap.set(cv2.CAP_PROP_FRAME_WIDTH, self.width)
        self.cap.set(cv2.CAP_PROP_FRAME_HEIGHT, self.height)

    def get_frame(self):
        ret, frame = self.cap.read()  # Read frame from webcam
        if ret:
            return frame
        else:
            return None

    def show(self):
        while True:
            frame = self.get_frame()
            if frame is None:
                break
            cv2.imshow("Webcam", frame)
            if cv2.waitKey(1) & 0xFF == 27:  # ESC key to exit
                break

        self.cap.release()
        cv2.destroyAllWindows()

# Usage
screen = Screen()
screen.show()