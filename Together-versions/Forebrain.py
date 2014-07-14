import math
#import bank #delete when final
from Midbrain import Midbrain

class Forebrain:	
	def __init__(self):
		self.midbrain=Midbrain()
		
	def test1(self):
		self.midbrain.limitSailServo()
	
	## sail setting!
	def setSails(self):
		# '''Sets the sails to the correct location for the wind data coming in. '''
		currentWindHeading = self.midbrain.readWindDirecrion()
		currentHeading = self.midbrain.readHeading()
		print 'current wind heading is: ', currentWindHeading
		print 'Current bot heading is: ', currentHeading
	
		windAngle=math.fabs(currentWindHeading-currentHeading)
		if windAngle>180:
			windAngle=math.fabs(windAngle-360)
		print 'calculated wind angle is:', windAngle
	
		if windAngle<0:
			print 'Error: negative wind angle!'
			sailDesired=40
		elif windAngle<45:
			print 'Bot is in irons!'
			sailDesired=40
			#outOfIrons()
		if (windAngle<180) & (windAngle>45):
			sailDesired=(.75*windAngle)-30
		if windAngle>180:
			sailDesired=90
			print 'Error: wind angle over 180 degrees'
		print 'Desired sail angle is: ', sailDesired
		return sailDesired
		
	
	## Going to ppoints!
	def slope(self,p2,p1):
		# '''gives the slope of the line to be followed
		#tested to work 12:45 PM, 6/11/14 '''
		m=float(p2[1]-p1[1])/float(p2[0]-p1[0])
		#print 'Slope is: ' + str(m)
		return m

	def headingToPoint(self,posDesired):
		#'''gives the heading (angle in degrees from the +x axis) of the line to be followed'''

		posCurrent = self.midbrain.readPosition() #robot's current position
		m=self.slope(posDesired,posCurrent)
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

	def goToPoint(self,pt):
		# '''outputs the necessary, global heading in order to go toward a point'''

		currentHeading = self.midbrain.readHeading()
		headingtoPoint=self.headingToPoint(pt)
		print 'currentHeading' +str(currentHeading)
		print 'headingtoPoint' +str(headingtoPoint)
	
		desiredHeading=float(currentHeading+headingtoPoint)/2
		print 'the desire heading is:'+str(desiredHeading)
		return desiredHeading
		
		
	## Following lines!
	#def slope(self,posDesired,linstart):
		# '''gives the slope of the line to be followed
		#tested to work 12:45 PM, 6/11/14'''
	#	m=float(posDesired[1]-linstart[1])/float(posDesired[0]-linstart[0])
		#print 'Slope is: ' + str(m)
	#	return m

	def heading_line(self,linstart,posDesired):
		#'''gives the heading (angle in degrees from the +x axis) of the line to be followed'''

		m=self.slope(posDesired,linstart)
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


	def above_below_on_line(self,posCurrent,linstart,posDesired):
		# '''gives whether the bot is above, below, or on the line it should be following.
		#tested to work at 13:14 on 6/11/14
		# Based on: http://math.stackexchange.com/questions/324589/detecting-whether-a-point-is-above-or-below-a-slope'''

		posCurrent = self.midbrain.readPosition()
		m=self.slope(posDesired, linstart)
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
	

	def followLine(self,linstart,posDesired):
		# '''Outputs the necessary, global heading for the robot to follow a line with specified endpoints'''
		
		posCurrent=self.midbrain.readPosition()
		bot_posVlin=self.above_below_on_line(posCurrent,linstart,posDesired)
		lineheading=self.heading_line(linstart,posDesired)
		botheading = self.midbrain.readHeading()
		print 'Line heading: '+str(lineheading)
		print 'Bot heading: '+str(botheading)
		print 'bot_posVlin', bot_posVlin
		
		#check through possible cases and assign the correct, desired, global heading accordingly
		if (bot_posVlin=='above') & (botheading>lineheading): #above line and heading away from it.
			print 'Bot above and heading away from line to be followed'
			headDesired=((lineheading-botheading)/2)+lineheading

		elif (bot_posVlin=='below') & (botheading>lineheading): #below line and heading toward it.
			print 'Bot below and heading away from line to be followed'
			headDesired=((lineheading-botheading)/2)+lineheading

		elif (bot_posVlin=='below') & (botheading<lineheading): #below line and heading away from it. 
			print 'Bot below and heading toward from line to be followed'
			headDesired=lineheading-math.fabs((lineheading-botheading)/2)

		elif (bot_posVlin=='above') & (botheading<lineheading): #above line and heading toward it.
			print 'Bot above and heading toward from line to be followed'
			headDesired=lineheading-math.fabs((lineheading-botheading)/2)
		elif bot_posVlin=='on': #on line! :)
			print 'Bot is on the line to be followed!'
			headDesired=lineheading
			
			
		print 'The desired heading for the bot is:' + str(headDesired)
		return headDesired



	## Maintaining heading!
	def mtnHeading(self, desiredHeading):
		# '''Keeps the robot on a desired heading. Output: desired, global heading'''
		#currentHeading = self.midbrain.readHeading()
		currentHeading=45; ###TODO: uncomment when the hindbrain compas sensors come in and work
		print 'Current heading: ' + str(currentHeading)
		print 'Desired heading:' +str(desiredHeading)
		delta=abs((currentHeading-desiredHeading)/2)
		print 'Delta: '+ str(delta)
		if currentHeading > desiredHeading:
			desiredStearing=currentHeading-delta
			print 'desired greater than current'
		elif currentHeading<desiredHeading:
			desiredStearing=currentHeading+delta
			print 'current greater than desired'
		elif currentHeading==desiredHeading:
			desiredStearing=currentHeading
			print 'current heading is the desired heading'
			
	
		print 'the desired stearing angle is: ' + str(desiredStearing)
		return desiredStearing
		
		
	## Avoid obstacles!
	def obsAvoid(self):
		# '''works with IR sensor to avoid obstacles. Essentially integral control.'''
	
		dist_to_object=self.midbrain.readIR1() #distance to object from PIR/Sharp sensor
		if  dist_to_object >50:
			print "Servo moving necessary so I don't hit a rock!"
			stearingDesired = 30*dist_to_object/256; 
			sailDesired=self.setSails()
			print 'desired stearing is: ' + str(stearingDesired) + ' degrees'
			print 'desired sail is: ' + str(sailDesired) + ' degrees'
			return (stearingDesired, sailDesired)
			
	def readPosition(self):
		'''reads the current GPS position off the robot via the hindbrain's method'''
		return self.midbrain.readPosition()
	
if __name__=='__main__':
	FB=Forebrain()
	FB.readPosition()
	FB.obsAvoid()
	FB.mtnHeading(45)
	FB.followLine([3,4],[1,0]) #followLine(self,posCurrent,linstart,posDesired):
	FB.above_below_on_line([3,4],[1,0],[9,10])
	FB.heading_line([1,0],[9,10]) #heading_line(self,linstart,posDesired)
	FB.headingToPoint([9,10])
	FB.setSails()
	
	#print ("test 1:")
	#FB.test1()
	
