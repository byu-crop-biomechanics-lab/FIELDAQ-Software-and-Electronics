from .connections import *
import configurator as config

class Pot:

    def __init__(self):
        self.config_data = config.get('sensors', {})
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
                self.pot_adc = POT_CHAN.value
                return self.pot_adc
            else:
                self.pot = (POT_CHAN.value * self.slope) + self.intercept
                return self.pot
        except:
            if adc_out == 1:
                return self.pot_adc
            else:
                return self.pot
