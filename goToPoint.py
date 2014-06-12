def slope(p2,p1):
	#gives the slope of the line to be followed
	#tested to work 12:45 PM, 6/11/14
	import bank
	m=float(p2[1]-p1[1])/float(p2[0]-p1[0])
	#print 'Slope is: ' + str(m)
	return m

def headingToPoint():
	#gives the heading (angle in degrees from the +x axis) of the line to be followed
	import bank
	import math

	posCurrent=bank.bank('posCurrent') #robot's current position
	posDesired=bank.bank('posDesired') #waypoint going toward
	m=slope(posDesired,posCurrent)
	angle=math.degrees(math.atan(m/1))

	xcheck=(posDesired[0]-posCurrent[0])>0#if true, in I or IV
	ycheck=(posDesired[1]-posCurrent[1])>0#if true, in I or II
	#print 'x check: ' +str(xcheck) + '. y check:' +str(ycheck)+'.'

	if (ycheck==True) & (xcheck==False):  #quadrent 2
		angle=90+math.fabs(angle)
		#print 'Boat should be traveling into quadrent 2!'

	if  (xcheck==True) & (ycheck==False): #quadrent 4
		angle=270+math.fabs(angle)
		#print 'Boat should be heading into quadrent 4!'

	if (xcheck==False) & (ycheck==False): #quadrent 3
		angle =180+math.fabs(angle)
		#print 'Boat should be heading into quadrent 3!'
	#if quadrent 1, the angle doesn't need to be parsed.

	return angle

def goToPoint():
	import bank

	currentHeading=bank.bank('currentHeading')
	headingtoPoint=headingToPoint()
	print 'currentHeading' +str(currentHeading)
	print 'headingtoPoint' +str(headingtoPoint)
	
	desiredHeading=float(currentHeading+headingtoPoint)/2
	print 'the desire heading is:'+str(desiredHeading)
	return desiredHeading

goToPoint()
