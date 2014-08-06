import serial
import time

#Arduino serial connection
arduino=serial.Serial('/dev/ttyACM0')

#send = 'd\n'
#arduino.write(send)

def receiving0(ser):
    global last_received

    buffer = ''
    last_received='\n'
    while last_received=='\n':
        buffer = buffer + ser.read(ser.inWaiting())
        if '\n' in buffer:
            lines = buffer.split('\n') # Guaranteed to have at least 2 entries
            last_received = lines[-2]
            #If the Arduino sends lots of empty lines, you'll lose the
            #last filled line, so you could make the above statement conditional
            #like so: if lines[-2]: last_received = lines[-2]
            print last_received
            buffer = lines[-1]
            
def receivingE(ser):
    buffer = ''
    while True:
        buffer = buffer + ser.read(ser.inWaiting())
        if '\n' in buffer:
            lines = buffer.split('\n')
            return lines[-2]
            
            
def receivingSO(ser):
    global last_received

    buffer = ''
    while True:
        buffer = buffer + ser.read(ser.inWaiting())
        if '\n' in buffer:
            lines = buffer.split('\n') # Guaranteed to have at least 2 entries
            last_received = lines[-2]
            #If the Arduino sends lots of empty lines, you'll lose the
            #last filled line, so you could make the above statement conditional
            #like so: if lines[-2]: last_received = lines[-2]
            buffer = lines[-1]
            print last_received

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

for i in range(15):
	print (receiving(arduino))


def crap():
	readIn=False
	count=0
	air=[]

	red=arduino.read()
	air+=red
	red=arduino.read()
	air+=red
	red=arduino.read()
	air+=red
	red=arduino.read()
	air+=red
	red=arduino.read()
	air+=red

	print air
