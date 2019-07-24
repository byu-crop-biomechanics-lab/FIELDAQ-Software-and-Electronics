"""
Testing Menu
"""

from kivy.lang import Builder
from kivy.properties import NumericProperty
from kivy.properties import StringProperty
from kivy.properties import ListProperty
from kivy.clock import Clock
from Sensor import Sensor

from view.BaseScreen import BaseScreen
from view.StaticList import StaticList
import configurator as config
from view.elements import *
import datetime

Builder.load_file('view/screens/main/TestingScreen.kv')

ONE_SEC = 1

class TestingScreen(BaseScreen):
    height_num = StringProperty("N/A")
    plot = StringProperty("N/A")
    operator = StringProperty("N/A")
    time = StringProperty("N/A")
    datasets = []

    def on_pre_enter(self):
        """Before the Screen loads, read the configuration file to get the current
        list of notes. Show the default buttons."""
        self.event = Clock.schedule_interval(self.update_time, ONE_SEC)
        self.height_num = str(config.get('height',0))
        self.plot = str(config.get('plot_num',0))
        self.operator = str(config.get('operator','N/A'))
        self.time = datetime.datetime.now().strftime("%I:%M:%S %p")
        # Get notes from config file
        notes = config.get('notes', {
            "pretest": [],
            "posttest": [],
            "bank": []
        })
        # Set the data
        self.ids['pretest'].list_data = notes["pretest"]
        self.ids['posttest'].list_data = notes["posttest"]

    def update_time(self, obj):
        self.time = datetime.datetime.now().strftime("%I:%M:%S %p")

    def on_leave(self):
        self.event.cancel()
