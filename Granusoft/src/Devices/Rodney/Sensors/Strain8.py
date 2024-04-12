from .connections import *

"""
Set global/default values for Reading ADCs: 

"""
num_ADCs = 2                        # number of ADCs in the system
readPeriod = 1                      # seconds
samplesPerRead = 50                 # number of samples to take per read    
frequency = 115200
ADC_Res = 23                        # [bits] ADC resolution (max 23) (don't go below 8)
ADC_Res_Dec = (2 ** ADC_Res) - 1    # [bits] ADC resolution decimal value
supply_voltage = 3.25               # [Volts] Set this to what ADC is tied to (VCC)
gain = 128                          # Set to programmed gain (not used currently in strain8.py)


#####################################################################################


# This function reads the voltage from the ADC and converts it to a strain value
def read_voltage(adc):
    if not adc.available():  # While the ADC is not available, do nothing
        raise Exception('ADC is not connected')
    return adc.read() * supply_voltage / (ADC_Res_Dec)
    # 23-bit resolution, gain before ADC, ENOB is effectve number of bits taken from nau7802 datasheet


class Strain8:

    def __init__(self):
        self.start_channel = 1
        self.delay_time = 0.012
    
    # call this function to read all four of the strain gauges x amount of times over x amount of seconds
    # pass in the desired time period over which data will be recorded
    # pass in the desired number of samples over the time period
    # note: time period will be approximate because it takes time to read the ADC
    def read_gauges(self, sampPer=readPeriod, samples=samplesPerRead):
        # populate g1,g2,g3, and g4 with the data from the ADCs
        if self.start_channel == 1:
            strainAy = (read_voltage(ADC0))
            ADC0.channel = 2
            strainBy = (read_voltage(ADC1))
            ADC1.channel = 2
            time.sleep(self.delay_time)
            strainAx = (read_voltage(ADC0))
            strainBx = (read_voltage(ADC1))
            self.start_channel = 2
        elif self.start_channel == 2:
            strainAx = (read_voltage(ADC0))
            ADC0.channel = 1
            strainBx = (read_voltage(ADC1))
            ADC1.channel = 1
            time.sleep(self.delay_time)
            strainAy = (read_voltage(ADC0))
            strainBy = (read_voltage(ADC1))
            self.start_channel = 1
        

        return {'Ax': strainAx, 'Ay': strainAy, 'Bx': strainBx, 'By': strainBy}