###########import cv2
###########import matplotlib.pyplot as plt
###########import numpy as np




def make_image_mask(img):
#    img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) 
#    ret,thresh = cv2.threshold(img,40,255,cv2.THRESH_BINARY)
#         define range of blue color in HSV
    lower_blue = np.array([80,20,10])
    upper_blue = np.array([180,180,255])

    # Threshold the HSV image to get only blue colors
    thresh = cv2.inRange(img, lower_blue, upper_blue)
    return thresh

def get_circle(frame):    
    side_mask = make_image_mask(frame)
    contours, hierarchy = cv2.findContours(side_mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    
    cnt = contours[0]
    (x,y),radius = cv2.minEnclosingCircle(cnt)
    side_center = (int(x),int(y))
    side_radius = int(radius)
    #print 'center: ', side_center, 'radius: ', side_radius, ' found from side camera'
    
    return side_center, radius

###for img_val in range(start_val,end_val):
###    file_name='5-11_data_collection/test{}/test{}image{}.jpg'.format(str(testNum), str(testNum), str(img_val))
###    img = cv2.imread(file_name)
###    cv2.imwrite('image.jpg',img)
###    cv2.imshow('saved img', cv2.imread('image.jpg'))
###    if cv2.waitKey(1) & 0xFF == ord('q'):
###        exit()
####    get_circle(img)

###########cv2.destroyAllWindows()


import cv2
import numpy as np
import time

testNum=21

start_val=0
end_val = 100

for i in range(start_val,end_val):
    # Capture frame-by-frame
    frame = cv2.imread('5-11_data_collection/test21/test21image{}.jpg'.format(str(i)))

    # Our operations on the frame come here
    #gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    center, radius = get_circle(frame)
    radius = int(radius)
    print center , radius
    img = cv2.circle(frame,center,radius,(0,255,0),2)
    # Display the resulting frame
    cv2.imshow('frame',frame)
    time.sleep(.5)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        print 'hi'

# When everything done, release the capture
cv2.destroyAllWindows()
