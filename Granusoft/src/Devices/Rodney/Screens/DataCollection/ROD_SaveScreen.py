from os import mkdir, listdir
from kivy.lang import Builder
from Devices.Rodney.Sensors import Sensor
import datetime
from Devices.Rodney.Data.TestSingleton import TestSingleton

from util.BaseScreen import BaseScreen
from kivy.properties import StringProperty
from util.elements import *
from Devices.Rodney.Settings.configurator import SettingsSingleton as settings
import csv
try:
    from Devices.Rodney.Sensors.connections import *
except:
    pass

from getmac import get_mac_address as gma
from util.getKVPath import getKVPath
import os

#import pytz
#from timezonefinder import TimezoneFinder

Builder.load_file(getKVPath(os.getcwd(), __file__))


class ROD_SaveScreen(BaseScreen):
    config = settings()
    use_height_sensor = config.get('height_sensor', 0)

    def on_pre_enter(self):
        """Prior to the screen loading, check if barcode needs to be scanned"""
        use_barcode = self.config.get('barcode_scan', "OFF")
        barcode = self.ids['barcode']
        barcode.text = ""

        if use_barcode == "OFF":
            self.save_test()
            self.check_height_sensor_status()
            super(ROD_SaveScreen, self).move_to(self.next_screen)

    def on_enter(self):
        """Once the Screen loads, focus the TextInput"""
        barcode = self.ids['barcode']
        barcode.focus = True

    # def find_time_zone(self):
    #     sensor = Sensor()
    #     sensor.get_header_data()
    #     sensor_data = sensor.get_sensor_data()
    #     obj = TimezoneFinder()
    #     return obj.timezone_at(lat = sensor_data["Location"][0], lng = sensor_data["Location"][1])

    def current_time(self):
            # tz = pytz.timezone(self.find_time_zone()) 
            return datetime.datetime.now().strftime("%H:%M:%S")

    def save_test(self):
        """Save all test data to csv file"""
        barcode = self.ids['barcode']

        ts = TestSingleton()
        self.datasets = ts.get_datasets()
        ts.set_break_height(str(self.config.get('break_height', 0)))

        # Prepare the notes
        notes = self.config.get('notes', {
            "pretest": [],
            "bank": []
        })
        pre_notes = notes["pretest"]
        post_notes = ts.get_post_notes()
        dt = datetime.datetime.now()

        # Sets the filename to save the csv file as
        folder_name = 'Tests/'+str(self.config.get('folder', 0))
        import os

        if not os.path.exists('Tests'):
            os.makedirs('Tests', exist_ok=True)

        if not os.path.exists(folder_name):
            os.makedirs(folder_name, exist_ok=True)
            

        #get mac address
        mac_address = gma()

        #try:
        self.config.set('curr_test_num', (self.config.get('curr_test_num', 0) + 1))
        filename = folder_name+'/' + dt.strftime('%Y_%m_%d_%H_%M_%S') + '_P' + str(self.config.get('plot_num', 0)) \
        + '_T' + str(self.config.get('curr_test_num', 0)).zfill(2) + '.csv'
            
        try:
            gps.update()
        except:
            pass
        sensor = Sensor()
        sensor.get_header_data()
        sensor_data = sensor.get_sensor_data()
        location = [str("%.7f" % sensor_data["Location"][0]),
                    str("%.7f" % sensor_data["Location"][1])]

        self.config_data = self.config.get('sensors', {})
        self.NAMES = ['Strain 0', 'Strain 1', 'Strain 2', 'Strain 3', 'Whisker Front', 'Whisker Back']
        self.SENSOR = ['Strain 0', 'Strain 1', 'Strain 2', 'Strain 3', 'Whisker Front', 'Whisker Back']
        self.UNITS = ['V', 'V', 'V', 'V', 'Deg', 'Deg']
        self.IDS = ['Strain 0', 'Strain 1', 'Strain 2', 'Strain 3', 'Whisker Front', 'Whisker Back']

        with open(filename, 'w+', newline='') as csvFile:
            writer = csv.writer(csvFile)
            writer.writerow(['----------META DATA----------'])
            writer.writerow(['SOFTWARE VERSION', '2.3.0','DEVICE MAC ADDRESS',mac_address])
            writer.writerow(
                ['DEVICE OPERATOR', str(self.config.get('operator', 0))])
            writer.writerow(['----------TEST ATTRIBUTES----------'])
            writer.writerow(['FIELD', 'VALUE', 'UNIT'])
            writer.writerow(['YEAR', dt.strftime("%Y")])
            writer.writerow(['MONTH', dt.strftime("%m")])
            writer.writerow(['DAY', dt.strftime("%d")])
            writer.writerow(
                ['TIME', self.current_time(), 'Local Time'])
            writer.writerow(['PLOT', str(self.config.get('plot_num', 0)), '#'])
            writer.writerow(['HEIGHT', str(self.config.get('height', 0)), 'cm'])
            writer.writerow(['BARCODE', str(barcode.text)])
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
                self.config.get('break_height', 0)), 'cm'])
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
            writer.writerow(['TIME (milliseconds)', 'Strain Ax', 'Strain Bx', 'Strain Ay', 'Strain By', 'Whisker Front', 'Whisker Back'])
            datasets = ts.get_datasets()
            for ds in datasets:
                writer.writerow(
                    [f'{(ds.timestamp * 1000):.3f}', ds.strain8['Ax'], ds.strain8['Bx'], ds.strain8['Ay'], ds.strain8['By'], ds.whiskerFront, ds.whiskerBack])

        csvFile.close()


    def check_height_sensor_status(self):
        if str(self.config.get('height_sensor', 0)) == "ON":
            self.next_screen = 'rod_testing_screen_auto'
        else:
            self.next_screen = 'rod_testing_screen'