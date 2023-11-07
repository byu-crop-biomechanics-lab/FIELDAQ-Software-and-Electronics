"""
An input text box that, when selected, allows the user to type in the current Operator
setting via a touch screen keyboard that will pop up. The value in the input text box
when you first visit this view is whatever value for the Operator setting is currently
stored in our settings file .
"""

from kivy.lang import Builder
import os
import Arm.Settings.configurator as config
from util.BaseScreen import BaseScreen
from util.input.StrInput import StrInput
from util.getKVPath import getKVPath

Builder.load_file(getKVPath(os.getcwd(), __file__))

class ARM_FolderScreen(BaseScreen):
    def on_pre_enter(self):
        """Before the Screen loads, read the configuration file to get the current
        operator and set the TextInput text."""
        input = self.ids['folder']
        input.text = str(config.get('folder', "Default Folder"))
        input.validate()

    def on_enter(self):
        """Once the Screen loads, focus the TextInput"""
        input = self.ids['folder']
        input.focus = True


    def save(self):
        """Save button was pressed: save the new operator in the configuration file."""
        folder_list = config.get('folders',0)
        input = self.ids['folder']
        valid = input.validate()
        if valid:
            config.set('folder', str(input.text))
            if str(input.text) not in folder_list:
                try:
                    os.mkdir('Tests/'+str(config.get('folder', 0)))
                except:
                    pass
                folder_list.append(str(input.text))
                config.set('folders', folder_list)
            return True
        else:
            input.focus = True
            return False
