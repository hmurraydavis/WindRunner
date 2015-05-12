import serial
import cv2
import numpy as np
import threading
import datetime
import time

testNum=8

#For collecting data for IRSC 2015 conference

write_file = 'spoof{}.txt'.format(testNum)
#Test 1 -- NA
#Test 2 -- luffing
#Test 3 -- holding shape
#Test 4 -- both/switch
#Test 5 -- holding shape
#Test 6 -- NA -- bad accl sensor_data
#Test 7 -- luffing
#Test 8 -- both 

# Camera 0 is the integrated web cam on my netbook
camera_side = 1 #right Webcam
camera_back = 0

#camera_bk_obj = cv2.VideoCapture(camera_back)
camera_side_obj = cv2.VideoCapture(camera_side)

#make ze global variables!!!
side_center=(0,0)
back_center=(0,0)
side_radius=0
back_radius=0

img_val=0


#Arduino serial connection
arduino=serial.Serial('/dev/ttyACM0')

def receiving(ser):
	buffer = ''
	while True:
		read_values = ser.read(ser.inWaiting())
		if '$' in read_values:
			buffer = read_values.split('$')[-1]
		else:
			buffer = buffer + read_values
		if '\n' in buffer:
			lines = buffer.split('\n')
			return lines[-2]

def make_image_mask(img):
#    img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) 
#    ret,thresh = cv2.threshold(img,40,255,cv2.THRESH_BINARY)
#         define range of blue color in HSV
    lower_blue = np.array([90,90,10])
    upper_blue = np.array([200,200,255])

    # Threshold the HSV image to get only blue colors
    thresh = cv2.inRange(img, lower_blue, upper_blue)
    return thresh

def save_video_frame(img):
    file_name='test{}image{}.jpg'.format(str(testNum), str(img_val))
    cv2.imwrite(file_name, img)
    global img_val
    file_name = img_val+1
    
    
def get_circle_sd():
    global side_center, side_radius
    
    ret, frame = camera_side_obj.read()
    save_video_frame(frame)
    
    side_mask = make_image_mask(frame)
    contours, hierarchy = cv2.findContours(side_mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    
    cnt = contours[0]
    (x,y),radius = cv2.minEnclosingCircle(cnt)
    side_center = (int(x),int(y))
    side_radius = int(radius)
    print 'center: ', side_center, 'radius: ', side_radius, ' found from side camera'
    cat = cv2.circle(frame,side_center,side_radius,(0,255,0),5)
    cat = cv2.circle(side_mask,side_center,side_radius,(0,255,0),5)
    cv2.imshow('frame',frame)
    cv2.imshow('mask',side_mask)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        exit()
    return (x,y), radius
    
def get_circle_bk():
    global back_center, back_radius
    
    ret, frame = camera_bk_obj.read()
    
    side_mask = make_image_mask(frame)
    contours, hierarchy = cv2.findContours(side_mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    
    cnt = contours[0]
    (x,y),radius = cv2.minEnclosingCircle(cnt)
    back_center = (int(x),int(y))
    back_radius = int(radius)
    print 'center: ', back_center, 'radius: ', back_radius, 'found from back camera'
    cat = cv2.circle(frame,back_center,back_radius,(0,255,0),5)
#    cv2.imshow('frame',frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        exit()
    
    return back_center, back_radius

			
#general methodology:
#   1. read in from arduino
#   2. Get centroid of light from webcam
#   3. Write both to file
#   4. Begin again!

while 1:
    try:
        #Read data in from the Arduino:
        print 'pre-arduino'
        sensor_data = receiving(arduino)
        print 'got dat arduino stuff'
        
        print datetime.datetime.now()
        #Read video frames in from the webcams:
        
        sdcenter, sdradius = get_circle_sd()

        with open(write_file, 'a') as f:
            dataString='Sc:'+str(sdcenter[0])+'|'+str(sdcenter[1])+' Sr:'+str(sdradius)+' '+sensor_data
            print dataString
            f.write(dataString)
            f.write('\n')
         
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    except KeyboardInterrupt as e:
        camera_side.release()
        cv2.destroyAllWindows()
        import traceback
        traceback.print_exc()
        exit()
    except IndexError as e:
        with open(write_file, 'a') as f:
            f.write('SOMETHING_WENT_WRONG')
            f.write('\n')
