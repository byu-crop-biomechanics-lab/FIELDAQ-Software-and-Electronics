"""
The main screen contains three buttons for navigation:
View Images, Testing, and Settings

It also shows environment data: Temperature, Humidity, Location, and Time.
"""

from kivy.lang import Builder
from kivy.properties import StringProperty
from kivy.clock import Clock
from view.BaseScreen import BaseScreen
from Sensor import Sensor
import datetime

Builder.load_file('view/screens/camera/CameraMainScreen.kv')

INTERVAL = .004
INTERVAL2 = 5

class CameraMainScreen(BaseScreen):
    sensor = Sensor()
    temperature = StringProperty("0")
    humidity = StringProperty("0")
    location = StringProperty("1.12, 3.58")
    time = StringProperty("0")
    def on_pre_enter(self):
        self.test_time = 0
        self.event = Clock.schedule_interval(self.update_time, INTERVAL)
        self.event2 = Clock.schedule_interval(self.update_values, INTERVAL2)
        #self.update_values
        self.sensor_man = Sensor()
        if self.sensor_man.REAL_DATA is False:
            self.ids['warning_text'].text = 'WARNING: Using falsified data.  Check console for stack trace.'

    def on_enter(self):
        self.event3 = Clock.schedule_interval(self.update_values, 0.01)

    def update_time(self, obj):
        self.time = datetime.datetime.now().strftime("%I:%M:%S %p")

    def update_values(self, obj):
        self.sensor.get_header_data()
        sensor_data = self.sensor.get_sensor_data()
        self.temperature = str("%.0f" % sensor_data["Temperature"])
        self.humidity = str("%.0f" % sensor_data["Humidity"])
        self.location = ('(' + str("%.4f" % sensor_data["Location"][0]) + ', ' + str("%.4f" % sensor_data["Location"][1]) + ')')
        try:
            self.event3.cancel()
        except:
            pass

    def on_leave(self):
        self.event.cancel()
        self.event2.cancel()
