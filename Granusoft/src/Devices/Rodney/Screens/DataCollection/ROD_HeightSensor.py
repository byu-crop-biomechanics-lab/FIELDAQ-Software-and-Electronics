import os
from kivy.lang import Builder
from Devices.Rodney.Settings.configurator import SettingsSingleton as settings
from util.BaseScreen import BaseScreen
from util.getKVPath import getKVPath
from util.TestLog import TestLog
Builder.load_file(getKVPath(os.getcwd(), __file__))

class ROD_HeightSensor(BaseScreen):
    config = settings()
    def on_enter(self):
        
        log = TestLog()
        log.connection("Entering ROD_HeightScreen")

    def use_height_sensor_yes(self):
        self.config.set('height_sensor',"ON")

    def use_height_sensor_no(self):
        self.config.set('height_sensor',"OFF")