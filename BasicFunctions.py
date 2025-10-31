import cv2

import numpy as np


kernal = np.ones((5,5), np.uint8)


path = "Resources/lena.png"

img = cv2.imread(path)

imgGray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

imgBlur = cv2.GaussianBlur(imgGray,(5,5),0)

imgCanny = cv2.Canny(imgGray,100,100)

imgDilation = cv2.dilate(imgCanny,kernal, iterations=1)

imgerode = cv2.erode(imgDilation,kernal, iterations=1)

cv2.imshow("Image",img)
cv2.imshow("GrayImage",imgGray)
cv2.imshow("GaussianBlur",imgBlur)
cv2.imshow("ImgCANNY",imgCanny)
cv2.imshow("ImgDilation",imgDilation)
cv2.imshow("ImgErode",imgerode)


cv2.waitKey() & 0xFF == ord('q')

cv2.destroyAllWindows()