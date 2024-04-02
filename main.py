import cv2
import numpy as np
import pyautogui

from screen import Screen

RES_SCREEN=pyautogui.size()
SCREEN_WIDTH = 1280
SCREEN_HEIGHT = 720
FRAME_WIDTH = 640
FRAME_HEIGHT = 480

def main():
    source=int(input("Enter 1 to use built in webcam or 2 to use remote camera : "))
    if(source==1):
        URL=0
    elif (source==2):
        URL=input("Enter the URL for video stream within quotations : ")
    camera = cv2.VideoCapture(URL)
    camera.set(cv2.CAP_PROP_FRAME_WIDTH, FRAME_WIDTH)
    camera.set(cv2.CAP_PROP_FRAME_HEIGHT, FRAME_HEIGHT)

if __name__ == '__main__':
    main()