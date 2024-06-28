import os
from kivy.lang import Builder
import Devices.Darling.configurator as config
from util.BaseScreen import BaseScreen
from util.getKVPath import getKVPath
import os
from util.TestLog import TestLog

Builder.load_file(getKVPath(os.getcwd(), __file__))

class DAR_HeightSensor(BaseScreen):

    def on_enter(self):    
        log=TestLog()
        log.connection("Entered DAR_HeightSensor")

    def use_height_sensor_yes(self):
        config.set('height_sensor',"ON")

    def use_height_sensor_no(self):
        config.set('height_sensor',"OFF")