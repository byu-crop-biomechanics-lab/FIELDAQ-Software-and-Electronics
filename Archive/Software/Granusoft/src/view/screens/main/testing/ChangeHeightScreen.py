"""
An input text box that, when selected, allows the user to type in the current Height
setting via a touch screen number pad that will pop up. The value in the input text box
when you first visit this view is whatever value for the Height setting is currently
stored in our settings file.
"""

from kivy.lang import Builder

import configurator as config
from view.BaseScreen import BaseScreen
import csv

Builder.load_file('view/screens/main/testing/ChangeHeightScreen.kv')

class ChangeHeightScreen(BaseScreen):

    def on_pre_enter(self):
        """Before the Screen loads, read the configuration file to get the current
        height."""
        input = self.ids['height']
        input.text = self.load_cell_height
        input.validate()

    def on_enter(self):
        """Once the Screen loads, focus the TextInput"""
        input = self.ids['height']
        input.focus = True

    def save(self):
        """Save button was pressed: save the new height in the configuration file.
        Returns True if save was successful.  False otherwise."""
        input = self.ids['height']
        valid = input.validate()
        if valid:
            self.save_new_height(float(input.text))
            return True
        else:
            input.focus = True
            return False

    def set_file(self, filename):
        self.fileName = filename

    def set_height(self,height):
        self.load_cell_height = height

    def save_new_height(self,height):
            foldername = "Tests/"+config.get('selected_folder',0)+'/'
            height_line = 10
            r = csv.reader(open(foldername + str(self.fileName)))
            lines = list(r)

            lines[height_line][1]= height

            writer = csv.writer(open(foldername + str(self.fileName), 'w+',newline=''))
            writer.writerows(lines)