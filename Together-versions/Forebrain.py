class Forebrain:
	import math
	import bank #delete when final
	
	
	## sail setting!
	def setSails():
		# '''Sets the sails to the correct location for the wind data coming in. '''
		currentWindHeading=bank.bank('currentWindHeading')
		currentHeading=bank.bank('currentHeading')
		print 'current wind heading is: ', currentWindHeading
		print 'Current bot heading is: ', currentHeading
	
		windAngle=math.fabs(currentWindHeading-currentHeading)
		if windAngle>180:
			windAngle=math.fabs(windAngle-360)
		print 'calculated wind angle is:', windAngle
	
		if windAngle<0:
			print 'Error: negative wind angle!'
			sailDesired=40
		if windAngle<45:
			print 'Bot is in irons!'
			#outOfIrons()
		if (windAngle<180) & (windAngle>45):
			sailDesired=(.75*windAngle)-30
		if windAngle>180:
			sailDesired=90
			print 'Error: wind angle over 180 degrees'
		print 'Desired sail angle is: ', sailDesired
		return sailDesired
		
	
	## Going to ppoints!
	def slope(p2,p1):
		# '''gives the slope of the line to be followed
		#tested to work 12:45 PM, 6/11/14 '''
		m=float(p2[1]-p1[1])/float(p2[0]-p1[0])
		#print 'Slope is: ' + str(m)
		return m

	def headingToPoint():
		#'''gives the heading (angle in degrees from the +x axis) of the line to be followed'''

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
		# '''outputs the necessary, global heading in order to go toward a point'''

		currentHeading=bank.bank('currentHeading')
		headingtoPoint=headingToPoint()
		print 'currentHeading' +str(currentHeading)
		print 'headingtoPoint' +str(headingtoPoint)
	
		desiredHeading=float(currentHeading+headingtoPoint)/2
		print 'the desire heading is:'+str(desiredHeading)
		return desiredHeading
		
		
	## Following lines!
	def slope(posDesired,linstart):
		# '''gives the slope of the line to be followed
		#tested to work 12:45 PM, 6/11/14'''
		import bank
		m=float(posDesired[1]-linstart[1])/float(posDesired[0]-linstart[0])
		#print 'Slope is: ' + str(m)
		return m

	def heading_line():
		#'''gives the heading (angle in degrees from the +x axis) of the line to be followed'''

		linstart=bank.bank('linstart')
		posDesired=bank.bank('posDesired')
		m=slope(posDesired,linstart)
		angle=math.degrees(math.atan(m/1))

		xcheck=(posDesired[0]-linstart[0])>0#if true, in I or IV
		ycheck=(posDesired[1]-linstart[1])>0#if true, in I or II
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


	def above_below_on_line():
		# '''gives whether the bot is above, below, or on the line it should be following.
		#tested to work at 13:14 on 6/11/14
		# Based on: http://math.stackexchange.com/questions/324589/detecting-whether-a-point-is-above-or-below-a-slope'''

		posCurrent=bank.bank('posCurrent')
		posDesired=bank.bank('posDesired')
		linstart=bank.bank('linstart')
		m=slope(posDesired, linstart)
		b=posDesired[1]-(m*posDesired[0])
		check=m*posCurrent[0]+b
		if check<posCurrent[1]:
			print 'Bot is above the line'
			return 'above'
		if check>posCurrent[1]:
			print 'Bot is below the line'
			return 'below'
		if check == posCurrent[1]:
			print 'Bot is on the line!'
			return 'on'
	

	def followLine():
		# '''Outputs the necessary, global heading for the robot to follow a line with specified endpoints'''
		
		bot_posVlin=above_below_on_line()
		lineheading=heading_line()
		botheading=bank.bank('currentHeading')
		print 'Line heading: '+str(lineheading)
		print 'Bot heading: '+str(botheading)
		
		#check through possible cases and assign the correct, desired, global heading accordingly
		if (bot_posVlin=='above') & (botheading>lineheading): #above line and heading away from it.
			print 'Bot above and heading away from line to be followed'
			headDesired=((lineheading-botheading)/2)+lineheading

		if (bot_posVlin=='below') & (botheading>lineheading): #below line and heading toward it.
			print 'Bot below and heading away from line to be followed'
			headDesired=((lineheading-botheading)/2)+lineheading

		if (bot_posVlin=='below') & (botheading<lineheading): #below line and heading away from it. 
			print 'Bot below and heading toward from line to be followed'
			headDesired=lineheading-math.fabs((lineheading-botheading)/2)

		if (bot_posVlin=='above') & (botheading<lineheading): #above line and heading toward it.
			print 'Bot above and heading toward from line to be followed'
			headDesired=lineheading-math.fabs((lineheading-botheading)/2)
		if bot_posVlin=='on': #on line! :)
			print 'Bot is on the line to be followed!'
			headDesired=lineheading
			
			
		print 'The desired heading for the bot is:' + str(headDesired)
		return headDesired



	## Maintaining heading!
	def mtnHeading():
		# '''Keeps the robot on a desired heading. Output: desired, global heading'''
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
		
		
	## Avoid obstacles!
	def obsAvoid():
		# '''works with IR sensor to avoid obstacles. Essentially integral control.'''
	
		dist_to_object=bank.bank('dist_to_object') #distance to object from PIR/Sharp sensor
		if  dist_to_object >50:
			print "Servo moving necessary so I don't hit a rock!"
			stearingDesired = 30*dist_to_object/256; 
			#sailDesired = bank.bank('sailDesired') + 1
			sailDesired=bank.sailDesiredF()
			print 'desired stearing is: ' + str(stearingDesired) + ' degrees'
			print 'desired sail is: ' + str(sailDesired) + ' degrees'
			return (stearingDesired, sailDesired)
	
	
