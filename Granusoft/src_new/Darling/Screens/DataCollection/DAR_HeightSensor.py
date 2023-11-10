import os
from kivy.lang import Builder
import Darling.configurator as config
from util.BaseScreen import BaseScreen
from util.getKVPath import getKVPath
import os

Builder.load_file(getKVPath(os.getcwd(), __file__))

class DAR_HeightSensor(BaseScreen):
    def use_height_sensor_yes(self):
        config.set('height_sensor',"ON")

    def use_height_sensor_no(self):
        config.set('height_sensor',"OFF")