"""
Shows all data: Temperature, Humidity, Location, Time, and all Sensor data
"""

from kivy.lang import Builder
from kivy.properties import NumericProperty
from kivy.properties import StringProperty
from kivy.properties import ListProperty
from kivy.clock import Clock
from Sensor import Sensor
import datetime
import time
import math
from TestSingleton import TestSingleton

from view.BaseScreen import BaseScreen
from view.StaticList import StaticList
from view.elements import *
import configurator as config
import csv
try:
    from sensors.connections import *
except:
    pass

from kivy.garden.graph import Graph, MeshLinePlot

Builder.load_file('view/screens/main/testing/TestDetailScreen.kv')

ONE_SEC = 1


class TestDetailScreen(BaseScreen):
    x_max = NumericProperty(1)
    y_max1 = NumericProperty(1)
    y_max2 = NumericProperty(1)
    x_major = NumericProperty(1)
    y_major1 = NumericProperty(1)
    y_major2 = NumericProperty(1)
    datasets = []

    def find_max_x_load(self):
        max = 0
        for dataset in self.datasets:
            if(dataset.x_load > max):
                max = dataset.x_load
        return max
    def on_pre_enter(self):
        sensor = Sensor()
        sensor.clear_gps_memory()

    def on_enter(self):
        self.graph1 = self.ids['graph_test1']
        self.graph2 = self.ids['graph_test2']
        self.plot1 = MeshLinePlot(color=[1, 1, 1, 1])
        self.plot2 = MeshLinePlot(color=[1, 1, 1, 1])

    def set_file(self, filename):
        self.fileName = filename

    def rootLodge_note(self):
        RLB = self.ids['RootLodgeButton']
        if self.lodgeFlag == "ROOT LODGE":
            self.lodgeFlag = "STALK LODGE"
            RLB.text = "Stalk\nLodge"
            RLB.background_color = (0,0,0,1)
        elif self.lodgeFlag == "STALK LODGE":
            self.lodgeFlag = "ROOT LODGE"
            RLB.background_color = (1,0,0,1)
            RLB.text = "Root\nLodge"
        else:
            self.lodgeFlag = "ROOT LODGE"
            RLB.background_color = (1,0,0,1)
            RLB.text = "Root\nLodge"

    def on_leave(self):
        self.graph1.remove_plot(self.plot1)
        self.graph1._clear_buffer()
        self.graph2.remove_plot(self.plot2)
        self.graph2._clear_buffer()
