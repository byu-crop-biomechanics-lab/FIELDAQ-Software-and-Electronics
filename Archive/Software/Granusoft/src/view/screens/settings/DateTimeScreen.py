"""
An input text box that, when selected, allows the user to type in a new note via a touch
screen keyboard that will pop up. The input text box will iniinputally be empty.
"""

from kivy.lang import Builder

import configurator as config
from view.BaseScreen import BaseScreen
from view.input.StrInput import StrInput
import os

Builder.load_file('view/screens/settings/DateTimeScreen.kv')

class DateTimeScreen(BaseScreen):
    def on_pre_enter(self):
        input = self.ids['datetime']
        input.text = ''
        try:
            os.system('sudo timedatectl set-ntp false')
        except:
            pass

    def on_enter(self):
        """Once the Screen loads, focus the Texinputnput"""
        input = self.ids['datetime']
        input.focus = True

    def save(self):

        input = self.ids['datetime']

        date_time = input.text
        valid = input.validate()

        if valid:
            try:
                txt = str(date_time).split(' ')
                msg = '\''+txt[0]+' '+txt[1]+'\''
                config.set('timezone',txt[2])
                os.system('sudo date -s '+msg) 
                return True
            except:
                return False
        else:
            input.show_invalid()
            input.focus = True
            return False
