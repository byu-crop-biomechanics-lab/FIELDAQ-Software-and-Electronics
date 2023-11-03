"""
Test settings confirmation menu. This is to make sure the user sets the correct
data for the test.
"""

from kivy.lang import Builder
from kivy.properties import StringProperty

from view.BaseScreen import BaseScreen
import configurator as config
from view.elements import *

Builder.load_file('view/screens/main/testing/TestSettingsConfirmation.kv')

class TestSettingsConfirmation(BaseScreen):
    height_num = StringProperty("N/A")
    plot = StringProperty("N/A")
    operator = StringProperty("N/A")

    def on_pre_enter(self):
        """Before the Screen loads, read the configuration file to get the current
        list of notes. Show the default buttons."""
        self.height_num = str(config.get('height',0))
        self.plot = str(config.get('plot_num',0))
        self.operator = str(config.get('operator','N/A'))
