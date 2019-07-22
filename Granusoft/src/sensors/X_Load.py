from .connections import *

class X_Load:

    def __init__(self):
        self.load = 0.0

    def get_data(self):
        try:
            self.load = X_LOAD_CHAN.value * 25 / 1067 # voltage * 1000  #scale to milliVolts
            # print('Voltage:', X_LOAD_CHAN.voltage*1000)
            return self.load
        except:
            return self.load
