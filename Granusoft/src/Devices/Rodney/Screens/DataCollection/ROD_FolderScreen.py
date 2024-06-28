"""
An input text box that, when selected, allows the user to type in the current Operator
setting via a touch screen keyboard that will pop up. The value in the input text box
when you first visit this view is whatever value for the Operator setting is currently
stored in our settings file .
"""

from kivy.lang import Builder
import os
from Devices.Rodney.Settings.configurator import SettingsSingleton as settings
from util.BaseScreen import BaseScreen
from util.input.StrInput import StrInput
from util.getKVPath import getKVPath
from util.TestLog import TestLog
Builder.load_file(getKVPath(os.getcwd(), __file__))

class ROD_FolderScreen(BaseScreen):


    def on_pre_enter(self):
        """Before the Screen loads, read the configuration file to get the current
        operator and set the TextInput text."""
        input = self.ids['folder']
        self.config = settings()
        input.text = str(self.config.get('folder', "Default Folder"))
        input.validate()

    def on_enter(self):
        """Once the Screen loads, focus the TextInput"""
        
        log = TestLog()
        log.connection("Entering ROD_FolderScreen")
        input = self.ids['folder']
        input.focus = True


    def save(self):
        """Save button was pressed: save the new operator in the configuration file."""
        folder_list = self.config.get('folders', "default")
        input = self.ids['folder']
        valid = input.validate()
        if valid:
            self.config.set('folder', str(input.text))
            if folder_list == 0 or str(input.text) not in folder_list:
                try:
                    os.mkdir('Tests/'+str(self.config.get('folder', 0)))
                except:
                    pass
                folder_list = folder_list + " " + (str(input.text))
                self.config.set('folders', folder_list)
            return True
        else:
            input.focus = True
            return False
