"""
Test settings confirmation menu. This is to make sure the user sets the correct
data for the test.
"""

from kivy.lang import Builder
from kivy.properties import StringProperty

from util.BaseScreen import BaseScreen
from Devices.Rodney.Settings.configurator import SettingsSingleton as settings
from util.elements import *
from util.getKVPath import getKVPath
import os

Builder.load_file(getKVPath(os.getcwd(), __file__))

class ROD_TestSettingsConfirmation(BaseScreen):
    height_num = StringProperty("N/A")
    plot = StringProperty("N/A")
    operator = StringProperty("N/A")
    folder = StringProperty("Default")

    def on_pre_enter(self):
        """Before the Screen loads, read the configuration file to get the current
        list of notes. Show the default buttons."""
        self.config = settings()
        self.height_num = str(self.config.get('height',0))
        self.plot = str(self.config.get('plot_num',0))
        self.operator = str(self.config.get('operator','N/A'))
        self.folder = str(self.config.get('folder','Default'))

    def on_leave(self):
        """When the screen leaves, save the current notes to the configuration file."""
        # if "Default" not in os.listdir('Tests/'):
        #     os.mkdir('Tests/Default')
