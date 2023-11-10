"""
This screen makes sure that the user will not accidentally delete images stored on the device. It is quite simple
with only two buttons, delete and cancel. The position and type of button is intentionally different than the previous
set of buttons so it is very obvious there was a change in screen. 
"""

import os

from kivy.lang import Builder

from util.BaseScreen import BaseScreen
from os import listdir
from os.path import isfile, join
from util.getKVPath import getKVPath

Builder.load_file(getKVPath(os.getcwd(), __file__))

class CAM_ImageDeleteConfirmation(BaseScreen):
    def on_pre_enter(self):
        self.image_filenames = [f for f in listdir("Images") if (isfile(join("Images", f)) and f != ".gitignore")]

    def remove_all(self):
        for name in self.image_filenames:
            if name != '.gitignore':
                os.remove('Images/' + name)
        super(CAM_ImageDeleteConfirmation, self).back()

    def cancel(self):
        super(CAM_ImageDeleteConfirmation, self).back()