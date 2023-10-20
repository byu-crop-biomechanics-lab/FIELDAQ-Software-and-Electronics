"""
Shows all data: Temperature, Humidity, Location, Time, and all Sensor data
"""

from kivy.lang import Builder
from kivy.properties import NumericProperty, StringProperty
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
    x_max_imu = NumericProperty(1)
    xlabel = StringProperty("Pot Angle")
    xmajor = NumericProperty(1)
    xmax = NumericProperty(1)
    y_max = NumericProperty(1)
    x_major = NumericProperty(1)
    x_major_imu = NumericProperty(1)
    y_major = NumericProperty(1)
    toggle = 0

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
        self.plot_imu = MeshLinePlot(color=[1, 1, 1, 1])
        ts = TestSingleton()
        self.datasets = ts.get_datasets()
        last_index = len(self.datasets) - 1

        if math.ceil(max(self.datasets[i].pot_angle for i in range(0, len(self.datasets))) / 100) > 0 or math.ceil(max(self.datasets[i].imu_angle for i in range(0, len(self.datasets))) / 100) > 0:
            self.x_max = math.ceil(max(self.datasets[i].pot_angle for i in range(
                0, len(self.datasets))) / 100) * 100
            self.x_max_imu = math.ceil(
                max(self.datasets[i].imu_angle for i in range(0, len(self.datasets))) / 100) * 100
        else:
            self.x_max = 100
            self.x_max_imu = 100
        if math.ceil(max(self.datasets[i].x_load for i in range(0, len(self.datasets))) / 5) > 0:
            self.y_max = math.ceil(
                max(self.datasets[i].x_load for i in range(0, len(self.datasets))) / 5) * 5
        else:
            self.y_max = 5
        self.x_major = int(self.x_max/5)
        self.x_major_imu = int(self.x_max_imu/5)
        self.y_major = int(self.y_max/5)

        self.plot.points = [(self.datasets[i].pot_angle, self.datasets[i].x_load)
                            for i in range(0, len(self.datasets))]
        self.plot_imu.points = [(self.datasets[i].imu_angle, self.datasets[i].x_load)
                                for i in range(0, len(self.datasets))]

        self.xlabel = 'Pot Angle (deg)'
        self.xmajor = self.x_major
        self.xmax = self.x_max

        self.graph.add_plot(self.plot)

    def save_post_notes(self):
        """Saves selected post test notes."""

        ts = TestSingleton()
        ts.set_post_notes(self.ids["posttest"].remove_selected())

    def on_leave(self):
        self.graph.remove_plot(self.plot)
        self.graph._clear_buffer()

    def toggle_button(self):
        if  self.toggle:
            self.graph.remove_plot(self.plot_imu)
            self.xlabel = 'Pot Angle (deg)'
            self.xmajor = self.x_major
            self.xmax = self.x_max
            self.graph.add_plot(self.plot)
            self.toggle = 0
        else:
            self.graph.remove_plot(self.plot)
            self.xlabel = 'IMU Angle (deg)'
            self.xmajor = self.x_major_imu
            self.xmax = self.x_max_imu
            self.graph.add_plot(self.plot_imu)
            self.toggle = 1

    def check_height_sensor_status(self):
        if str(config.get('height_sensor', 0)) == "ON":
            self.next_screen = 'testing_screen_auto'
        else:
            self.next_screen = 'testing_screen'