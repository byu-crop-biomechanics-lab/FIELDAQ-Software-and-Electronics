"""
This screen is designed to test the precision of the GPS unit
by taking measurements every 15 seconds while the operator
walks on a predetermined path. The coordinates can be uploaded
to google to compare the precision of the gps.
"""

from kivy.lang import Builder
from kivy.properties import NumericProperty
from kivy.properties import StringProperty
from kivy.properties import ListProperty
from kivy.clock import Clock
from Sensor import Sensor
import datetime

from view.BaseScreen import BaseScreen
from view.elements import *
try:
    from sensors.connections import *
except:
    pass
import csv

Builder.load_file('view/screens/settings/GPSMapScreen.kv')

INTERVAL = 15

class GPSMapScreen(BaseScreen):
    sensor = Sensor()
    def update_gps_location(self):
        gps.update()
            # Turn button red or something. Have csvwrite start writing and
            # have stop button send stop signal to csvwrite.

    def start_gps_test(self):
        self.ids['test_text'].text = 'GPS TESTING IN PROGRESS'
        dt = datetime.datetime.now()
        self.filename = 'Tests/' + dt.strftime('%Y_%m_%d_%H_%M_%S') + '.csv'
        with open(self.filename, 'w+', newline='') as csvFile:
            self.writer = csv.writer(csvFile)
            self.writer.writerow(['Item Number', 'Latitude', 'Longitude'])
            try:
                gps.update()
            except:
                pass
            self.sensor.get_header_data()
            sensor_data = self.sensor.get_sensor_data()
            self.writer.writerow([dt.strftime('%H_%M_%S'), str("%.7f" % sensor_data["Location"][0]), str("%.7f" % sensor_data["Location"][1])])
            self.event = Clock.schedule_interval(self.schedule_gps, INTERVAL)
        csvFile.close()

    def schedule_gps(self, obj):
        try:
            gps.update()
        except:
            pass
        self.sensor.get_header_data()
        sensor_data = self.sensor.get_sensor_data()
        dt = datetime.datetime.now()
        with open(self.filename, 'a', newline='') as csvFile:
            self.writer = csv.writer(csvFile)
            self.writer.writerow([dt.strftime('%H_%M_%S'), str("%.7f" % sensor_data["Location"][0]), str("%.7f" % sensor_data["Location"][1])])
        csvFile.close()

    def stop_gps_test(self):
        self.ids['test_text'].text = 'GPS TESTING DONE'
        self.event.cancel()

    def on_leave(self):
        self.ids['test_text'].text = 'GPS Testing'
        try:
            self.event.cancel()
        except:
            pass
