"""
This screen makes sure that the user will not accidentally delete tests stored on the device. It is quite simple
with only two buttons, delete and cancel. The position and type of button is intentionally different than the previous
set of buttons so it is very obvious there was a change in screen. 
"""

import os

from kivy.lang import Builder

from view.BaseScreen import BaseScreen
from os import listdir
from os.path import isfile, join

Builder.load_file('view/screens/settings/TestDeleteConfirmation.kv')

class TestDeleteConfirmation(BaseScreen):
    def on_pre_enter(self):
        self.test_filenames = [f for f in listdir("TestArchive") if (isfile(join("TestArchive", f)) and f != ".gitignore")]

    def remove_all(self):
        for name in self.test_filenames:
            if name != '.gitignore':
                os.remove('TestArchive/' + name)
        super(TestDeleteConfirmation, self).back()

    def cancel(self):
        super(TestDeleteConfirmation, self).back()