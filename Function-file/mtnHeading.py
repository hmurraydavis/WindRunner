def mtnHeading():
	# Keeps the robot on a desired heading 
	import bank
	currentHeading=bank.bank('currentHeading')
	desiredHeading=bank.bank('desiredHeading')
	print 'Current heading: ' + str(currentHeading)
	print 'Desired heading:' +str(desiredHeading)
	delta=abs((currentHeading-desiredHeading)/2)
	print 'Delta: '+ str(delta)
	if currentHeading > desiredHeading:
		desiredStearing=currentHeading-delta
		print 'desired greater than current'
	if currentHeading<desiredHeading:
		desiredStearing=currentHeading+delta
		print 'current greater than desired'
	
	print 'the desired stearing angle is: ' + str(desiredStearing)
	return desiredStearing

#mtnHeading()
