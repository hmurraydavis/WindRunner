import cv2
import numpy as np

# Camera 0 is the integrated web cam on my netbook
camera_side = 1 #right Webcam
camera_back = 2
 
#Number of frames to throw away while the camera adjusts to light levels
ramp_frames = 30
 
#### Now we can initialize the camera capture object with the cv2.VideoCapture class.
#### All it needs is the index to a camera port.
camera_side = cv2.VideoCapture(camera_side)
#camera_back = cv2.VideoCapture(camera_back)

while(True):
    # Capture frame-by-frame
    ret, frame = camera_side.read()

    # Our operations on the frame come here
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Display the resulting frame
    cv2.imshow('frame',gray)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# When everything done, release the capture
camera_side.release()
cv2.destroyAllWindows()
