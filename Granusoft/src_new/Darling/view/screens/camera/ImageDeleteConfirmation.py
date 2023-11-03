"""
This screen makes sure that the user will not accidentally delete images stored on the device. It is quite simple
with only two buttons, delete and cancel. The position and type of button is intentionally different than the previous
set of buttons so it is very obvious there was a change in screen. 
"""

import os

from kivy.lang import Builder

from view.BaseScreen import BaseScreen
from os import listdir
from os.path import isfile, join

Builder.load_file('view/screens/camera/ImageDeleteConfirmation.kv')

class ImageDeleteConfirmation(BaseScreen):
    def on_pre_enter(self):
        self.image_filenames = [f for f in listdir("Images") if (isfile(join("Images", f)) and f != ".gitignore")]

    def remove_all(self):
        for name in self.image_filenames:
            if name != '.gitignore':
                os.remove('Images/' + name)
        super(ImageDeleteConfirmation, self).back()

    def cancel(self):
        super(ImageDeleteConfirmation, self).back()