import sys, tty, termios
import serial

stearServo=45 #initialize to middle
sailServo=90 #initiialize to middle
arduino=serial.Serial('/dev/ttyACM1')
 
def read_char():
    '''
    Read a single character from a unix terminal and immediately return it.
    '''
    # grab a file descriptor
    fd = sys.stdin.fileno()
    old_settings = termios.tcgetattr(fd)
    try:
        # get naughty and set that terminal into raw mode
        tty.setraw(sys.stdin.fileno())
        # get acquainted with a lonesome character
        ch = sys.stdin.read(1)
    finally:
        # pretend we were never here
        termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
    return ch
 
if __name__ == '__main__':
    while True:
        # read in dat char
        c = read_char()
 
        # WOOP WOOP EMERGENCY ESCAPE
        if c == 'q':
            # make a fast getaway
            sys.exit()
        else:
            # tell it like it is
            print 'you entered:', c
            if c=='z': #pull sail in
            	sailServo=sailServo-1
            	if sailServo<0:
            		sailServo=0
            		print "Stop it! My sail is as far in as it will go!"
            	arduino.write("w%i\n"%sailServo)
            if c=='a': #let sail out
            	sailServo=sailServo+1
            	if sailServo>180:
            		sailServo=180
            		print "Stop it! My sail is as far out as it can go!"
            	arduino.write("w%i\n"%sailServo)
            if c=='x': #turn left
            	stearServo=stearServo+1
            	if stearServo>90:
            		stearServo=90
            		print "Stop it! I'm as far left as I can go!"
            	arduino.write("s%i\n"%stearServo)
            if c=='c': #turn right
            	stearServo=stearServo-1
            	if stearServo<0:
            		stearServo=0
            		print "Stop it! I'm as far right as I can go!"
            	arduino.write("s%i\n"%stearServo)
