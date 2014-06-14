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
			time=raw_input('How long would you like it to avoid obstacles on its own?')
			mission.append(['obstacle avoid',time])
			
		if mode=='go to point':
			pt=raw_input('GPS coordinates of point (in brackets:[])? ')
			mission.append(['go to point',pt])
			
		if mode=='maintain heading':
			heading=raw_input('Desired global heading (in degrees)?')
			mission.append(['maintain heading',heading])
			
	print 'Mission is:', mission
	for mis in mission:
		if mis=='line follow':
			pass
		if mis=='obstacle avoid':
			pass
		if mis=='go to point':
			pass
		if mis=='maintain heading':
			pass
missionMannager()
