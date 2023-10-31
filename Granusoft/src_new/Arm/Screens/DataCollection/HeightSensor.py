import os
from kivy.lang import Builder
import Arm.Settings.configurator as config
from util.BaseScreen import BaseScreen
from util.getKVPath import getKVPath

Builder.load_file(getKVPath(os.getcwd(), __file__))

class HeightSensor(BaseScreen):
    def use_height_sensor_yes(self):
        config.set('height_sensor',"ON")

    def use_height_sensor_no(self):
        config.set('height_sensor',"OFF")