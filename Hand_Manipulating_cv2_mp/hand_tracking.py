import cv2
import mediapipe as mp
import time

class HandDetector():
    def __init__(self):
        self.mp_hands = mp.solutions.hands
        self.hands = self.mp_hands.Hands()#Use default hyperparameters
        self.draw = mp.solutions.drawing_utils
    def findHands(self,img):

        imgRGB = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)#Only working with RGB
        self.results = self.hands.process(imgRGB)

        if self.results.multi_hand_landmarks:
            for hand_cor in self.results.multi_hand_landmarks:
                self.draw.draw_landmarks(img,hand_cor, self.mp_hands.HAND_CONNECTIONS)
        return img  
    
    def findPositions(self,img,parts,draw=True):
        '''
        To choose part of hand - write appropriate integer - https://developers.google.com/mediapipe/solutions/vision/hand_landmarker
        '''
        h,w,c = img.shape
        #During while - its clearing all the time and then is packed with new values
        CordsList=[]
        if self.results.multi_hand_landmarks:
            for hand_cor in self.results.multi_hand_landmarks:
                for id, cor in enumerate(hand_cor.landmark):
                    x = int(cor.x*w)
                    y=int(cor.y*h)
                    CordsList.append([id,x,y])
            if draw:
                if type(parts) == list:
                    for part in parts:
                        cv2.circle(img,CordsList[part][1:],15,(0,0,255),cv2.FILLED)    
                else:
                    cv2.circle(img,CordsList[parts][1:],15,(0,0,255),cv2.FILLED)    

        return CordsList
    