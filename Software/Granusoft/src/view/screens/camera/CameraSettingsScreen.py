"""
Settings relevant to the camera are viewed here. Some settings relevant are:
Plot Number, Height, etc.

Switching back to the main Granustem functionality is also achieved through the
Settings screen.
"""

import os

from kivy.lang import Builder
from kivy.uix.floatlayout import FloatLayout
from kivy.properties import ObjectProperty
from kivy.properties import StringProperty
from kivy.uix.popup import Popup

import configurator as config
from view.BaseScreen import BaseScreen

Builder.load_file('view/screens/camera/CameraSettingsScreen.kv')

class LoadDialog(Popup):
    '''A dialog to load a file.  The load and cancel properties point to the
    functions called when the load or cancel buttons are pressed.'''
    load = ObjectProperty(None)
    cancel = ObjectProperty(None)


class SaveDialog(Popup):
    '''A dialog to save a file.  The save and cancel properties point to the
    functions called when the save or cancel buttons are pressed.'''
    save = ObjectProperty(None)
    cancel = ObjectProperty(None)

class CameraSettingsScreen(BaseScreen):
    def dismiss_popup(self):
        self._popup.dismiss()

    def show_load(self):
        self._popup = LoadDialog(load=self.load, cancel=self.dismiss_popup)
        self._popup.open()

    def show_save(self):
        self._popup = SaveDialog(save=self.save, cancel=self.dismiss_popup)
        self._popup.open()

    def load(self, path, filename):
        config.load_from(os.path.join(path, filename))
        self.dismiss_popup()

    def save(self, path, filename):
        config.save_as(os.path.join(path, filename))
        self.dismiss_popup()

    def updateOS(self):
        os.system("git pull")
        os.system("python3 main.py")
