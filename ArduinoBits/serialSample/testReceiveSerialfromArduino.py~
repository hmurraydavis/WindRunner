import serial


arduino=serial.Serial('/dev/ttyACM0')
echo=arduino.readline()
print echo
while echo=="/n":
	print "hi"
	echo=arduino.readline()
	print "read in: ",echo
