import bank

def limitStearingServo():
	sailDesired=bank.bank('sailDesired')
	if sailDesired >90:
		sailDesired=90
	if stearingDesired<0:
		sailDesired=0
		
	print "The sail angle sent to the servo is:", sailDesired
		
#limitStearingServo()
