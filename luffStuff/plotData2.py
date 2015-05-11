import matplotlib.pyplot as plt
import numpy as np

#Test 1 -- NA
#Test 2 -- luffing
#Test 3 -- holding shape
#Test 4 -- both/switch
#Test 5 -- holding shape
#Test 6 -- NA -- bad accl sensor_data
#Test 7 -- luffing
#Test 8 -- both 

#Open file as read only to get ze datas:
file_name = 'test3.txt'
f = open(file_name, 'r')

p=[] #array of pressure values
az=[]

for line in f:
    P,AZ = line.split(',') #Split the line into useful segments
    __sentinal, p_value = P.split('P:')
    __sentinal, az_value = AZ.split('Az:')
    az_value = float(az_value) * (5.0 / 1023.0)
    p.append(p_value)
    az.append(az_value)


plt.plot(p, linewidth=3.0)
plt.ylabel('Pressure (mb)', fontsize=17)
plt.xlabel('Time', fontsize=17)
plt.title('Pressure over Time', fontsize=25)
plt.show()

plt.clf()
plt.plot(az, 'g', linewidth=3.0)
plt.ylabel('Acceleration (V)', fontsize=17)
plt.xlabel('Time', fontsize=17)
plt.title('Acceleration over Time', fontsize=25)
plt.show()

