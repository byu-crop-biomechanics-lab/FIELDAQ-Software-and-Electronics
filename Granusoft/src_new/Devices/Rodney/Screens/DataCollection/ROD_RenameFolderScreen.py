"""
An input text box that, when selected, allows the user to type in the current Operator
setting via a touch screen keyboard that will pop up. The value in the input text box
when you first visit this view is whatever value for the Operator setting is currently
stored in our settings file .
"""

from kivy.lang import Builder
import os
import Devices.Rodney.Settings.configurator as config
from util.BaseScreen import BaseScreen
from util.input.StrInput import StrInput
from util.getKVPath import getKVPath
from util.elements import *

Builder.load_file(getKVPath(os.getcwd(), __file__))

class ROD_RenameFolderScreen(BaseScreen):
    def __init__(self, **kwargs):
        super(BaseScreen, self).__init__(**kwargs)
        self.save_button = GranuSideButton(text='Save')
        self.save_button.bind(on_release=self.save)

    def on_pre_enter(self):
        """Before the Screen loads, read the configuration file to get the current
        operator and set the TextInput text."""
        input = self.ids['folder']
        input.text = str(config.get('selected_folder', "Default Folder"))
        self.previous_name = input.text
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
            os.rename('Tests/'+self.previous_name,"Tests/"+str(input.text))
            folder_list = folder_list.replace(self.previous_name, "")
            folder_list = folder_list + input.text
            config.set('folders', folder_list)
        else:
            input.focus = True
            return False
        self.move_to('rod_test_folders_screen')
