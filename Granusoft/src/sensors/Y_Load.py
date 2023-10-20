from .connections import *
import configurator as config

class Y_Load:

    def __init__(self):
        self.config_data = config.get('sensors', {})
        self.load = 0.0
        self.load_adc = 0.0
        try:
            self.slope = self.config_data['Y Load']['slope']
            self.intercept = self.config_data['Y Load']['intercept']
        except:
            self.slope = 1.0
            self.intercept = 0

    def get_data(self, adc_out = 0):
        try:
            if adc_out == 1:
                self.load_adc = Y_LOAD_CHAN.voltage*1000 #scale to milliVolts
                return self.load_adc
            else:
                self.load = (Y_LOAD_CHAN.voltage*1000 * self.slope) + self.intercept
                return self.load
        except:
            if adc_out == 1:
                return self.load_adc
            else:
                return self.load
