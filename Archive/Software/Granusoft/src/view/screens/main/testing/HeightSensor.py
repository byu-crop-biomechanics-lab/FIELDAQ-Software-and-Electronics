import os
from kivy.lang import Builder
import configurator as config
from view.BaseScreen import BaseScreen

Builder.load_file('view/screens/main/testing/HeightSensor.kv')

class HeightSensor(BaseScreen):
    def use_height_sensor_yes(self):
        config.set('height_sensor',"ON")

    def use_height_sensor_no(self):
        config.set('height_sensor',"OFF")