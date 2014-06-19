def slope(posDesired,linstart):
	#gives the slope of the line to be followed
	#tested to work 12:45 PM, 6/11/14
	import bank
	m=float(posDesired[1]-linstart[1])/float(posDesired[0]-linstart[0])
	#print 'Slope is: ' + str(m)
	return m

def heading_line():
	#gives the heading (angle in degrees from the +x axis) of the line to be followed
	import bank
	import math
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
	# gives whether the bot is above, below, or on the line it should be following.
	#tested to work at 13:14 on 6/11/14
	# Based on: http://math.stackexchange.com/questions/324589/detecting-whether-a-point-is-above-or-below-a-slope
	import bank
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
	import bank
	import math
	
	bot_posVlin=above_below_on_line()
	lineheading=heading_line()
	botheading=bank.bank('currentHeading')
	print 'Line heading: '+str(lineheading)
	print 'Bot heading: '+str(botheading)
	
	if (bot_posVlin=='above') & (botheading>lineheading): #above line and heading away from it.
		print 'Bot above and heading away from line to be followed'
		headDesired=((lineheading-botheading)/2)+lineheading

	if (bot_posVlin=='below') & (botheading>lineheading):
		print 'Bot below and heading away from line to be followed'
		headDesired=((lineheading-botheading)/2)+lineheading

	if (bot_posVlin=='below') & (botheading<lineheading):
		print 'Bot below and heading toward from line to be followed'
		headDesired=lineheading-math.fabs((lineheading-botheading)/2)

	if (bot_posVlin=='above') & (botheading<lineheading):
		print 'Bot above and heading toward from line to be followed'
		headDesired=lineheading-math.fabs((lineheading-botheading)/2)
	if bot_posVlin=='on':
		print 'Bot is on the line to be followed!'
		headDesired=lineheading
	print 'The desired heading for the bot is:' + str(headDesired)


#followLine()
#above_below_on_line()
#slope()
#heading_line()
