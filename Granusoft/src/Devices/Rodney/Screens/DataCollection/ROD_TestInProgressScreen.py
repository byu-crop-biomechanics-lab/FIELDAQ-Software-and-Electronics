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
import numpy as np

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
        self.x_max = 20
        self.y_min1 = -6.6
        self.y_min2 = -6.6
        self.y_max1 = 6.6
        self.y_max2 = 6.6
        self.x_major = int((self.x_max-self.x_min)/5)
        self.y_major1 = int((self.y_max1-self.y_min1)/5)
        self.y_major2 = int((self.y_max2-self.y_min2)/5)
        self.datasets = []
        self.test_sensor = Sensor()
        self.plot1 = MeshLinePlot(color=[1, 0, 0, 1])
        self.plot2 = MeshLinePlot(color=[0, 0, 1, 1])
        self.plot3 = MeshLinePlot(color=[1, 0, 0, 1])
        self.plot4 = MeshLinePlot(color=[0, 0, 1, 1])
        self.graph1 = self.ids['graph_test1']
        self.graph2 = self.ids['graph_test2']

        self.plot1.points = []
        self.plot2.points = []
        self.plot3.points = []
        self.plot4.points = []
        self.graph1.add_plot(self.plot1)
        self.graph1.add_plot(self.plot2)
        self.graph2.add_plot(self.plot3)
        self.graph2.add_plot(self.plot4)

        self.event = Clock.schedule_interval(self.update_dataset, INTERVAL)
        #ClockBaseInterruptBehavior.interupt_next_only = True

    def update_dataset(self, obj):
        self.second_counter += 1
        time_delta = datetime.datetime.now() - self.start_time
        total_time_passed = time_delta.seconds + (time_delta.microseconds * .000001)
        self.test_time = time_delta.seconds
        if len(self.datasets) != 0 and self.second_counter >= 5: # delay to allow plots to update
            self.double_counter += 1
            self.second_counter = 0
            self.graph1._clear_buffer()
            self.graph2._clear_buffer()
            
            # Setting the min and max of the visual plot
            self.x_max = max(20, math.ceil(self.datasets[-1].timestamp / 5) * 5) # set plot x to 20 or larger
            self.x_min = max(0, self.x_max - 20) # only show last 20 seconds

            self.y_min1 = min(self.y_min1, math.ceil(self.datasets[-1].strain8[0])*1.2)
            self.y_min1 = min(self.y_min1, math.ceil(self.datasets[-1].strain8[1])*1.2)
            self.y_max1 = max(self.y_max1, math.ceil(self.datasets[-1].strain8[0])*1.2)
            self.y_max1 = max(self.y_max1, math.ceil(self.datasets[-1].strain8[1])*1.2)

            self.y_min2 = min(self.y_min2, math.ceil(self.datasets[-1].strain8[2])*1.2)
            self.y_min2 = min(self.y_min2, math.ceil(self.datasets[-1].strain8[3])*1.2)
            self.y_max2 = max(self.y_max2, math.ceil(self.datasets[-1].strain8[2])*1.2)
            self.y_max2 = max(self.y_max2, math.ceil(self.datasets[-1].strain8[3])*1.2)
            
            self.x_major = int((self.x_max-self.x_min)/5)
            self.y_major1 = int((self.y_max1-self.y_min1)/5)
            self.y_major2 = int((self.y_max2-self.y_min2)/5)

            self.plot1.points.append((self.datasets[-1].timestamp, self.datasets[-1].strain8[0]))
            self.plot2.points.append((self.datasets[-1].timestamp, self.datasets[-1].strain8[1]))
            self.plot3.points.append((self.datasets[-1].timestamp, self.datasets[-1].strain8[2]))
            self.plot4.points.append((self.datasets[-1].timestamp, self.datasets[-1].strain8[3]))

        sensor_values = self.test_sensor.get_sensor_data(adc_out=1) # FIXME THIS GETS RAW VOLTAGES
        self.strain8 = sensor_values["strain8"]
        self.whiskerFront = sensor_values["WhiskerFront"]
        self.whiskerBack  = sensor_values['WhiskerBack']

        new_dataset = Dataset(total_time_passed, self.strain8, self.whiskerFront, self.whiskerBack)
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
        self.graph1.remove_plot(self.plot2)
        self.graph1._clear_buffer()
        self.graph2.remove_plot(self.plot3)
        self.graph2.remove_plot(self.plot4)
        self.graph2._clear_buffer()