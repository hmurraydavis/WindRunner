import bank
import math

def setSails():
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
setSails()
