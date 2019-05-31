from .connections import *

class Humidity:

    def __init__(self):
        self.hum = 0.0

    def get_data(self):
        try:
            self.hum = am.relative_humidity
            return self.hum
        except:
            return self.hum
