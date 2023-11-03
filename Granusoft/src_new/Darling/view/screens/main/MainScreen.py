"""
The main screen contains four buttons for navigation:
Settings, Testing, Live Feed, and Exit

It also shows environment data: Temperature, Humidity, Location, and Time.
"""

from kivy.lang import Builder
from kivy.properties import StringProperty
from kivy.clock import Clock
from view.BaseScreen import BaseScreen
from Sensor import Sensor
import datetime
# import pytz
# from timezonefinder import TimezoneFinder

Builder.load_file('view/screens/main/MainScreen.kv')

INTERVAL = .004
INTERVAL2 = 5

class MainScreen(BaseScreen):
    sensor = Sensor()
    location = StringProperty("1.12, 3.58")
    time = StringProperty("0")
    current_date = StringProperty("DD/MM/YYYY")
    load_cell_height = StringProperty("0.00")
    #time_zone = StringProperty("N/A")
    loadCellHeightUnits = 'cm'

    def on_pre_enter(self):
        #self.time_zone = self.find_time_zone()
        self.test_time = 0
        self.event = Clock.schedule_interval(self.update_time, INTERVAL)
        self.event2 = Clock.schedule_interval(self.update_values, INTERVAL2)
        self.sensor_man = Sensor()
        if self.sensor_man.REAL_DATA is False:
            self.ids['warning_text'].text = 'WARNING: Using fake data.  Check console for stack trace.'

    def on_enter(self):
        self.event3 = Clock.schedule_interval(self.update_values, 0.01)

    def update_time(self, obj):
        self.time = datetime.datetime.now().strftime("%I:%M:%S %p") 
        # tz = pytz.timezone(self.time_zone) 
        # self.time = datetime.datetime.now(tz).strftime("%I:%M:%S %p")

    def update_values(self, obj):
        self.sensor.get_header_data()
        sensor_data = self.sensor.get_sensor_data()
        self.current_date = datetime.date.today().strftime("%d/%m/%Y")
        self.load_cell_height = str("%.2f" % sensor_data["Load Cell Height"])
        self.location = ('(' + str("%.4f" % sensor_data["Location"][0]) + ', ' + str("%.4f" % sensor_data["Location"][1]) + ')')
        try:
            self.event3.cancel()
        except:
            pass
    
    # def find_time_zone(self):
    #     self.sensor.get_header_data()
    #     sensor_data = self.sensor.get_sensor_data()
    #     obj = TimezoneFinder()
    #     return obj.timezone_at(lat = sensor_data["Location"][0], lng = sensor_data["Location"][1])

    def on_leave(self):
        self.event.cancel()
        self.event2.cancel()
