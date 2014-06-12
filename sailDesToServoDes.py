def sailDesToServoDes():
	#midbrain
	#converts from the sail theta to the equivelent theta for the sail winch
	import bank
	sailDesired=bank.bank('sailDesired')
	sailServoDesired= (sailDesired-20)/2
	print 'The servo set angle is: ' +str(sailServoDesired) + ' degrees'
	return sailServoDesired
sailDesToServoDes()
