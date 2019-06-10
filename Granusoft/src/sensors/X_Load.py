from .connections import *

class X_Load:

    def __init__(self):
        self.load = 0.0

    def get_data(self):
        try:
            self.load = X_LOAD_CHAN.voltage*1000 #scale to milliVolts
            return self.load
        except:
            return self.load
