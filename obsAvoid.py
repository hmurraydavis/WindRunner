def obsAvoid():
	#works with PIR sensor to avoid obstacles. Essentially integral control.
	import bank
	
	dist_to_object=bank.bank('dist_to_object') #distance to object from PIR/Sharp sensor
	if  dist_to_object >50:
		print "Servo moving necessary so I don't hit a rock!"
		stearingDesired = 30*dist_to_object/256; 
		#sailDesired = bank.bank('sailDesired') + 1
		sailDesired=bank.sailDesired()
		print 'desired stearing is: ' + str(stearingDesired) + ' degrees'
		print 'desired sail is: ' + str(sailDesired) + ' degrees'
		return (stearingDesired, sailDesired)





obsAvoid()
