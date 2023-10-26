"""
The main screen contains four buttons for navigation:
Settings, Testing, Live Feed, and Exit

It also shows environment data: Temperature, Humidity, Location, and Time.
"""

from kivy.lang import Builder
from util.BaseScreen import BaseScreen

Builder.load_file('ModeSelect.kv')


class ModeSelect(BaseScreen):
    
    def on_pre_enter(self):
       pass
    def on_enter(self):
        pass

    def on_leave(self):
        pass