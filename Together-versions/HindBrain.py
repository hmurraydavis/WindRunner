import bank

class Hindbrain:

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
		pass
		
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
