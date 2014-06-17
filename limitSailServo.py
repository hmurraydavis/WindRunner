import bank

def limitSailServo():
	sailDesired=bank.bank('sailDesired')
	if sailDesired >180:
		sailDesired=180
	if sailDesired<0:
		sailDesired=0
		
	print "The sail angle sent to the servo is:", sailDesired
		
limitSailServo()
