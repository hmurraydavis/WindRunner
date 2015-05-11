import serial
import cv2

write_file = 'test8.txt'
#Test 1 -- NA
#Test 2 -- luffing
#Test 3 -- holding shape
#Test 4 -- both/switch
#Test 5 -- holding shape
#Test 6 -- NA -- bad accl sensor_data
#Test 7 -- luffing
#Test 8 -- both 




#For collecting data for IRSC 2015 conference

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
			
#general methodology:
#   1. read in from arduino
#   2. Get centroid of light from webcam
#   3. Write both to file
#   4. Begin again!

while 1:
    sensor_data = receiving(arduino)
    print sensor_data

    with open(write_file, 'a') as f:
        f.write(sensor_data)
        f.write('\n')
