import cv2
import numpy as np
import pprint

def make_image_mask(img):
    img = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY) 
    ret,thresh = cv2.threshold(img,80,255,cv2.THRESH_BINARY)
    return thresh

def save_video_frame(img):
    cv2.imwrite(img)
    
def get_side_video():
    ret, side_vid = camera_side.read()
    side_mask = make_image_mask(side_vid)
    (x,y),radius = cv2.minEnclosingCircle(side_mask)
    save_video_frame(side_vid)
    print 'Side pos = ', (x,y)
    return (x,y) 

# Camera 0 is the integrated web cam on my netbook
camera_side = 1 #right Webcam
camera_back = 2
 
#Number of frames to throw away while the camera adjusts to light levels
ramp_frames = 30
 
#### Now we can initialize the camera capture object with the cv2.VideoCapture class.
#### All it needs is the index to a camera port.
camera_side = cv2.VideoCapture(camera_side)
camera_back = cv2.VideoCapture(camera_back)

while(True):
    ret, frame = camera_side.read()
    side_mask = make_image_mask(frame)
    contours, hierarchy = cv2.findContours(side_mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
#    img = cv2.drawContours(thresh, contours, -1, (0,255,0), 3) 

    cnt = contours[0]
    (x,y),radius = cv2.minEnclosingCircle(cnt)
    center = (int(x),int(y))
    radius = int(radius)
    print 'center: ', center, 'radius: ', radius
    cat = cv2.circle(frame,center,radius,(0,255,0),5)
    cv2.imshow('frame',frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# When everything done, release the capture
camera_side.release()
cv2.destroyAllWindows()
