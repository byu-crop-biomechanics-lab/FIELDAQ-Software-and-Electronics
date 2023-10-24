"""
The main screen contains four buttons for navigation:
Settings, Testing, Live Feed, and Exit

It also shows environment data: Temperature, Humidity, Location, and Time.
"""

from kivy.lang import Builder
from kivy.properties import StringProperty
from kivy.clock import Clock
from view.BaseScreen import BaseScreen
from Sensor import Sensor
import datetime
# import pytz
# from timezonefinder import TimezoneFinder

Builder.load_file('view/screens/main/ModeSelect.kv')


class ModeSelect(BaseScreen):
    
    def on_pre_enter(self):
       pass
    def on_enter(self):
        pass

    def on_leave(self):
        pass