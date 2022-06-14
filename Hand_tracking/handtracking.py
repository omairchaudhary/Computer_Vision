#import libraries
import cv2 as cv
import mediapipe as mp
import time

VideoCapture = cv.VideoCapture(0)
myhand = mp.solutions.hands
hands = myhand.Hands()
mpDraw = mp.solutions.drawing_utils
pTime = 0
cTime = 0


while True:
    success, img = VideoCapture.read()
    imgrgb = cv.cvtColor(img,cv.COLOR_BGR2RGB)

    result = hands.process(imgrgb)

    if result.multi_hand_landmarks:
      for handLms in result.multi_hand_landmarks:
         mpDraw.draw_landmarks(img,handLms,myhand.HAND_CONNECTIONS)  
    
    cTime =time.time()
    fps = 1/(cTime-pTime)
    pTime = cTime

    cv.putText(img,str(int(fps)),(10,70),cv.FONT_HERSHEY_PLAIN,3,(255,0,255),3)    
    cv.imshow("handtracking",img)
    cv.waitKey(1)

