"""
The main screen contains four buttons for navigation:
Settings, Testing, Live Feed, and Exit

It also shows environment data: Temperature, Humidity, Location, and Time.
"""

from kivy.lang import Builder
from kivy.properties import StringProperty
from kivy.clock import Clock
from view.BaseScreen import BaseScreen
import datetime

from Sensor import Sensor

Builder.load_file('view/screens/main/MainScreen.kv')

INTERVAL = .004

class MainScreen(BaseScreen):
    temperature = StringProperty("0")
    humidity = StringProperty("0")
    location = StringProperty("0.00,0.00")
    time = StringProperty("0")
    def on_pre_enter(self):
        self.test_time = 0
        self.event = Clock.schedule_interval(self.update_values, INTERVAL)
        self.sensor_man = Sensor()
        if self.sensor_man.REAL_DATA is False:
            self.ids['warning_text'].text = 'WARNING: Using fake data.  Check console for stack trace.'

    def update_values(self, obj):
        self.time = datetime.datetime.now().strftime("%I:%M:%S %p")

    def on_leave(self):
        self.event.cancel()
