"""
This screen makes sure that the user will not accidentally archive stored tests on the device. It is quite simple
with only two buttons, archive and cancel. The position and type of button is intentionally different than the previous
set of buttons so it is very obvious there was a change in screen. 
"""

import os
import json

from kivy.lang import Builder

from util.BaseScreen import BaseScreen
from os import listdir
from os.path import isfile, join
from util.getKVPath import getKVPath

Builder.load_file(getKVPath(os.getcwd(), __file__))

class ROD_TestArchiveConfirmation(BaseScreen):
    def on_pre_enter(self):
        with open('Devices/Rodney/Settings/config.json') as f:
            data = json.load(f)
            self.current_folder = data['selected_folder']
        self.test_filenames = [f for f in listdir("Tests/" + self.current_folder) if (isfile(join("Tests/" + self.current_folder, f)) and f != ".gitignore")]

    def archive_all(self):
        if not os.path.exists('TestArchive'):
            os.makedirs('TestArchive', exist_ok=True)

        for name in self.test_filenames:
            if name != '.gitignore':
                os.rename('Tests/' + self.current_folder + "/" + name, 'TestArchive/' + name)
        super(ROD_TestArchiveConfirmation, self).back()

    def cancel(self):
        super(ROD_TestArchiveConfirmation, self).back()