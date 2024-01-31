from .connections import *
from Devices.Rodney.Settings.configurator import SettingsSingleton as settings


class X_Load:

    def __init__(self):
        print("X Load init")
        self.config = settings()
        self.config_data = self.config.get('sensors', {})
        self.load = 0.0
        self.load_adc = 0.0
        try:
            self.slope = self.config_data['X Load']['slope']
            self.intercept = self.config_data['X Load']['intercept']
            print('X Load configured')
        except:
            print('X Load not configured')
            self.slope = 1.0
            self.intercept = 0

    def get_data(self, adc_out = 0):
        try:
            if adc_out == 1:
                self.load_adc = X_LOAD_CHAN.value
                return self.load_adc
            else:
                self.load = (X_LOAD_CHAN.value * self.slope) + self.intercept
                return self.load
        except:
            if adc_out == 1:
                return self.load_adc
            else:
                print('Failed X Load')
                return self.load
