"""
An input text box that, when selected, allows the user to type in the current Operator
setting via a touch screen keyboard that will pop up. The value in the input text box
when you first visit this view is whatever value for the Operator setting is currently
stored in our settings file .
"""

from kivy.lang import Builder
import os
import configurator as config
from view.BaseScreen import BaseScreen
from view.input.StrInput import StrInput

from os import listdir
from os.path import isdir, join

Builder.load_file('view/screens/main/testing/FolderScreen.kv')

TESTS_FOLDER = 'Tests/'

class FolderScreen(BaseScreen):
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
        folder_list = [f for f in listdir(TESTS_FOLDER) if isdir(join(TESTS_FOLDER, f))]
        input = self.ids['folder']
        valid = input.validate()
        if valid:
            config.set('folder', str(input.text).replace(' ',''))
            if str(input.text).replace(' ','') in folder_list:
                return True
            os.mkdir('Tests/'+str(config.get('folder', 0)))
            folder_list.append(str(input.text).replace(' ',''))
            config.set('folders', folder_list)
            return True
        else:
            input.focus = True
            return False
        
        