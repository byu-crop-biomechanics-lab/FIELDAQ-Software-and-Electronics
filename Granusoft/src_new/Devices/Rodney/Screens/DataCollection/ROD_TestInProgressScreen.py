"""
Test in Progress
"""

import datetime

from kivy.lang import Builder
from kivy.properties import NumericProperty
from kivy.properties import StringProperty
from kivy.properties import ListProperty
from kivy.clock import Clock
from Devices.Rodney.Data.Dataset import Dataset
from Devices.Rodney.Sensors import Sensor
from Devices.Rodney.Data.TestSingleton import TestSingleton

from util.BaseScreen import BaseScreen
from Devices.Rodney.Settings.configurator import SettingsSingleton as settings
from util.elements import *
import datetime
import time
import math

from kivy.garden.graph import MeshLinePlot
from util.getKVPath import getKVPath
import os

Builder.load_file(getKVPath(os.getcwd(), __file__))

INTERVAL = .003
SECOND_CAP = 1/INTERVAL

class ROD_TestInProgressScreen(BaseScreen):
    test_time = NumericProperty(0)
    x_max = NumericProperty()
    x_min = NumericProperty()
    y_max1 = NumericProperty()
    y_max2 = NumericProperty()
    y_min1 = NumericProperty()
    y_min2 = NumericProperty()
    x_major = NumericProperty()
    y_major1 = NumericProperty()
    y_major2 = NumericProperty()
    temperature = 0
    humidity = 0
    location = 0
    x_load = 0
    y_load = 0
    pot_angle = 0
    imu_angle = 0
    data_rate = 0
    second_counter = 0
    double_counter = 0
    start_time = 0
    start_timestamp = datetime.datetime.now().strftime("%I:%M:%S %p")

    def on_pre_enter(self):
        self.config = settings()
        self.test_time = 0
        self.temperature = 0
        self.humidity = 0
        self.location = 0
        self.x_load = 0
        self.y_load = 0
        self.pot_angle = 0
        self.imu_angle = 0
        self.data_rate = 0
        self.strain1 = 0
        self.strain2 = 0
        self.second_counter = 0
        self.double_counter = 0
        self.start_time = datetime.datetime.now()
        self.datasets = []
        self.x_min = 0
        self.y_min1 = 0
        self.y_min2 = 0
        self.y_max1 = 100
        self.y_max2 = 100
        self.x_major = int((self.x_max-self.x_min)/5)
        self.y_major1 = int((self.y_max1-self.y_min1)/5)
        self.y_major2 = int((self.y_max2-self.y_min2)/5)
        self.datasets = []
        self.test_sensor = Sensor()
        self.plot1 = MeshLinePlot(color=[1, 1, 1, 1])
        self.plot2 = MeshLinePlot(color=[1, 1, 1, 1])

        self.event = Clock.schedule_interval(self.update_dataset, INTERVAL)
        #ClockBaseInterruptBehavior.interupt_next_only = True
    def find_max_x_load(self):
        max = 0
        for dataset in self.datasets:
            if(dataset.x_load > max):
                max = dataset.x_load
        return max

    def update_dataset(self, obj):
        self.second_counter += 1
        time_delta = datetime.datetime.now() - self.start_time
        total_time_passed = time_delta.seconds + (time_delta.microseconds * .000001)
        self.test_time = time_delta.seconds
        if self.second_counter >= SECOND_CAP/2:
            self.double_counter += 1
            self.second_counter = 0
            self.graph1 = self.ids['graph_test1']
            self.graph2 = self.ids['graph_test2']
            self.graph1.remove_plot(self.plot1)
            self.graph2.remove_plot(self.plot2)
            self.graph1._clear_buffer()
            self.graph2._clear_buffer()
            self.plot1 = MeshLinePlot(color=[1, 1, 1, 1])
            self.plot2 = MeshLinePlot(color=[1, 1, 1, 1])
            last_index = len(self.datasets) - 1
            
            self.x_max = math.ceil(self.datasets[last_index].timestamp / 5) * 5
            self.y_min1 = max(self.y_min1, math.ceil(self.datasets[last_index].strain1)*0.8) # why are these 80% and 120% ?
            self.y_min2 = max(self.y_min2, math.ceil(self.datasets[last_index].strain2)*0.8)
            self.y_max1 = max(self.y_max1, math.ceil(self.datasets[last_index].strain1)*1.2)
            self.y_max2 = max(self.y_max2, math.ceil(self.datasets[last_index].strain2)*1.2)
            

            self.x_major = int((self.x_max-self.x_min)/5)
            self.y_major1 = int((self.y_max1-self.y_min1)/5)
            self.y_major2 = int((self.y_max2-self.y_min2)/5)

            self.plot1.points = [(self.datasets[i].timestamp, self.datasets[i].strain8[0]) for i in range(0, len(self.datasets), 5)]
            self.plot2.points = [(self.datasets[i].timestamp, self.datasets[i].strain8[1]) for i in range(0, len(self.datasets), 5)]
            
            self.graph1.add_plot(self.plot1)
            self.graph2.add_plot(self.plot2)

        sensor_values = self.test_sensor.get_sensor_data(adc_out=1) # FIXME THIS GETS RAW VOLTAGES
        self.strain8 = sensor_values["strain8"]
        self.whiskers = sensor_values["whiskers"]

        new_dataset = Dataset(total_time_passed, self.strain8, self.whiskers)
        self.datasets.append(new_dataset)

    def on_pre_leave(self):
        self.event.cancel()
        ts = TestSingleton()
        ts.clear_all()
        ts.set_height(str(self.config.get('height', "")))
        ts.set_plot(str(self.config.get('plot_num', "")))
        self.config.set('break_height', "N/A")

        ts.set_operator(str(self.config.get('operator', "")))
        ts.set_timestamp(self.start_timestamp)
        ts.set_datasets(self.datasets)
        self.datasets = []
        self.graph1.remove_plot(self.plot1)
        self.graph1._clear_buffer()
        self.graph2.remove_plot(self.plot2)
        self.graph2._clear_buffer()