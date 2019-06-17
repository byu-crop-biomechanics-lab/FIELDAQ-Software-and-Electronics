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

from kivy.garden.graph import Graph, MeshLinePlot

Builder.load_file('view/screens/main/testing/TestingResultsScreen.kv')

ONE_SEC = 1


class TestingResultsScreen(BaseScreen):
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

    def on_enter(self):
        self.graph1 = self.ids['graph_test1']
        self.graph2 = self.ids['graph_test2']
        self.plot1 = MeshLinePlot(color=[1, 1, 1, 1])
        self.plot2 = MeshLinePlot(color=[1, 1, 1, 1])
        ts = TestSingleton()
        self.datasets = ts.get_datasets()
        last_index = len(self.datasets) - 1

        self.x_max = math.ceil(self.datasets[last_index].timestamp / 5) * 5
        #self.y_max = math.ceil(self.find_max_x_load() / 10000) * 10000
        if math.ceil(max(self.datasets[i].pot_angle for i in range(0,len(self.datasets))) / 250) > 0:
            self.y_max1 = math.ceil(max(self.datasets[i].pot_angle for i in range(0,len(self.datasets))) / 250) * 250
        else:
            self.y_max1 = 250
        if math.ceil(max(self.datasets[i].x_load for i in range(0,len(self.datasets)))/ 250) > 0:
            self.y_max2 = math.ceil(max(self.datasets[i].x_load for i in range(0,len(self.datasets)))/ 250) * 250
        else:
            self.y_max2 = 250
        self.x_major = int(self.x_max/5)
        self.y_major1 = int(self.y_max1/5)
        self.y_major2 = int(self.y_max2/5)

        self.plot1.points = [(self.datasets[i].timestamp, self.datasets[i].pot_angle) for i in range(0, len(self.datasets))]
        self.plot2.points = [(self.datasets[i].timestamp, self.datasets[i].x_load) for i in range(0, len(self.datasets))]
        #for i in range(0,len(self.datasets)):
        #    print("Time:",self.datasets[i].timestamp," -- X_Load:", self.datasets[i].x_load)

        self.graph1.add_plot(self.plot1)
        self.graph2.add_plot(self.plot2)

        self.lodgeFlag = "STALK LODGE"
        RLB = self.ids['RootLodgeButton']
        RLB.text = "Stalk\nLodge"

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

    def save_test(self):
        ts = TestSingleton()
        self.datasets = ts.get_datasets()
        ts.set_break_height(str(config.get('break_height', 0)))

        #Prepare the notes
        notes = config.get('notes', {
            "pretest": [],
            "posttest": [],
            "bank": []
        })
        pre_notes = notes["pretest"]
        post_notes = notes["posttest"]
        while(len(pre_notes) < 5):
            pre_notes.append('')
        while(len(post_notes) < 5):
            post_notes.append('')
        dt = datetime.datetime.now()
        filename = 'Tests/' + dt.strftime('%Y_%m_%d_%H_%M_%S') + '.csv'


        sensor = Sensor()
        sensor.get_header_data()
        sensor_data = sensor.get_sensor_data()
        temperature = str(sensor_data["Temperature"])
        humidity = str(sensor_data["Humidity"])
        location = [str("%.5f" % sensor_data["Location"][0]), str("%.5f" % sensor_data["Location"][1])]

        with open(filename, 'w+', newline='') as csvFile:
            writer = csv.writer(csvFile)
            writer.writerow(['----------META DATA----------'])
            writer.writerow(['SOFTWARE VERSION', '2.1.0'])
            writer.writerow(['DEVICE OPERATOR', str(config.get('operator', 0))])
            writer.writerow(['----------TEST ATTRIBUTES----------'])
            writer.writerow(['FIELD', 'VALUE', 'UNIT'])
            writer.writerow(['YEAR', dt.strftime("%Y")])
            writer.writerow(['MONTH', dt.strftime("%m")])
            writer.writerow(['DAY', dt.strftime("%d")])
            writer.writerow(['TIME', dt.strftime("%H:%M:%S"), 'Local Time Zone'])
            writer.writerow(['PLOT', str(config.get('plot_num', 0)), '#'])
            writer.writerow(['HEIGHT', str(config.get('height', 0)), 'cm'])
            writer.writerow(['TEMPERATURE', temperature, 'C'])
            writer.writerow(['HUMIDITY', humidity, '%'])
            writer.writerow(['LATITUDE', location[0], ' angular degrees'])
            writer.writerow(['LONGITUDE', location[1], ' angular degrees'])
            writer.writerow(['----------OPTIONAL DATA----------'])
            writer.writerow(['PRE_TEST_NOTE_1', pre_notes[0]])
            writer.writerow(['PRE_TEST_NOTE_2', pre_notes[1]])
            writer.writerow(['PRE_TEST_NOTE_3', pre_notes[2]])
            writer.writerow(['PRE_TEST_NOTE_4', pre_notes[3]])
            writer.writerow(['PRE_TEST_NOTE_5', pre_notes[4]])
            writer.writerow(['POST_TEST_NOTE_1', post_notes[0]])
            writer.writerow(['POST_TEST_NOTE_2', post_notes[1]])
            writer.writerow(['POST_TEST_NOTE_3', post_notes[2]])
            writer.writerow(['POST_TEST_NOTE_4', post_notes[3]])
            writer.writerow(['POST_TEST_NOTE_5', post_notes[4]])
            writer.writerow(['BREAK_HEIGHT', str(config.get('break_height', 0)), 'cm'])
            writer.writerow(['LODGE_TYPE', self.lodgeFlag])
            writer.writerow(['LCA_WEIGTH', '0', 'g'])
            writer.writerow(['----------SENSOR CALIBRATION DATA (stored_value*A + B = raw_data)------'])
            writer.writerow(['SENSOR', 'A', 'B', 'UNIT', 'ID'])
            writer.writerow(['LOAD_X', '0', '0', 'N', 'loadx1'])
            writer.writerow(['LOAD_Y', '0', '0', 'Newton', 'loady1'])
            writer.writerow(['IMU', '0', '0', 'Deg', 'imu1'])
            writer.writerow(['POT', '0', '0', 'Deg', 'pot1'])
            writer.writerow(['TEMP', '0', '0', 'C', 'temp1'])
            writer.writerow(['HUM', '0', '0', '%', 'hum1'])
            writer.writerow(['----------TEST DATA-----------'])
            writer.writerow(['TIME (s)', 'ANGLE_POT', 'ANGLE_IMU', 'LOAD_X', 'LOAD_Y'])
            datasets = ts.get_datasets()
            for ds in datasets:
                writer.writerow([ds.timestamp, ds.pot_angle, ds.imu_angle, ds.x_load, ds.y_load])


        csvFile.close()

    def on_leave(self):
        RLB = self.ids['RootLodgeButton']
        RLB.background_color = (0,0,0,1)
        self.graph1.remove_plot(self.plot1)
        self.graph1._clear_buffer()
        self.graph2.remove_plot(self.plot2)
        self.graph2._clear_buffer()
