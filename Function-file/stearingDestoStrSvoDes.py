import bank


def stearingDestoStrSvoDes():
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
	
	
stearingDestoStrSvoDes()
	
