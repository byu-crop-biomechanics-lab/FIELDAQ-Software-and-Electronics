from .connections import *
import configurator as config

class X_Load:

    def __init__(self):
        self.config_data = config.get('sensors', {})
        self.load = 0.0
        self.load_adc = 0.0
        try:
            self.slope = self.config_data['X Load']['slope']
            self.intercept = self.config_data['X Load']['intercept']
        except:
            self.slope = 1.0
            self.intercept = 0

    def get_data(self):
        try:
            self.load = (X_LOAD_CHAN.value * self.slope) + self.intercept
            self.load_adc = X_LOAD_CHAN.value
            return self.load
        except:
            return self.load
