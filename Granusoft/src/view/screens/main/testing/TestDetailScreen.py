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
import numpy as np
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
    pot_angle = []
    imu_angle = []
    force_app = []

    def find_max_x_load(self):
        max = 0
        for dataset in self.datasets:
            if(dataset.x_load > max):
                max = dataset.x_load
        return max
    def on_pre_enter(self):
        sensor = Sensor()
        sensor.clear_gps_memory()
        self.screenTitle = self.ids['testTitle']

    def on_enter(self):
        self.graph1 = self.ids['graph_test1']
        self.plot1 = MeshLinePlot(color=[1, 1, 1, 1])
        self.screenTitle.text = str(self.fileName[:-4])
        with open('Tests/' + str(self.fileName)) as testFile:
            readCSV = csv.reader(testFile, delimiter=',')
            testData = 0
            for row in readCSV:
                if testData == 1:
                    self.pot_angle.append(row[1])
                    self.imu_angle.append(row[2])
                    self.force_app.append(row[3])
                if str(row[0]) == 'TIME (s)' and testData == 0:
                    testData = 1
        self.plot1.points = [(float(self.pot_angle[i]), float(self.force_app[i])) for i in range(0, len(self.pot_angle))]
        self.x_max = math.ceil(max(float(self.pot_angle[i]) for i in range(0, len(self.pot_angle)))*1.05)
        self.x_major = int(self.x_max/5)
        self.y_max1 = math.ceil(max(float(self.force_app[i]) for i in range(0, len(self.force_app)))*1.05)
        self.y_major1 = int(self.y_max1/5)
        self.graph1.add_plot(self.plot1)

    def set_file(self, filename):
        self.fileName = filename[0]

    def on_leave(self):
        self.graph1.remove_plot(self.plot1)
        self.graph1._clear_buffer()
