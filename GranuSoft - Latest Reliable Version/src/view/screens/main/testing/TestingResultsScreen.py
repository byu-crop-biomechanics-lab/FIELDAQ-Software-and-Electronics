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
    y_max = NumericProperty(1)
    x_major = NumericProperty(1)
    y_major = NumericProperty(1)
    datasets = []

    def __init__(self, **kwargs):
        '''Creates Kivy Buttons to be able to dynamically change the sidebar actions
        based on interaction with the lists.'''
        super(BaseScreen, self).__init__(**kwargs)

        self.stalkLodge_button = GranuNoteButton(text = 'Stalk\nLodge')
        '''self.stalkLodge_button.bind(on_release = self.save)'''
        self.rootLodge_button = GranuNoteButton(text = 'Root\nLodge')
        '''self.rootLodge_button.bind(on_release = self.new)'''
        self.wetSoil_button = GranuNoteButton(text = 'Wet\nSoil')
        '''self.wetSoil_button.bind(on_release = self.remove)'''
        self.postNote_button = GranuNoteButton(text = 'Add Post-\nTest Note')
        '''self.postNote_button.bind(on_release = root(BaseScreen, root).move_to('note_screen'))'''

    # Button Changes

    def default_buttons(self):
        buttons = self.ids['postTest_buttons']
        buttons.clear_widgets()
        buttons.add_widget(self.stalkLodge_button)
        buttons.add_widget(self.rootLodge_button)
        buttons.add_widget(self.wetSoil_button)
        buttons.add_widget(self.postNote_button)

    def find_max_x_load(self):
        max = 0
        for dataset in self.datasets:
            if(dataset.x_load > max):
                max = dataset.x_load
        return max

    def on_enter(self):
        self.graph = self.ids['graph_test']
        self.plot = MeshLinePlot(color=[1, 1, 1, 1])
        ts = TestSingleton()
        self.datasets = ts.get_datasets()
        last_index = len(self.datasets) - 1

        # Add buttons
        self.default_buttons

        self.x_max = math.ceil(self.datasets[last_index].timestamp / 5) * 5
        #self.y_max = math.ceil(self.find_max_x_load() / 10000) * 10000
        self.y_max = 2000
        self.x_major = int(self.x_max/5)
        self.y_major = int(self.y_max/5)

        self.plot.points = [(self.datasets[i].timestamp, self.datasets[i].pot_angle) for i in range(0, len(self.datasets))]
        #for i in range(0,len(self.datasets)):
        #    print("Time:",self.datasets[i].timestamp," -- X_Load:", self.datasets[i].x_load)

        self.graph.add_plot(self.plot)

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

        with open(filename, 'w+', newline='') as csvFile:
            writer = csv.writer(csvFile)
            writer.writerow(['----------META DATA----------'])
            writer.writerow(['SOFTWARE VERSION', '2.0.0'])
            writer.writerow(['DEVICE OPERATOR', str(config.get('operator', 0))])
            writer.writerow(['----------TEST ATTRIBUTES----------'])
            writer.writerow(['FIELD', 'VALUE', 'UNIT'])
            writer.writerow(['YEAR', dt.strftime("%Y")])
            writer.writerow(['MONTH', dt.strftime("%m")])
            writer.writerow(['DAY', dt.strftime("%d")])
            writer.writerow(['TIME', dt.strftime("%H:%M:%S"), 'Local Time Zone'])
            writer.writerow(['PLOT', str(config.get('plot_num', 0)), '#'])
            writer.writerow(['HEIGHT', str(config.get('height', 0)), 'cm'])
            writer.writerow(['TEMPERATURE', '40', 'C'])
            writer.writerow(['HUMIDITY', '40', '%'])
            writer.writerow(['LATITUDE', '40', 'angular degrees'])
            writer.writerow(['LONGITUDE', '40', 'angular degrees'])
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


        self.graph.remove_plot(self.plot)
        self.graph._clear_buffer()
