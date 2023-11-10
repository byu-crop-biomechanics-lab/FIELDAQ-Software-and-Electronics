from .connections import *

class Temperature:

    def __init__(self):
        self.temp = 0.0

    def get_data(self):
        try:
            self.temp = 0.0 #am.temperature
            return self.temp
        except:
            return self.temp
