# where all "global" variables are stored. A way of sharing data between all the dependednt functions

def getsailCurrent():
	pass
	
def getstearingCurrent():
	pass
	
def getposCurrent():
	pass
	
def getdist_to_object():
	pass

def getcurrentHeading():
	pass

def bank(what):
	#sail servo:
	sailDesired=25
	sailCurrent=getsailCurrent()
	sailCurrent=30 #remove when getsailCurrent works

	#stearing servo:
	stearingDesired=-5
	stearingCurrent=0

	#position:
	posDesired=[200,950]
	posCurrent=[240,905]
	linstart=[237,900] #for line following
		
	dist_to_object=300 #distance from the bot to the next object

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
	if what=='dist_to_object':
		return dist_to_object

def stearingCurrent():
	return stearingCurrent

def desiredHeading():
	return desiredHeading

def sailDesired():
	print sailDesired
	return sailDesired
