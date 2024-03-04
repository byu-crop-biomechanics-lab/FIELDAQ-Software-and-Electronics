from .connections import *
from Devices.Rodney.Settings.configurator import SettingsSingleton as settings

class WhiskerFront:

    def __init__(self):
        self.config = settings()
        self.config_data = self.config.get('sensors', {})
        self.pot = 0.0
        self.pot_adc = 0.0
        try:
            self.slope = self.config_data['Pot Angle']['slope']
            self.intercept = self.config_data['Pot Angle']['intercept']
        except:
            self.slope = 1.0
            self.intercept = 0.0

    def get_data(self, adc_out = 0):
        try:
            if adc_out == 1:
                self.pot_adc = CHAN3.value
                return self.pot_adc
            else:
                self.pot = (CHAN3.value * self.slope) + self.intercept
                return self.pot
        except:
            if adc_out == 1:
                return self.pot_adc
            else:
                return self.pot