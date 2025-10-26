# Import the OpenCV library
import cv2

# Load an image from the specified file path.
# "Resources/lena.png" is the path to the image file.
img = cv2.imread("Resources/lena.png")

# live video from a webcam (0 is usually the default camera).
# video_capture = cv2.VideoCapture(0)
# video_capture = cv2.VideoCapture(0)


# Create a new window to display the image.
# "DisplayImage" is the name of the window.
# 'img' is the variable containing the image data to be shown.
cv2.imshow("DisplayImage",img)

# Wait for a key to be pressed.
# The '0' argument means it will wait *indefinitely* until any key is pressed.
# This is a crucial step to keep the image window open until you are done.
cv2.waitKey(0)


# this command closes all the windows that were opened by OpenCV.
cv2.destroyAllWindows()
