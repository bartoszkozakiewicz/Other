import cv2
import mediapipe as mp
import time
from hand_tracking import HandDetector
from controller import Controller
import pyautogui
import numpy as np

def main():
    prevt=0
    currt =0

    detector = HandDetector()

    camW = 640
    camH = 480
    cap = cv2.VideoCapture(0)
    cap.set(3,camW)
    cap.set(4,camH)

    while True:
        success, img = cap.read()

        img = detector.findHands(img)
        coords = detector.findPositions(img,[4,8,12],True)
        #If there is hand shown, then controller is "switched on"
        if len(coords)!=0:
            controller = Controller(img,coords)
            controller.volume_control()
            controller.mouse_control()

        #Calculating FPS
        currt=time.time()
        fps = 1/(currt-prevt)
        prevt=currt

        cv2.putText(img,str(int(fps)),(30,50),cv2.FONT_HERSHEY_PLAIN, fontScale=3,color=(255,0,0))
        cv2.imshow("Image",img)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break


if __name__ == "__main__":
    main()