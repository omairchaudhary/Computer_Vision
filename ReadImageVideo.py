import cv2

img = cv2.imread("Resources/lena.png")
# video_capture = cv2.VideoCapture(0)

cv2.imshow("DisplayImage",img)


cv2.waitKey(0)

cv2.destroyAllWindows()
