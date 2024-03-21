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
supply_voltage = 3.3                # [Volts] Set this to what ADC is tied to (VCC)
gain = 128                          # Set to programmed gain (not used currently in strain8.py)


#####################################################################################


# This function reads the voltage from the ADC and converts it to a strain value
def read_voltage(adc):
    if not adc.available():  # While the ADC is not available, do nothing
        pass
    return (
        adc.read() * supply_voltage / (ADC_Res_Dec)
    )  # 23-bit resolution, gain before ADC, ENOB is effectve number of bits taken from nau7802 datasheet


class Strain8:

    def __init__(self):
        self.cv1 = 0.0
        self.cv2 = 0.0
        self.ch1 = 0.0
        self.ch2 = 0.0
        self.dv1 = 0.0
        self.dv2 = 0.0
        self.dh1 = 0.0
        self.dh2 = 0.0
        self.kv1 = 0.0
        self.kv2 = 0.0
        self.kh1 = 0.0
        self.kh2 = 0.0
    
    # call this function to read all four of the strain gauges x amount of times over x amount of seconds
    # pass in the desired time period over which data will be recorded
    # pass in the desired number of samples over the time period
    # note: time period will be approximate because it takes time to read the ADC
    def read_gauges(self, sampPer=readPeriod, samples=samplesPerRead):
        delayTime = sampPer / (
            num_ADCs * samples
        ) 

        # populate g1,g2,g3, and g4 with the data from the ADCs
        g1 = (read_voltage(ADC0))
        g2 = (read_voltage(ADC1))
        g3 = (read_voltage(ADC2))
        g4 = (read_voltage(ADC3))

        # put g1,g2,g3 in a list to return to user
        result = [g1, g2, g3, g4]
        return result