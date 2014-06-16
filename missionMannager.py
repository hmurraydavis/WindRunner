import time
import bank
import followLine
import obsAvoid
import goToPoint
import mtnHeading


def missionMannager():
	
	number_of_modes=int(raw_input('How many modes would you like to have in your mission?'))
	
	mission=[]
	
	for mode in range (0,number_of_modes):
		mode=raw_input('What mode would you like to use here? choces: "line follow," "obstacle avoid," "go to point," "maintain heading" ')
		if mode=='line follow':
			pt1=raw_input('GPS Coordinates of first point (in brackets:[])? ')
			pt2=raw_input('GPS Coordinates of second point (in brackets:[])? ')
			mission.append(['line follow',pt1,pt2])
			
		if mode=='obstacle avoid':
			timeT=raw_input('How long would you like it to avoid obstacles on its own?')
			mission.append(['obstacle avoid',timeT])
			
		if mode=='go to point':
			pt=raw_input('GPS coordinates of point (in brackets:[])? ')
			mission.append(['go to point',pt])
			
		if mode=='maintain heading':
			heading=raw_input('Desired global heading (in degrees)?')
			timeT=timeT=raw_input('How long would you like it to maintain this heading?')
			mission.append(['maintain heading',heading,timeT])
			
	print 'Mission is:', mission
	
	for mis in mission:
		print mis[0]
		if mis[0]=='line follow':
			while bank.bank('posCurrent')!=mis[2]:
				followLine.followLine()
				time.sleep(.25)
		if mis[0]=='obstacle avoid':
			for t in range (0,2*int(mis[1])):
				obsAvoid.obsAvoid()
		if mis[0]=='go to point':
			while bank.bank('posCurrent')!=mis[1]:
				goToPoint.goToPoint()
				time.sleep(.25)
		if mis[0]=='maintain heading':
			for t in range (0,4*int(mis[2])):
				mtnHeading.mtnHeading()
				time.sleep(.25)
missionMannager()
