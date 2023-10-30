from .connections import *
import configurator as config
from Singleton import SettingsSingleton

class Strain1:

    def __init__(self):
        self.config = SettingsSingleton()
        self.config_data = self.config.get('sensors', {})
        self.load = 0.0
        self.load_adc = 0.0
        try:
            self.slope = self.config_data['Strain 1']['slope']
            self.intercept = self.config_data['Strain 1']['intercept']
        except:
            self.slope = 1.0
            self.intercept = 0

    def get_data(self, adc_out = 0):
        try:
            if adc_out == 1:
                self.load_adc = STRAIN_1_CHAN.value
                return self.load_adc
            else:
                self.load = (STRAIN_1_CHAN.value * self.slope) + self.intercept
                return self.load
        except:
            if adc_out == 1:
                return self.load_adc
            else:
                print('Failed X Strain 1')
                return self.load
