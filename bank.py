# where all "global" variables are stored. A way of sharing data between all the dependednt functions

def bank(what):
	#sail:
	sailDesired=25
	sailCurrent=30

	#stearing servo:
	stearingDesired=-5
	stearingCurrent=0

	#position:
	posDesired=[200,950]
	posCurrent=[240,905]
	linstart=[237,900] #for line following
		
	pastDist=290 #needed????
	currentDist=300

	#heading:
	currentHeading=150
	desiredHeading=160

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

def stearingCurrent():
	return stearingCurrent

def desiredHeading():
	return desiredHeading

def sailDesired():
	print sailDesired
	return sailDesired
