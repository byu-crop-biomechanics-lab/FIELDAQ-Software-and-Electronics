"""
Test in Progress
"""

import datetime

from kivy.lang import Builder
from kivy.properties import NumericProperty
from kivy.properties import StringProperty
from kivy.properties import ListProperty
from kivy.clock import Clock
from Dataset import Dataset
from Sensor import Sensor
from TestSingleton import TestSingleton
from Sensor import Sensor

from view.BaseScreen import BaseScreen
import configurator as config
from kivy.config import Config as KivyConfig
from view.elements import *
import datetime
import time
import math

from kivy.garden.graph import Graph, MeshLinePlot

Builder.load_file('view/screens/main/testing/TestInProgressScreen.kv')

INTERVAL = .003
SECOND_CAP = 1/INTERVAL

class TestInProgressScreen(BaseScreen):
    test_time = NumericProperty(0)
    x_max = NumericProperty()
    y_max1 = NumericProperty()
    y_max2 = NumericProperty()
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
        self.test_time = 0
        self.temperature = 0
        self.humidity = 0
        self.location = 0
        self.x_load = 0
        self.y_load = 0
        self.pot_angle = 0
        self.imu_angle = 0
        self.data_rate = 0
        self.second_counter = 0
        self.double_counter = 0
        self.start_time = datetime.datetime.now()
        self.datasets = []
        self.x_max1 = 5
        self.y_max1 = 100
        self.y_max2 = 5
        self.x_major = int(self.x_max/5)
        self.y_major1 = int(self.y_max1/5)
        self.y_major2 = int(self.y_max2/5)
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
            self.y_max1 = max(self.y_max1, math.ceil(self.datasets[last_index].pot_angle / 100) * 100)
            self.y_max2 = max(self.y_max2, math.ceil(self.datasets[last_index].x_load / 5) * 5)

            self.x_major = int(self.x_max/5)
            self.y_major1 = int(self.y_max1/5)
            self.y_major2 = int(self.y_max2/5)

            self.plot1.points = [(self.datasets[i].timestamp, self.datasets[i].pot_angle) for i in range(0, len(self.datasets), 5)]
            self.plot2.points = [(self.datasets[i].timestamp, self.datasets[i].x_load) for i in range(0, len(self.datasets), 5)]
            
            self.graph1.add_plot(self.plot1)
            self.graph2.add_plot(self.plot2)



        sensor_values = self.test_sensor.get_sensor_data()
        self.x_load = sensor_values["X Load"]
        self.y_load = sensor_values["Y Load"]
        self.pot_angle = sensor_values["Pot Angle"]
        self.imu_angle = sensor_values["IMU Angle"]


        new_dataset = Dataset(total_time_passed, self.x_load, self.y_load, self.pot_angle, self.imu_angle, self.data_rate)
        self.datasets.append(new_dataset)

    def on_pre_leave(self):
        self.event.cancel()
        ts = TestSingleton()
        ts.clear_all()
        ts.set_height(str(config.get('height', "")))
        ts.set_plot(str(config.get('plot_num', "")))
        config.set('break_height', "N/A")

        ts.set_operator(str(config.get('operator', "")))
        ts.set_timestamp(self.start_timestamp)
        ts.set_datasets(self.datasets)
        self.datasets = []
        self.graph1.remove_plot(self.plot1)
        self.graph1._clear_buffer()
        self.graph2.remove_plot(self.plot2)
        self.graph2._clear_buffer()