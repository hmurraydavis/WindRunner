import matplotlib.pyplot as plt
import numpy as np
#import plotData2 as pd2

test_num = 37  # 36 #24  
#31, 34, 37
start_val = 40



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
file_name = '5-11_data_collection/test{}.txt'.format(str(test_num))
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
#        print p_value
        p.append(p_value)
        az.append(az_value)
        z.append(z_value)
        sdx.append(sdx_value)
        sdy.append(sdy_value)

##plt.clf()
##plt.plot(az, 'g', linewidth=3.0, label='acceleration sensor')
##plt.plot(p, linewidth=3.0, label='pressure')
##plt.plot(z, 'm', linewidth=3.0, label='vibration sensor')
##plt.legend()
##plt.ylabel('Voltage (V) or Presure (mb)', fontsize=17)
##plt.xlabel('Time', fontsize=17)
##plt.title('Sensor Output over Time', fontsize=25)
##plt.show()

#accl_rect_avg, accl_max_avg, acclZ_val = pd2.compute_acceleration_statistics(az)
#print acclZ_val

def rectify(a):
    plot_array=[]
    a_rectified=[]; a_tozero=[]
    for i, __ in enumerate(a):
        plot_array.append(i)
        a[i] = float(a[i])
    
    m,b = np.polyfit(plot_array,a,1)
    
    a = np.array(a)
    a_tozero = a-b
    a_rectified = abs(a_tozero)
#    print a_rectified
#    plt.plot(a_tozero, 'r')
#    plt.plot(a_rectified, 'b')
#    plt.plot(plot_array*0)
#    plt.show()
    return a_rectified
    

def time_rectified_process(ra, interval):
    ra_avgs = []; ra_maxes = []
    
    for index, element in enumerate(ra[interval:len(ra)-interval]):
        ra_avgs.append(sum(ra[index: index+interval])/interval)
        ra_maxes.append(max(ra[index: index+interval]))
    return np.array(ra_avgs), np.array(ra_maxes)

    
def variance_through_time(a, interval):
    a_vars = []
    for index, value in enumerate(a):
        a[index] = float(a[index])
    
    for index, element in enumerate(a[interval:len(a)-interval]):
        a_vars.append(100*np.var(a[index:index+interval]))
        
    return np.array(a_vars)


interval = 35
az_rectified = rectify(az[start_val:])
z_rectified = rectify(z[start_val:])

az_avgs, az_maxes = time_rectified_process(az_rectified, interval)
z_avgs, z_maxes = time_rectified_process(z_rectified, interval)
z_avg_ur, z_maxes_ur = time_rectified_process(z,interval)

p_var = variance_through_time(p[start_val:], interval)
#p = [float(a) for a in p]
#p_raw_plot = [a/1000.0 for a in p]
#print p_raw_plot
#np.divide(p[start_val:start_val+len(az_avgs)],100)

plt.plot(az[start_val:start_val+len(az_avgs)], alpha=0.4, color='#8360A2', linewidth=4.0, label='raw accelerometer data')
plt.plot(z[start_val:start_val+len(az_avgs)], alpha=0.45, color = '#B4649E', linewidth=4.0, label='raw vibration data')
#plt.plot(p_raw_plot, alpha=0.45, linewidth=4.0, label='raw pressure data')

plt.plot(az_avgs, color='#073A3C', linewidth=3.0, label='acceleration time window mean')
plt.plot(az_maxes, color='#0A0133', linewidth=3.0, label='acceleration time window maximum')
#plt.plot(p_avgs, linewidth=3.0, label='pressure time window mean')
#plt.plot(100*p_maxes, linewidth=3.0, label='pressure time window maximum')
#plt.plot(z_avgs, linewidth=3.0, label='vibration time window mean')
#plt.plot(z_maxes, linewidth=3.0, label='vibration time window maximum')
plt.plot(z_avg_ur[start_val:start_val+len(az_avgs)], color = '#4A0838',linewidth=3.0, label='vibration time window mean')
plt.plot(z_maxes_ur[start_val:start_val+len(az_avgs)], color='#600A12', linewidth=3.0, label='vibration time window maximum')
plt.plot(10*p_var, color='#495E0A', linewidth=3.0, label='pressure time window variance (x10)')

plt.ylabel('Data (measured units)', fontsize=21)
plt.xlabel('Time', fontsize=21)
plt.title('Processed Data Over Time', fontsize=28)
plt.legend()
plt.show()

 

###Vibration plot!
##fig3, ax1 = plt.subplots()
###ax1.plot(az, 'm', linewidth=3.0, label='acceleration sensor')
##ax1.plot(z, 'b', linewidth=3.0, label='vibration sensor')
###ax1.plot(acclZ_val, 'c', linewidth=3.0, label='acceleration rectified average')
###ax1.plot(accl_max_avg, 'c', linewidth=3.0, label='acceleration sensor')
##ax1.set_xlabel('time (s)', size=18)
### Make the y-axis label and tick labels match the line color.
##ax1.set_ylabel('Vibration (V)', color='m', size=18)
##for tl in ax1.get_yticklabels():
##    tl.set_color('m')


##ax2 = ax1.twinx()
##ax2.plot(p, 'r', linewidth=3.0)
##ax2.set_ylabel('Point X Position (pixels)', color='r', size=18)
##for tl in ax2.get_yticklabels():
##    tl.set_color('r')
##plt.title('Data from Transition Trial', fontsize=25)
##plt.legend()
##plt.show()


##Sail Position Plot: 
#plt.clf()
#plt.plot(sdx, linewidth=3.0, label='x position')
#plt.plot(sdy, linewidth=3.0, label='y position')
#plt.legend()
#plt.ylabel('Position (Pixels)', fontsize=17)
#plt.xlabel('Time', fontsize=17)
#plt.title('Position over Time', fontsize=25)
#plt.show()

##Pressure plot
#p = np.array(p)
#plt.plot(p, linewidth=3.0, label='pressure')
##plt.plot(sdx, linewidth=3.0, label='x position')
#plt.legend()
#plt.ylabel('Pressure (mb)', fontsize=17)
#plt.xlabel('Time', fontsize=17)
#plt.title('Pressure over Time', fontsize=25)
#plt.show()

##Acceleration plot
#plt.clf()
#plt.plot(az, 'g', linewidth=3.0, label='acceleration sensor')
#plt.plot(z, 'm', linewidth=3.0, label='vibration sensor')
##plt.plot(sdx, linewidth=3.0, label='x position')
#plt.legend()
#plt.ylabel('Acceleration (V)', fontsize=17)
#plt.xlabel('Time', fontsize=17)
#plt.title('Acceleration over Time', fontsize=25)
#plt.show()

##Vibration plot
#plt.clf()
#plt.plot(z, 'm', linewidth=3.0, label='vibration sensor')
#plt.ylabel('Vibration (V)', fontsize=17)
#plt.xlabel('Time', fontsize=17)
#plt.title('Vibration over Time', fontsize=25)
#plt.show()



