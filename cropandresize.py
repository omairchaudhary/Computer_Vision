import cv2 


image_path = "Resources/CarImage.jpg"

img = cv2.imread(image_path)


cv2.imshow("display window name", img)


cv2.waitKey(0)


cv2.destroyAllWindows()