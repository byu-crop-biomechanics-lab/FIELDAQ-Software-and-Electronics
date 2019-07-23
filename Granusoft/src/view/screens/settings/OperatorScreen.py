"""
An input text box that, when selected, allows the user to type in the current Operator
setting via a touch screen keyboard that will pop up. The value in the input text box
when you first visit this view is whatever value for the Operator setting is currently
stored in our settings file .
"""

from kivy.lang import Builder

import configurator as config
from view.BaseScreen import BaseScreen
from view.input.StrInput import StrInput

Builder.load_file('view/screens/settings/OperatorScreen.kv')

class OperatorScreen(BaseScreen):
    def on_pre_enter(self):
        """Before the Screen loads, read the configuration file to get the current
        operator and set the TextInput text."""
        input = self.ids['operator']
        input.text = str(config.get('operator', "Default User"))
        input.validate()

    def on_enter(self):
        """Once the Screen loads, focus the TextInput"""
        input = self.ids['operator']
        input.focus = True
        #input.select_all()

    def save(self):
        """Save button was pressed: save the new operator in the configuration file."""
        input = self.ids['operator']
        valid = input.validate()
        if valid:
            config.set('operator', str(input.text))
            return True
        else:
            input.focus = True
            return False
