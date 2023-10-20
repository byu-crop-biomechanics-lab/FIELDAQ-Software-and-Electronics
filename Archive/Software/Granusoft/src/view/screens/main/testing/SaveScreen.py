import os, stat
from os import mkdir, listdir
from os.path import isfile, join
from shutil import copy, rmtree
from re import TEMPLATE
from kivy.lang import Builder
from Sensor import Sensor
import datetime
from TestSingleton import TestSingleton

from view.BaseScreen import BaseScreen
from kivy.properties import StringProperty
from view.elements import *
import configurator as config
import csv
try:
    from sensors.connections import *
except:
    pass

from getmac import get_mac_address as gma

Builder.load_file('view/screens/main/testing/SaveScreen.kv')

TEMP_FOLDER = 'Tests/temp'

class SaveScreen(BaseScreen):
    use_height_sensor = config.get('height_sensor', 0)

    def on_pre_enter(self):
        """Prior to the screen loading, check if barcode needs to be scanned"""
        use_barcode = config.get('barcode_scan', "OFF")
        barcode = self.ids['barcode']
        barcode.text = ""
        self.check_height_sensor_status()

        if use_barcode == "OFF":
            self.save_test()
            self.check_height_sensor_status()
            super(SaveScreen, self).move_to(self.next_screen)

    def on_enter(self):
        """Once the Screen loads, focus the TextInput"""
        barcode = self.ids['barcode']
        barcode.focus = True

    def current_time(self):
            return datetime.datetime.now().strftime("%H:%M:%S")

    def save_test(self):
        """Save all test data to csv file"""
        barcode = self.ids['barcode']

        ts = TestSingleton()
        self.datasets = ts.get_datasets()
        ts.set_break_height(str(config.get('break_height', 0)))

        # Prepare the notes
        notes = config.get('notes', {
            "pretest": [],
            "bank": []
        })
        pre_notes = notes["pretest"]
        post_notes = ts.get_post_notes()
        dt = datetime.datetime.now()


        # Sets the filename to save the csv file as
        folder_name = 'Tests/'+str(config.get('folder', 0))

        try:
            os.mkdir(folder_name)
        except:
            if os.access(folder_name,os.W_OK) and os.access(folder_name,os.X_OK):
                pass
            else:
                folder_name = self.create_duplicate_folder(folder_name)            

        #get mac address
        mac_address = gma()

        #try:
        config.set('curr_test_num', (config.get('curr_test_num', 0) + 1))
        filename = folder_name+'/' + dt.strftime('%Y_%m_%d_%H_%M_%S') + '_P' + str(config.get('plot_num', 0)) \
        + '_T' + str(config.get('curr_test_num', 0)).zfill(2) + '.csv'
            
        try:
            gps.update()
        except:
            pass
        sensor = Sensor()
        sensor.get_header_data()
        sensor_data = sensor.get_sensor_data()
        location = [str("%.7f" % sensor_data["Location"][0]),
                    str("%.7f" % sensor_data["Location"][1])]

        self.config_data = config.get('sensors', {})
        self.NAMES = ['X Load', 'Y Load', 'IMU Angle', 'Pot Angle', 'Temperature', 'Humidity']
        self.SENSOR = ['LOAD_X', 'LOAD_Y', 'IMU', 'POT','TEMP','HUM']
        self.UNITS = ['Pounds', 'Pounds', 'Deg', 'Deg','C','%']
        self.IDS = ['loadx1', 'loady1', 'imu1', 'pot1','temp1','hum1']

        with open(filename, 'w+', newline='') as csvFile:
            writer = csv.writer(csvFile)
            writer.writerow(['----------META DATA----------'])
            writer.writerow(['SOFTWARE VERSION', '2.3.0','DEVICE MAC ADDRESS',mac_address])
            writer.writerow(
                ['DEVICE OPERATOR', str(config.get('operator', 0))])
            writer.writerow(['----------TEST ATTRIBUTES----------'])
            writer.writerow(['FIELD', 'VALUE', 'UNIT'])
            writer.writerow(['YEAR', dt.strftime("%Y")])
            writer.writerow(['MONTH', dt.strftime("%m")])
            writer.writerow(['DAY', dt.strftime("%d")])
            writer.writerow(
                ['TIME', self.current_time(), config.get('timezone',0)])
            writer.writerow(['PLOT', str(config.get('plot_num', 0)), '#'])
            writer.writerow(['HEIGHT', str(config.get('height', 0)), 'cm'])
            writer.writerow(['BARCODE', str(barcode.text)])
            writer.writerow(['TEMPERATURE', 'N/A', 'C'])
            writer.writerow(['HUMIDITY', 'N/A', '%'])
            writer.writerow(['LATITUDE', location[0], 'angular degrees'])
            writer.writerow(['LONGITUDE', location[1], 'angular degrees'])
            writer.writerow(['----------OPTIONAL DATA----------'])
            for i in range(5):
                try:
                    writer.writerow(
                        ['PRE_TEST_NOTE_' + str(i+1), pre_notes[i]])
                except:
                    writer.writerow(['PRE_TEST_NOTE_' + str(i+1), ''])
            for i in range(5):
                try:
                    writer.writerow(
                        ['POST_TEST_NOTE_' + str(i+1), post_notes[i]])
                except:
                    writer.writerow(['POST_TEST_NOTE_' + str(i+1), ''])
            writer.writerow(['BREAK_HEIGHT', str(
                config.get('break_height', 0)), 'cm'])
            writer.writerow(['LCA_WEIGTH', '0', 'g'])
            writer.writerow(
                ['----------SENSOR CALIBRATION DATA (stored_value*A + B = raw_data)------'])
            writer.writerow(['SENSOR', 'A', 'B', 'UNIT', 'ID'])
            for j in range(len(self.NAMES)):
                try:
                    writer.writerow([self.SENSOR[j], self.config_data[self.NAMES[j]]['slope'],
                                    self.config_data[self.NAMES[j]]['intercept'], self.UNITS[j], self.IDS[j]])
                except:
                    writer.writerow([self.SENSOR[j], '1', '0',
                                    self.UNITS[j], self.IDS[j]])
            writer.writerow(['----------TEST DATA-----------'])
            writer.writerow(['TIME (milliseconds)', 'ANGLE_POT',
                            'ANGLE_IMU', 'LOAD_X', 'LOAD_Y'])
            datasets = ts.get_datasets()
            for ds in datasets:
                writer.writerow(
                    [(ds.timestamp * 1000), ds.pot_angle, ds.imu_angle, ds.x_load, ds.y_load])

        csvFile.close()

    def check_height_sensor_status(self):
        if str(config.get('height_sensor', 0)) == "ON":
            self.next_screen = 'testing_screen_auto'
        else:
            self.next_screen = 'testing_screen'

    def create_duplicate_folder(self,foldername):
        os.mkdir(TEMP_FOLDER)
        files = [f for f in listdir(foldername) if isfile(join(foldername, f))]
        for f in files:
            copy(foldername+'/'+f, TEMP_FOLDER)
        os.rename(TEMP_FOLDER, foldername+'2')
        os.system('sudo rm -r '+foldername)
        os.rename(foldername+'2', foldername)
        return foldername