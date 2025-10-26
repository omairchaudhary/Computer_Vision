import re
import cv2 as cv
from numpy import true_divide

#loading the cascade 
face_cascade = cv.CascadeClassifier('haarcascade_frontalface_default.xml')
eye_cascade = cv.CascadeClassifier('haarcascade_eye.xml')


#function for detection faces
def detect(gray,frame):
    faces = face_cascade.detectMultiScale(gray,1.3,5)
    for (x,y,w,h) in faces:
        cv.rectangle(frame,(x,y),(x+w,y+h),(255,0,0),2)
        roi_gray = gray[y:y+h, x:x+w]
        roi_color = frame[y:y+h , x:x+h]
        eye = eye_cascade.detectMultiScale(roi_gray,1.1,2)
        for (ex,ey,ew,eh) in eye:
            cv.rectangle(roi_color,(ex,ey),(ex+ew, ey+eh),(0,255,0),2)

    return frame


video_capture = cv.VideoCapture(0)
while True:
    _,frame = video_capture.read()
    gray = cv.cvtColor(frame,cv.COLOR_BGR2GRAY)
    canvas = detect(gray,frame)
    cv.imshow("myvideo",canvas)

    if cv.waitKey(1) & 0xFF == ord('q'):
        break

video_capture.release()
cv.destroyAllWindows()
cv.waitKey(1)