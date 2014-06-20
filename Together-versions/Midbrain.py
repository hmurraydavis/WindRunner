import math
import bank

class Midbrain:
	
	## limit sail servo so it doesn't go out of mechanical bounds:
	def limitSailServo(self):
		sailDesired=bank.bank('sailDesired')
		if sailDesired >180:
			sailDesired=180
		if sailDesired<0:
			sailDesired=0
		
		print "The sail angle sent to the servo is:", sailDesired
	
	
	
	## limit stearing servo so it doesn't go out of mechanical bounds:
	def limitStearingServo(self):
		stearingDesired=bank.bank('stearingDesired')
		if stearingDesired >90:
			stearingDesired=90
		if stearingDesired<0:
			stearingDesired=0
		
		print "The sail angle sent to the servo is:", stearingDesired
		
		
	## Set sails to servo readable position: AKA: get from boat heading to servo position
	def sailDesToServoDes(self):
		#midbrain
		#converts from the sail theta to the equivelent theta for the sail winch
		import bank
		sailDesired=bank.bank('sailDesired')
		sailServoDesired= (sailDesired-20)/2
		print 'The servo set angle is: ' +str(sailServoDesired) + ' degrees'
		return sailServoDesired
		
		
	## set stearing to readable servo heading: AKA: convert from global coordinate heading into servo set angle.
	
	def stearingDestoStrSvoDes(self):
		stearingDesired=bank.bank('stearingDesired')
		currentHeading=bank.bank('currentHeading')
	
		print 'desired stearing is: ', stearingDesired
		print 'current heading is: ',currentHeading
	
		if stearingDesired>currentHeading: #bot needs to turn left!
			stearingServoDesired=45-(stearingDesired-currentHeading)
		
		if stearingDesired<currentHeading: #bot needs to turn right!
			stearingServoDesired=45+(currentHeading-stearingDesired)
		
		print 'desired servo stearing angle is: ',stearingServoDesired
		return stearingServoDesired
		
MB=Midbrain()
if __name__=='__main__':
	MB.stearingDestoStrSvoDes()
	MB.sailDesToServoDes()
	MB.limitStearingServo()
	MB.limitSailServo()
		
	
