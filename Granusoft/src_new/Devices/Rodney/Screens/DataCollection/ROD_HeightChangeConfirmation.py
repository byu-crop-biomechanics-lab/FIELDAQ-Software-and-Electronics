from kivy.lang import Builder
from kivy.properties import StringProperty
from kivy.properties import ObjectProperty
from util.BaseScreen import BaseScreen
from Devices.Rodney.Sensors import Sensor
from kivy.uix.popup import Popup
from Devices.Rodney.Settings.configurator import SettingsSingleton as settings
from util.elements import *
from util.getKVPath import getKVPath
import os

Builder.load_file(getKVPath(os.getcwd(), __file__))

class ROD_HeightChangeConfirmDialog(Popup):
    cancel = ObjectProperty(None)
    proceed = ObjectProperty(None)


class ROD_HeightChangeConfirmation(BaseScreen):

    sensor = Sensor()
    load_cell_height = StringProperty("N/A")

    def on_pre_enter(self):
        self.load_cell_height = self.get_load_cell_sensor_height()
        self.check_height_change()
        self.config = settings()

    def save_new_height(self):
        self._popup.dismiss()
        
        self.config.set('height', float(self.load_cell_height))
        super(ROD_HeightChangeConfirmation, self).move_to('test_in_progress_screen')

    def check_height_change(self):
        current_height = float(self.config.get('height', 0))
        difference = 2.5
        new_height = float(self.load_cell_height) 
        if new_height > current_height + difference or new_height < current_height - difference:
            self.height_change_popup()
        else:
             self.config.set('height', float(self.load_cell_height))
             super(ROD_HeightChangeConfirmation, self).move_to('test_in_progress_screen')



    def height_change_popup(self):
        self._popup = ROD_HeightChangeConfirmDialog(cancel=self.dismiss_popup, proceed=self.save_new_height)
        self._popup.open()

    def dismiss_popup(self):
        self._popup.dismiss()
        super(ROD_HeightChangeConfirmation, self).move_to('testing_screen_auto')

    def get_load_cell_sensor_height(self):
        sensor_data = self.sensor.get_sensor_data(0)
        return str("%.2f" % sensor_data["Load Cell Height"])