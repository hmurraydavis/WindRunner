#import bank
import serial

class Hindbrain:
	#def __init__(self):
	#	self.GPS=serial.Serial ('/dev/ttyO1')
	
	def moveSailServos(self,sailServoAngle):
		# '''Moves the sail winch servo to the desired location'''
		pass
		
	def moveStearServo(self, stearServoAngle):
		# '''Moves the stearing servo to the desired angle'''
		pass
		
	def readTilt(self):
		# '''Read the current tild of the robot off the horizontal from the gyroscope'''
		pass
		
	def readPosition(self):
		# '''Reads the current GPS position from the GPS chip.'''
		
		#data=self.GPS.readline()
		data='$GPGGA,001038.00,3334.2313457,S,11211.0576940,W,2,04,5.4,354.682,M,-26.574,M,7.0,0138*79'
		data=data.split(',')
		#print data
		latitude=data[2]
		print 'latitude: ',latitude
		longitude=data[4]
		#print 'degrees: ', latitude[:2]
		#print 'minuites: ',latitude[2:]
		latitude=int(latitude[:2])+(float(latitude[2:])/60)
		if data[3]=='S':
			latitude=latitude*-1
		longitude=int(longitude[:2])+(float(longitude[2:])/60)
		if data[5]=='W':
			longitude=longitude*-1
		print 'Processed latitude:',latitude
		print 'Processed longitude:',longitude
		
		
		
		
	def readHeading(self):
		# '''Read the current, global heading of the robot from the compass'''
		pass
		
	def readObstacle(self):
		# '''Read from the standard IR sensor if there is an obstacle in front of the robot.'''
		pass
		
	def readWindDirecrion(self):
		# ''' Read in the current, global, apparent wind direction from the wind sensor (compass)'''
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
		
