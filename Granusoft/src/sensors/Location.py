from .connections import *
from kivy.clock import Clock

class Location:

    def __init__(self):
        self.lat = 0.0
        self.long = 0.0
        gps.update()
        if gps.has_fix:
            self.lat = gps.latitude
            self.long = gps.longitude
        self.Event = Clock.schedule_interval(self.data_refresh, 5)

    def get_data(self):
        gps.update()
        if gps.has_fix:
            self.lat = gps.latitude
            self.long = gps.longitude
        return self.lat, self.long

    def data_refresh(self, obj):
        gps.update()
        if gps.has_fix:
            self.lat = gps.latitude
            self.long = gps.longitude
        return self.lat, self.long

    def __del__(self):
        self.Event.cancel()
