

# where all "global" variables are stored. A way of sharing data between all the dependednt functions

#get most recent data:
#def getsailCurrent(self):
#	sailCurrent=30
#	return sailCurrent

def getstearingCurrent():
	pass

def getposCurrent():
	pass

def getdist_to_object():
	pass

def getcurrentHeading():
	pass

def linstart():
	pass


#current variables:
sailDesired=-200

def bank(what):
	#sail servo:
	#sailCurrent=getsailCurrent()
	sailCurrent=60

	#stearing servo:
	stearingDesired=160
	stearingCurrent=0

	#position:
	posDesired=[200,950]
	posCurrent=[240,905]
	linstart=[237,900] #for line following
	
	dist_to_object=300 #distance from the bot to the next object

	#heading:
	currentHeading=150
	desiredHeading=160

	#wind
	currentWindHeading=300

	# return requested value:
	if what=='pastDist':
		return pastDist
	if what=='sailDesired':
		return sailDesired
	if what=='currentHeading':
		return currentHeading
	if what == 'desiredHeading':
		return desiredHeading
	if what == 'posDesired':
		return posDesired
	if what=='posCurrent':
		return posCurrent
	if what=='linstart':
		return linstart
	if what=='dist_to_object':
		return dist_to_object
	if what=='stearingDesired':
		return stearingDesired
	if what=='currentWindHeading':
		return currentWindHeading

def stearingCurrent():
	return stearingCurrent

def desiredHeading():
	return desiredHeading

def sailDesiredF():
	#print sailDesired
	return sailDesired
