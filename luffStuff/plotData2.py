import matplotlib.pyplot as plt
import numpy as np

test_num = 13

start_val=0
end_val=100

time_window = 20

mode=' Sensor Data, Sail Holding Shape'

luffing_tests=[10,11,12,13,14,23,24,25,26,27,28]
holding_shape_tests = [15,16,17,18,19,20,21,22,23]

#Test 1 -- NA
#Test 2 -- luffing
#Test 3 -- holding shape
#Test 4 -- both/switch
#Test 5 -- holding shape
#Test 6 -- NA -- bad accl sensor_data
#Test 7 -- luffing
#Test 8 -- both 

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

def compute_variances_pressure_sensor(p):
    for i, value in enumerate(p):
        p[i]=float(value)
        
    end_var_calc = time_window
    start_var_calc = start_val
    pres_var=[]
    for i in range(start_val, end_val-time_window):
        pres_var.append(np.var(p[start_var_calc:end_var_calc]))
        start_var_calc = start_var_calc + 1
        end_var_calc = end_var_calc + 1
    print 'Average of pressure varience, test {}'.format(test_num), sum(pres_var)/len(pres_var)
    return pres_var
    
def compute_acceleration_statistics(az):
    plot_array=[]
    az_rectified=[]; az_tozero=[]
    for i in range(start_val,end_val):
        plot_array.append(i)
        
    m,b = np.polyfit(plot_array,az[start_val:end_val],1)

    for i, value in enumerate(az):
        az[i]=float(value)
        az_tozero.append(az[i]-b)
        az_rectified.append(abs(az[i]-b))

    ##plt.plot(az_tozero, 'r', linewidth=3.0, label='Acceleration, normalized about 0')
    ##plt.plot(az_rectified, 'y', linewidth=3.0, label='Acceleration normalized and rectified')
    ##plt.legend()
    ##plt.show()
    start_var_calc = start_val
    acclZ_val=[]
    for i in range(start_val, end_val-time_window):
        max_in_time_window = max(az[start_var_calc:start_var_calc+time_window])
        acclZ_val.append(max_in_time_window)
        start_val=start_var_calc+1
        
    print 'average of rectified acceleration data, test {}: '.format(test_num), sum(az_rectified)/len(az_rectified)
    print 'average of max val in time interval, test {}: '.format(test_num), sum(acclZ_val)/len(acclZ_val)


def compute_piezo_statistics(z): 
    plot_array=[]; start_var_calc=start_val
    z_tozero=[]; z_rectified=[]; z_max_vals=[]

    for i in range(start_val,end_val):
        plot_array.append(i)
    m,b = np.polyfit(plot_array,z[start_val:end_val],1)
    for i,value in enumerate(z):
        z[i]=float(z[i])
        z_tozero.append(z[i]-b)
        z_rectified.append(abs(z_tozero[i]))
        
    for i in range(start_val, end_val-time_window): 
        max_in_time_window=max(z_rectified[start_var_calc:start_var_calc+time_window])
        start_var_calc=start_var_calc+1
        z_max_vals.append(max_in_time_window)
        
    print 'Average rectified piezo data, test {}: '.format(test_num), sum(z_rectified)/len(z_rectified)
    print 'Average max rectified piezo data in time window, test {}: '.format(test_num), sum(z_max_vals)/len(z_max_vals)




###Pressure Plot!
##fig, ax1 = plt.subplots()
##ax1.plot(p[start_val:end_val], 'b', label='Pressure Sensor')
##ax1.set_xlabel('time (s)', size=18)
### Make the y-axis label and tick labels match the line color.
##ax1.set_ylabel('Pressure (mbar)', color='b', size=18)
##for tl in ax1.get_yticklabels():
##    tl.set_color('b')


##ax2 = ax1.twinx()
##ax2.plot(sdx[start_val:end_val], 'r', label='X Position')
##ax2.set_ylabel('Point X Position (pixels)', color='r', size=18)
##for tl in ax2.get_yticklabels():
##    tl.set_color('r')
##plt.title('Pressure'+mode, fontsize=25)
##plt.show()


###Acceleration Plot!!
##fig2, ax1 = plt.subplots()
##ax1.plot(az[start_val:end_val], 'g')
##ax1.set_xlabel('time (s)', size=18)
### Make the y-axis label and tick labels match the line color.
##ax1.set_ylabel('Z Axis Acceleration (V)', color='g', size=18)
##for tl in ax1.get_yticklabels():
##    tl.set_color('g')


##ax2 = ax1.twinx()
##ax2.plot(sdx[start_val:end_val], 'r')
##ax2.set_ylabel('Point X Position (pixels)', color='r', size=18)
##for tl in ax2.get_yticklabels():
##    tl.set_color('r')
##plt.title('Acceleration'+mode, fontsize=25)
##plt.show()

###Vibration Plot!!
##fig3, ax1 = plt.subplots()
##ax1.plot(z[start_val:end_val], 'm')
##ax1.set_xlabel('time (s)', size=18)
### Make the y-axis label and tick labels match the line color.
##ax1.set_ylabel('Vibration (V)', color='m', size=18)
##for tl in ax1.get_yticklabels():
##    tl.set_color('m')


##ax2 = ax1.twinx()
##ax2.plot(sdx[start_val:end_val], 'r')
##ax2.set_ylabel('Point X Position (pixels)', color='r', size=18)
##for tl in ax2.get_yticklabels():
##    tl.set_color('r')
##plt.title('Vibration'+mode, fontsize=25)
##plt.show()


