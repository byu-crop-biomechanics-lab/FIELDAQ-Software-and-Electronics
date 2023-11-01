"""
An input text box that, when selected, allows the user to type in the Break Height value of the last test via a touch screen number pad that will pop up. The value in the input text box when you first visit this view is whatever value for the Height setting is currently stored in our settings file.
"""

from kivy.lang import Builder

import Arm.Settings.configurator as config
from util.BaseScreen import BaseScreen
from util.input.FloatInput import FloatInput
from util.getKVPath import getKVPath
import os

Builder.load_file(getKVPath(os.getcwd(), __file__))

class BreakHeightScreen(BaseScreen):
    def on_pre_enter(self):
        """Before the Screen loads, read the configuration file to get the current
        height."""
        input = self.ids['break_height']
        input.text = str(config.get('break_height', 0))
        input.validate()

    def on_enter(self):
        """Once the Screen loads, focus the TextInput"""
        input = self.ids['break_height']
        input.focus = True

    def save(self):
        """Save button was pressed: save the new height in the configuration file.
        Returns True if save was successful.  False otherwise."""
        input = self.ids['break_height']
        valid = input.validate()
        if valid:
            config.set('break_height', input.text)
            return True
        else:
            input.focus = True
            return False

