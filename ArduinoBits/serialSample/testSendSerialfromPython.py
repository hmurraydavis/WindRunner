import serial

arduino=serial.Serial('/dev/ttyACM0')
arduino.write("hoi\n")
