import serial
import time

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

print "hello, there!"
send = 'd\n'
arduino.write(send)
platypus=receiving(arduino);
print (platypus)

send='c\n'
arduino.write(send)
print (receiving(arduino))


