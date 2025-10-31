# Import the OpenCV library
import cv2

FrameWidth = 640
FrameHeight = 350

# Load an image from the specified file path.
# img = cv2.imread("Resources/lena.png")

Read_video = cv2.VideoCapture("Resources/video.mp4")

# Read_video = cv2.VideoCapture(0)
# Read_video.set(3,FrameWidth)
# Read_video.set(4,FrameHeight)

while True:
    success, img =Read_video.read()
    img = cv2.resize(img, (FrameWidth,FrameHeight))
    # Create a new window to display the image.
    cv2.imshow("DisplayImage",img)
    
    # Wait for a key to be pressed.
    # The '0' argument means it will wait *indefinitely* until any key is pressed.
    # This is a crucial step to keep the image window open until you are done.
    if cv2.waitKey(1) & 0xFF ==ord('q'):
        break
# this command closes all the windows that were opened by OpenCV.
cv2.destroyAllWindows()
