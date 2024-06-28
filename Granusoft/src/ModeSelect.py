"""
The main screen contains four buttons for navigation:
Settings, Testing, Live Feed, and Exit

It also shows environment data: Temperature, Humidity, Location, and Time.
"""

from kivy.lang import Builder
from util.BaseScreen import BaseScreen
from util.getKVPath import getKVPath
import os
from util.TestLog import TestLog

Builder.load_file(getKVPath(os.getcwd(), __file__))


class ModeSelect(BaseScreen):
    
    def on_pre_enter(self):
       log = TestLog()
       log.connection("Entered ModeSelect screen")
       pass
    def on_enter(self):
        pass

    def on_leave(self):
        pass