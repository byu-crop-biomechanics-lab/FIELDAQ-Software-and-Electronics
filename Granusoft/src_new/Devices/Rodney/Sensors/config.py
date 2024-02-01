"""
Set values for Reading ADCs: 

"""
num_ADCs = 4                        # number of ADCs in the system
readPeriod = 1                      # seconds
samplesPerRead = 50                 # number of samples to take per read    
frequency = 400000

ADC_Res = 23                        # [bits] ADC resolution (max 23) (don't go below 8)
ADC_Res_Dec = (2 ** ADC_Res) - 1    # [bits] ADC resolution decimal value
supply_voltage = 3                  # [Volts] Set this to what ADC is tied to (VCC)
gain = 128                          # Set to programmed gain (not used currently in main.py)