import bank
import serial
import binascii

class Hindbrain:
	
	def __init__(self):
		#self.GPS=serial.Serial ('/dev/ttyO1') #uncomment when on BB
		
		#Arduino serial connection
		self.arduino=serial.Serial('/dev/ttyACM0') #uncomment when arduino is connected
		
		self.count=0
		pass # comment when GPS or Arduino is connected
	
	def moveSailServos(self,sailServoAngle):
		# '''Moves the sail winch servo to the desired location'''
		send = 'w{angle}\n'.format(angle=sailServoAngle)
		self.arduino.write(send)
		print send
		
		echo=self.arduino.readline()
		check = echo == (':)'+send)
		if True==check:
			print 'Sail winch received set angle. :)'
		if False==check:
			print 'Error--Sail winch not receiving set angle. :('
			#raise IOError('Sail winch not receiving set angle')
		pass
		
	def moveStearServo(self, stearServoAngle):
		# '''Moves the stearing servo to the desired angle'''
		send='s%i\n' %stearServoAngle
		self.arduino.write(send)
		print send
		
		echo=self.arduino.readline()
		check = echo == (':)'+send)
		if True==check:
			print 'Steer servo received set angle. :)'
		if False==check:
			print 'Error--Steer servo not receiving set angle. :('
			#raise IOError('Steer servo not receiving set angle')
		pass
		
	def readTilt(self):
		# '''Read the current tild of the robot off the horizontal from the gyroscope'''
		send='g\n'
		self.arduino.write(send)
		print send
		
		echo=self.arduino.readline()
		check = echo.startswith(send)
		if True==check:
			print 'Tilt sensor read from. :)'
		if False==check:
			print 'Error--tilt sensor not reading. :('
			#raise IOError('tilt sensor not reading.')
		return 45 #pretend tilt
		pass
		
	def readPosition(self):
		# '''Reads the current GPS position from the GPS chip.'''
		#data=self.GPS.readline() #uncomment when on BB
		
		#test data set: 
		data='$GPGGA,001038.00,3334.2313457,S,11211.0576940,W,2,04,5.4,354.682,M,-26.574,M,7.0,0138*74' #comment out when on BB
		ckStng=data[1:data[14].find('*')-2]

		ckSum=0
		for i in ckStng:
			ckSum = ckSum ^ ord(i)
		#print 'Check sum caluclated: hex:', hex(ckSum), 'dec:', ckSum
		data=data.split(',')
		ckSumSat=data[14].split('*')

		
		#if str(hex(ckSum)) != '0x'+str(ckSumSat[1]): #use  check sum from GPS vs calculated to verify string isn't corrupted:
			#print 'Check Sum Error from the GPS! :('
			#positionUse=bank.bank('posPast')
			#return positionUse
			
		if False: #TODO: uncomment above checksum stuff, delete this placeholder
			pass 
			
		else: #if the GPS string isn't corrupted, use it:
			print 'Good GPS data! :)'					
			if data[6]==0: #if there isn't a GPS lock, assume the robot hasn't moved
				print 'No GPS Lock! :('
				positionUse=bank.bank('posPast')
				return positionUse
				
			if data[6]==1:
				print 'GPS fix!'
			if data[6]==2:
				print 'DGPS fix!'
				
			latitude=data[2]
			longitude=data[4]
			latitude=int(latitude[:2])+(float(latitude[2:])/60)
			if data[3]=='S': #convert to negative if on the negative side of the earth
				latitude=latitude*-1
			longitude=int(longitude[:2])+(float(longitude[2:])/60)
			if data[5]=='W': #convert to negative if on the negative side of the world
				longitude=longitude*-1
			print 'Processed latitude:',latitude
			print 'Processed longitude:',longitude
			#return [latitude,longitude]	#TODO: uncomment when are actually using GPS data
			return [0,1]
		
		
	def readHeading(self):
		# '''Read the current, global heading of the robot from the compass'''
				# '''Read the current tild of the robot off the horizontal from the gyroscope'''
		send='c\n'
		self.arduino.write(send)
		print send
		
		echo=self.arduino.readline()		
		check = echo.startswith(send)
		if True==check:
			print 'Compass read from. :)'
		if False==check:
			print 'Error--compass not reading. :('
			#raise IOError('Compass not reading.')	
		return 45 #pretend value for now. #TODO get returned arduino value	
		pass
		
	def readObstacle1(self):
		# '''Read from the standard IR sensor if there is an obstacle in front of the robot.'''
		
		send='i\n'
		self.arduino.write(send)
		print send
		
		echo=self.arduino.readline()		
		check = echo.startswith(send)
		if True==check:
			print 'IR Range 1 read from. :)'
		if False==check:
			print 'Error--IR Range 1 not reading. :('
			#raise IOError('IR Range 1 not reading.')	
		return 100 #TODO return actual dist to obstacle
		pass
		
	def readWindDirecrion(self):
		# ''' Read in the current, global, apparent wind direction from the wind sensor (compass)'''
		
		send='d\n'
		self.arduino.write(send)
		print send
		
		echo=self.arduino.readline()		
		check = echo.startswith(send)
		if True==check:
			print 'Wind direction read from. :)'
		if False==check:
			print 'Error--Wind direction not reading. :('
			#raise IOError('IR Range 1 not reading.')
		return 60 #TODO return actual wind direction from arduino
		pass
		
	def dontHitThat(self):
		#'''Called by readObstacle if bot gets too close to an obstacle so it won't hit it. Puts servo to one side'''
		pass
		
	def dontFallOver(self):
		# '''Called by readTilt if the bot tilts to the point of flipping over. Will let the sail servo all the way out.'''
		pass
		
if __name__=='__main__':
	HB=Hindbrain()
	HB.readPosition()
	HB.moveSailServos(40)
	HB.moveStearServo(50)
	HB.readTilt()
	HB.readHeading()
	HB.readObstacle1()
	HB.readWindDirecrion()
