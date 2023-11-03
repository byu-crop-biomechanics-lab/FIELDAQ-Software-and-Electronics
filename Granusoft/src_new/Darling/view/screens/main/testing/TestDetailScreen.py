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
    y_max = NumericProperty(1)
    x_major = NumericProperty(1)
    y_major = NumericProperty(1)
    datasets = []
    pot_angle = []
    imu_angle = []
    force_app = []
    notes = []

    def __init__(self, **kwargs):
        super(BaseScreen, self).__init__(**kwargs)
        def gui_init(dt):
            self.test_notes_screen = self.manager.get_screen('test_notes_screen')
            self.parent_screen = self
        Clock.schedule_once(gui_init)

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

        self.graph = self.ids['graph_test']
        self.results_plot = MeshLinePlot(color=[1, 1, 1, 1])
        self.screenTitle.text = str(self.fileName[:-4])
        self.toggle_button = self.ids['imu_pot_toggle']
        self.toggle_button.bind(on_release = self.toggleButton)
        self.title_Text = self.ids['title_text']
        foldername = "Tests/"+config.get('selected_folder',0)+'/'
        with open(foldername + str(self.fileName)) as testFile:
            readCSV = csv.reader(testFile, delimiter=',')
            testData = 0
            for row in readCSV:
                if testData == 1:
                    self.pot_angle.append(row[1])
                    self.imu_angle.append(row[2])
                    self.force_app.append(row[3])
                if str(row[0]) == 'TIME (milliseconds)' and testData == 0:
                    testData = 1
                
                if 'POST' in row[0]:
                    if len(row[1]) !=0:
                        self.notes.append(str(row[1]))

        # Set the data
        self.ids['test_notes'].list_data = self.notes

        self.imu_points = [(float(self.imu_angle[i]), float(self.force_app[i])) for i in range(0, len(self.imu_angle))]
        self.imuXmax = math.ceil(max(float(self.imu_angle[i]) for i in range(0, len(self.imu_angle)))/10)*10
        self.imuXmajor = int(self.imuXmax/5)
        self.imu_title = 'X Load and IMU Data'
        self.pot_points = [(float(self.pot_angle[i]), float(self.force_app[i])) for i in range(0, len(self.pot_angle))]
        self.potXmax = math.ceil(max(float(self.pot_angle[i]) for i in range(0, len(self.pot_angle)))/10)*10
        self.potXmajor = int(self.potXmax/5)
        self.pot_title = 'X Load and Potentiometer Data'
        self.x_max = self.potXmax
        self.x_major = self.potXmajor
        self.y_max = math.ceil(max(float(self.force_app[i]) for i in range(0, len(self.force_app)))/15)*15
        self.y_major = int(self.y_max/5)
        self.results_plot.points = self.pot_points
        self.pot_plot = 1
        self.graph.add_plot(self.results_plot)
        self.title_Text.text = self.pot_title

    def toggleButton(self, obj):
        if self.pot_plot:
            self.graph.remove_plot(self.results_plot)
            self.results_plot.points = self.imu_points
            self.x_max = self.imuXmax
            self.x_major = self.imuXmajor
            self.graph.add_plot(self.results_plot)
            self.title_Text.text = self.imu_title
            self.pot_plot = 0
        else:
            self.graph.remove_plot(self.results_plot)
            self.results_plot.points = self.pot_points
            self.x_max = self.potXmax
            self.x_major = self.potXmajor
            self.graph.add_plot(self.results_plot)
            self.title_Text.text = self.pot_title
            self.pot_plot = 1

    def set_file(self, filename):
        self.fileName = filename[0]

    def on_leave(self):
        self.graph.remove_plot(self.results_plot)
        self.graph._clear_buffer()
        self.notes = []
    
    def update_notes(self):
        self.test_notes_screen.set_file(self.fileName)
        super(TestDetailScreen, self).move_to('test_notes_screen')