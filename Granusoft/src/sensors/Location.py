from .connections import *

class Location:

    def __init__(self):
        self.lat = 0.0
        self.long = 0.0
        gps.update()
        if gps.has_fix:
            self.lat = gps.latitude
            self.long = gps.longitude

    def get_data(self):
        gps.update()
        if gps.has_fix:
            gps.update()
            self.lat = gps.latitude
            self.long = gps.longitude
        return self.lat, self.long
