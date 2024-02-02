from connections import *

"""
Set global/default values for Reading ADCs: 

"""
num_ADCs = 4                        # number of ADCs in the system
readPeriod = 1                      # seconds
samplesPerRead = 50                 # number of samples to take per read    
frequency = 400000

ADC_Res = 23                        # [bits] ADC resolution (max 23) (don't go below 8)
ADC_Res_Dec = (2 ** ADC_Res) - 1    # [bits] ADC resolution decimal value
supply_voltage = 3                  # [Volts] Set this to what ADC is tied to (VCC)
gain = 128                          # Set to programmed gain (not used currently in main.py)

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
        pass
    
    # call this function to read all four of the strain gauges x amount of times over x amount of seconds
    # pass in the desired time period over which data will be recorded
    # pass in the desired number of samples over the time period
    # note: time period will be approximate because it takes time to read the ADC
    def read_gauges(sampPer=readPeriod, samples=samplesPerRead):
        delayTime = sampPer / (
            num_ADCs * samples
        ) 
        # initialize lists for storing data
        g1 = []
        g2 = []
        g3 = []
        g4 = []

        # populate g1,g2,g3, and g4 with the data from the ADCs
        for x in range(samples):
            g1.append(read_voltage(adc1))
            g2.append(read_voltage(adc2))
            g3.append(read_voltage(adc3))
            g4.append(read_voltage(adc4))
            time.sleep(delayTime)

        # put g1,g2,g3 in a list to return to user
        result = [g1, g2, g3, g4]
        return result