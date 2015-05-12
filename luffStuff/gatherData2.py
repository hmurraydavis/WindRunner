import serial
import cv2
import numpy as np

write_file = 'spoof3.txt'
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
camera_back = 2
 
#Number of frames to throw away while the camera adjusts to light levels
ramp_frames = 30
 
#### Now we can initialize the camera capture object with the cv2.VideoCapture class.
#### All it needs is the index to a camera port.
camera_side = cv2.VideoCapture(camera_side)
camera_back = cv2.VideoCapture(camera_back)


#For collecting data for IRSC 2015 conference

#Arduino serial connection
arduino=serial.Serial('/dev/ttyACM1')

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
    img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) 
    ret,thresh = cv2.threshold(img,80,255,cv2.THRESH_BINARY)
    return thresh

def save_video_frame(img):
    cv2.imwrite(img)
    
def get_side_video():
    ret, side_vid = camera_side.read()
    return side_vid
    
def get_back_video():
    ret, back_vid = camera_back.read()
    back_mask = make_image_mask(back_vid)
    (x,y),radius = cv2.minEnclosingCircle(back_mask)
    save_video_frame(back_vid)
    print 'Back pos = ', (x,y)
    return (x,y) 

			
#general methodology:
#   1. read in from arduino
#   2. Get centroid of light from webcam
#   3. Write both to file
#   4. Begin again!

while 1:
    try:
        #Read data in from the Arduino:
        sensor_data = receiving(arduino)
        
        #Read video frames in from the webcams:
        __error_code, side_frame = camera_side.read()
        cv2.imshow('side frame', side_frame)
        __error_code, back_frame = camera_back.read()
        cv2.imshow('back frame', back_frame)
        
#        side_mask = make_image_mask(side_frame)
        
        #Camera color mask and circle finding!

###        with open(write_file, 'a') as f:
###            dataString=sensor_data+',S:'+side_pos+',B:'+back_pos
###            print dataString
###            f.write(sensor_data)
###            f.write('\n')
         
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
        camera_side.release()
        cv2.destroyAllWindows()
