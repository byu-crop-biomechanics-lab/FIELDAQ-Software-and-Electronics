"""
Testing Menu
"""

from kivy.lang import Builder
from kivy.properties import NumericProperty
from kivy.properties import StringProperty
from kivy.properties import ListProperty
from kivy.clock import Clock
from Devices.Rodney.Sensors import Sensor

from util.BaseScreen import BaseScreen
from util.StaticList import StaticList
from Devices.Rodney.Settings.configurator import SettingsSingleton as settings
from util.elements import *
import datetime
from util.getKVPath import getKVPath
import os

Builder.load_file(getKVPath(os.getcwd(), __file__))

ONE_SEC = 1


class ROD_TestingScreen(BaseScreen):
    sensor = Sensor()
    load_cell_height = StringProperty("N/A")
    loadCellHeightUnits = " cm"
    plot = StringProperty("N/A")
    operator = StringProperty("N/A")
    time = StringProperty("0")
    current_date = StringProperty("N/A")
    date_time = StringProperty("N/A")
    # time_zone = StringProperty("N/A")
    folder = StringProperty("N/A")
    datasets = []

    def on_pre_enter(self):
        """Before the Screen loads, read the configuration file to get the current
        list of notes. Show the default buttons."""
        # self.time_zone = self.find_time_zone()
        self.event = Clock.schedule_interval(self.update_time, ONE_SEC)
        self.load_cell_height = self.get_height()
        self.config = settings()
        self.config.set('height', float(self.load_cell_height))
        self.plot = str(self.config.get('plot_num', 0))
        self.operator = str(self.config.get('operator', 'N/A'))
        self.folder = str(self.config.get('folder', 'N/A'))
        self.current_date = datetime.date.today().strftime("%d/%m/%Y")
        # Get notes from config file
        notes = self.config.get('notes', {
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

    def on_leave(self):
        self.event.cancel()
        folder_list = self.config.get('folders', "")
        input = self.config.get('folder', "")
        if folder_list == 0 or input not in folder_list:
            try:
                os.mkdir('Tests/'+str(self.config.get('folder', 0)))
            except:
                pass
            folder_list = folder_list + " " + input
            self.config.set('folders', folder_list)


    def get_height(self):
        return str(self.config.get('height', 0))
