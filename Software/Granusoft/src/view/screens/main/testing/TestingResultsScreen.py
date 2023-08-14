"""
Shows all data: Temperature, Humidity, Location, Time, and all Sensor data
"""

from kivy.lang import Builder
from kivy.properties import NumericProperty
from Sensor import Sensor
import math
from TestSingleton import TestSingleton

from view.BaseScreen import BaseScreen
from view.StaticList import StaticList
from view.elements import *
import configurator as config
try:
    from sensors.connections import *
except:
    pass

from kivy.garden.graph import MeshLinePlot

Builder.load_file('view/screens/main/testing/TestingResultsScreen.kv')

class TestingResultsScreen(BaseScreen):
    x_max = NumericProperty(1)
    y_max = NumericProperty(1)
    x_major = NumericProperty(1)
    y_major = NumericProperty(1)
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

        # Get notes from config file
        notes = config.get('notes', {"posttest": []})

        # Set the data
        self.ids['posttest'].list_data = notes["posttest"]

    def on_enter(self):
        self.graph = self.ids['graph_test']
        self.plot = MeshLinePlot(color=[1, 1, 1, 1])
        ts = TestSingleton()
        self.datasets = ts.get_datasets()
        last_index = len(self.datasets) - 1

        if math.ceil(max(self.datasets[i].pot_angle for i in range(0,len(self.datasets))) / 100) > 0:
            self.x_max = math.ceil(max(self.datasets[i].pot_angle for i in range(0,len(self.datasets))) / 100) * 100
        else:
            self.x_max = 100
        if math.ceil(max(self.datasets[i].x_load for i in range(0,len(self.datasets)))/ 5) > 0:
            self.y_max = math.ceil(max(self.datasets[i].x_load for i in range(0,len(self.datasets)))/ 5) * 5
        else:
            self.y_max = 5
        self.x_major = int(self.x_max/5)
        self.y_major = int(self.y_max/5)

        self.plot.points = [(self.datasets[i].pot_angle, self.datasets[i].x_load) for i in range(0, len(self.datasets))]

        self.graph.add_plot(self.plot)

    def save_post_notes(self):
        """Saves selected post test notes."""

        ts = TestSingleton()
        ts.set_post_notes(self.ids["posttest"].remove_selected())

    def on_leave(self):
        self.graph.remove_plot(self.plot)
        self.graph._clear_buffer()