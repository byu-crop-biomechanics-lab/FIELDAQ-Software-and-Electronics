"""
An input text box that, when selected, allows the user to type in the current Height
setting via a touch screen number pad that will pop up. The value in the input text box
when you first visit this view is whatever value for the Height setting is currently
stored in our settings file.
"""

from kivy.lang import Builder

import Arm.settings.configurator as config
from util.BaseScreen import BaseScreen
from util.input.FloatInput import FloatInput
from util.getKVPath import getKVPath
import os

Builder.load_file(getKVPath(os.getcwd(), __file__))

class ROD_HeightScreen(BaseScreen):
    def on_pre_enter(self):
        """Before the Screen loads, read the configuration file to get the current
        height."""
        input = self.ids['height']
        input.text = str(config.get('height', 0))
        input.validate()

    def on_enter(self):
        """Once the Screen loads, focus the TextInput"""
        input = self.ids['height']
        input.focus = True
        #input.select_all()

    def save(self):
        """Save button was pressed: save the new height in the configuration file.
        Returns True if save was successful.  False otherwise."""
        input = self.ids['height']
        valid = input.validate()
        if valid:
            config.set('height', float(input.text))
            return True
        else:
            input.focus = True
            return False

