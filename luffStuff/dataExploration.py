import matplotlib.pyplot as plt
import numpy as np

test_num = 31

#Test 10-system trial
#10-14-luff
#15-23 hold shape
#23-28 luffing
#29 scratch
#start holding shape then release below here
#30 and not  - good
#31 and not fantastic!!!
#32good
#33 so so not that much luff
#34 really nice trial! great release and luff
#35 pretty nice trial
#36 not good, bad transion to luff.not existant.setreme luff
#37 pretty good

#all three holding, luffing, and holding
#38

#Open file as read only to get ze datas:
file_name = 'test{}.txt'.format(str(test_num))
f = open(file_name, 'r')

p=[] #array of pressure values
az=[]
z=[]
sdx = []
sdy= []

for line in f:
    if not 'SOMETHING_WENT_WRONG' in line:
        SC, SR, P,AZ,Z = line.split(' ') #Split the line into useful segments
        __sentinal, p_value = P.split('P:')
        __sentinal, az_value = AZ.split('Az:')
        __sentinal, z_value = Z.split('Z:')
        __sentinal, sc_values = SC.split('Sc:')
        az_value = float(az_value) * (5.0 / 1023.0)
        z_value = float(z_value)* (5.0 / 1023.0)
        sdx_value,sdy_value = sc_values.split('|')
        print p_value
        p.append(p_value)
        az.append(az_value)
        z.append(z_value)
        sdx.append(sdx_value)
        sdy.append(sdy_value)


#Sail Position Plot: 
plt.clf()
plt.plot(sdx, linewidth=3.0, label='x position')
plt.plot(sdy, linewidth=3.0, label='y position')
plt.legend()
plt.ylabel('Position (Pixels)', fontsize=17)
plt.xlabel('Time', fontsize=17)
plt.title('Position over Time', fontsize=25)
plt.show()

#Pressure plot
p = np.array(p)
plt.plot(p, linewidth=3.0, label='pressure')
#plt.plot(sdx, linewidth=3.0, label='x position')
plt.legend()
plt.ylabel('Pressure (mb)', fontsize=17)
plt.xlabel('Time', fontsize=17)
plt.title('Pressure over Time', fontsize=25)
plt.show()

#Acceleration plot
plt.clf()
plt.plot(az, 'g', linewidth=3.0, label='acceleration sensor')
plt.plot(z, 'm', linewidth=3.0, label='vibration sensor')
#plt.plot(sdx, linewidth=3.0, label='x position')
plt.legend()
plt.ylabel('Acceleration (V)', fontsize=17)
plt.xlabel('Time', fontsize=17)
plt.title('Acceleration over Time', fontsize=25)
plt.show()

##Vibration plot
#plt.clf()
#plt.plot(z, 'm', linewidth=3.0, label='vibration sensor')
#plt.ylabel('Vibration (V)', fontsize=17)
#plt.xlabel('Time', fontsize=17)
#plt.title('Vibration over Time', fontsize=25)
#plt.show()


