from kivy.lang import Builder

from Devices.Rodney.Settings.configurator import SettingsSingleton as settings
from util.BaseScreen import BaseScreen
from util.input.StrInput import StrInput
from Devices.Rodney.Sensors import Sensor
from kivy.properties import StringProperty
from statistics import median
from util.getKVPath import getKVPath
import os

Builder.load_file(getKVPath(os.getcwd(), __file__))

class ROD_CalibratePointScreen(BaseScreen):
    sensor_name = StringProperty()

    def __init__(self, **kwargs):
        super(ROD_CalibratePointScreen, self).__init__(**kwargs)

    def on_pre_enter(self):
        adc_input = self.ids['adc']
        adc_input.text = ''
        real_input = self.ids['real']
        real_input.text = ''
        collectButton = self.ids['collect_button']
        collectButton.text = 'Collect\nADC'
        collectButton.bind(on_release = self.get_adc)

    def on_enter(self):
        """Once the Screen loads, focus the Texinputnput"""
        input = self.ids['real']
        input.focus = True

    def set_sensor(self, name):
        self.sensor_name = name

    def add(self):
        adc_input = self.ids['adc']
        real_input = self.ids['real']
        if adc_input.validate() and real_input.validate():
            calib_screen = self.manager.get_screen('rod_calibrate_screen')
            calib_screen.add_point(float(adc_input.text), float(real_input.text))
            return True
        else:
            return False

    def get_adc(self, obj):
        vals = []
        adc_input = self.ids['adc']
        sensor = Sensor()
        for i in range(100):
            if self.sensor_name=='Load Cell\nHeight':
                self.sensor_name = 'Load Cell Height'
            sensor_data = sensor.get_sensor_data(1)
            vals.append(sensor_data[self.sensor_name])
        med_val = median(vals)
        adc_input.text = str(med_val)
