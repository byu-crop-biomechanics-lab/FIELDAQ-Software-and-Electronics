"""
From the settings screen you can navigate to these options: Height, Plot, Operator,
Folder, Notes
"""

import os

from kivy.lang import Builder
from kivy.uix.floatlayout import FloatLayout
from kivy.properties import ObjectProperty
from kivy.properties import StringProperty
from kivy.uix.popup import Popup

import configurator as config
from view.BaseScreen import BaseScreen

Builder.load_file('view/screens/main/SettingsScreen.kv')

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

class SettingsScreen(BaseScreen):
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

    def update_os_git(self):
        os.system("git pull")
        os.system("python3 main.py")

    def update_os_usb(self):
        os.system("sudo mount -t vfat -o uid=pi,gid=pi /dev/sda1 /mnt/usbStick")
        os.system("sudo cp -r /mnt/usbStick/FIELDAQ/ ~/") # The pi's cp command has strange behavior
        os.system("sudo umount /mnt/usbStick")
        os.system("python3 main.py")
