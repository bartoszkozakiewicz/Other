import cv2
import mediapipe as mp
import time
from hand_tracking import HandDetector
import pyautogui
import numpy as np

#https://github.com/AndreMiras/pycaw
from comtypes import CLSCTX_ALL
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume

# print(volume.GetVolumeRange()) - checked volume range

class Controller():
    def __init__(self,img,coords):
        self.img= img
        self.coords = coords

        self.SCREEN_WIDTH, self.SCREEN_HEIGHT = pyautogui.size()
        self.h,self.w,_ = self.img.shape

        #Define used fingers
        self.finger12 = self.coords[12]
        self.finger4 = self.coords[4]
        self.finger8 = self.coords[8]
        self.center = self.coords[9]

        #Variables for volume controlling
        self.devices = AudioUtilities.GetSpeakers()
        self.interface = self.devices.Activate(IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
        self.volume = self.interface.QueryInterface(IAudioEndpointVolume)

    def volume_control(self):


        #Volume control - Volume range - (-65.25, 0.0) / fingers range (20,80)
        cv2.line(self.img, (self.finger8[1],self.finger8[2]), (self.finger12[1],self.finger12[2]), (255, 0, 0), 5)
        vol_hand = np.linalg.norm(np.array([self.finger8[1],self.finger8[2]]) - np.array([self.finger12[1],self.finger12[2]]))
        vol = np.interp(vol_hand, [20,80], [-65.25,0])
        self.volume.SetMasterVolumeLevel(vol, None)
        return self.img

    def mouse_control(self):
        #Mouse controlling - moving mouse with hands movement
        cv2.rectangle(self.img, (100,100), (440,380), (0, 255, 0), 2)
        screen_x = np.interp(self.center[1], [100,self.w-200], [0,self.SCREEN_WIDTH] )
        screen_y = np.interp(self.center[2], [100,self.h-100], [0,self.SCREEN_HEIGHT])
        pyautogui.moveTo(screen_x, screen_y)

        #Controlling mouse clicking with 2 fingers
        if -20 < self.finger8[1]-self.finger4[1] < 20 and  -20 < self.finger8[2]-self.finger4[2] < 20:
            pyautogui.click()   
        return self.img

