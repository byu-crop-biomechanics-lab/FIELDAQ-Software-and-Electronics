"""
Testing Menu
"""

from kivy.lang import Builder
from kivy.properties import NumericProperty
from kivy.properties import StringProperty
from kivy.properties import ListProperty
from kivy.properties import ObjectProperty
from kivy.clock import Clock
from Sensor import Sensor
from kivy.uix.popup import Popup

from view.BaseScreen import BaseScreen
from view.StaticList import StaticList
import configurator as config
from view.elements import *

import datetime
import os
# import pytz
# from timezonefinder import TimezoneFinder

Builder.load_file('view/screens/main/TestingScreenAuto.kv')

ONE_SEC = 1
HEIGHT_INTERVAL = 0.004


class TestingScreenAuto(BaseScreen):
    sensor = Sensor()
    load_cell_height = StringProperty("N/A")
    loadCellHeightUnits = " cm"
    plot = StringProperty("N/A")
    operator = StringProperty("N/A")
    time = StringProperty("N/A")
    # time_zone = StringProperty("N/A")
    current_date = StringProperty("N/A")
    date_time = StringProperty("N/A")
    folder = StringProperty("N/A")
    datasets = []




    def on_pre_enter(self):
        """Before the Screen loads, read the configuration file to get the current
        list of notes. Show the default buttons."""
        # self.time_zone = self.find_time_zone()
        self.event = Clock.schedule_interval(self.update_time, ONE_SEC)
        self.event2 = Clock.schedule_interval(self.update_height, HEIGHT_INTERVAL)
        self.load_cell_height = self.get_load_cell_sensor_height()
        config.set('height', float(self.load_cell_height))
        self.plot = str(config.get('plot_num', 0))
        self.operator = str(config.get('operator', 'N/A'))
        self.folder = str(config.get('folder', 'N/A'))
        self.current_date = datetime.date.today().strftime("%d/%m/%Y")
        # Get notes from config file
        notes = config.get('notes', {
            "pretest": [],
            "posttest": [],
            "bank": []
        })
        # Set the data
        self.ids['pretest'].list_data = notes["pretest"]
        self.ids['posttest'].list_data = notes["posttest"]

    # def find_time_zone(self):
    #     self.sensor.get_header_data()
    #     sensor_data = self.sensor.get_sensor_data()
    #     obj = TimezoneFinder()
    #     return obj.timezone_at(lat = sensor_data["Location"][0], lng = sensor_data["Location"][1])

    def update_time(self,obj):
        # tz = pytz.timezone(self.time_zone) 
        self.time = datetime.datetime.now().strftime("%I:%M:%S %p")
        self.date_time = self.current_date+": "+self.time

    def update_height(self,obj):
        self.load_cell_height = self.get_load_cell_sensor_height()

    def on_leave(self):
        self.event.cancel()

    def get_load_cell_sensor_height(self):
        sensor_data = self.sensor.get_sensor_data(0)
        return str("%.2f" % sensor_data["Load Cell Height"])

    # def export_tests(self, obj):
    #         if not os.path.ismount(self.USB_TEST_FOLDERS_PATH):
    #             try:
    #                 os.system("sudo mount -t vfat -o uid=pi,gid=pi /dev/sda1 /mnt/usbStick")
    #             except:
    #                 print("USB Not Mounted")
    #         self._popup = SaveConfirmDialog(save=self.usbSave, pathSelector=self.pathSelector, cancel=self.dismiss_popup)
    #         self._popup.open()