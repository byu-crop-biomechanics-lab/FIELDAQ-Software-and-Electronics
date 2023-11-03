from kivy.lang import Builder
from kivy.properties import StringProperty
from kivy.properties import ObjectProperty
from view.BaseScreen import BaseScreen
from Sensor import Sensor
from kivy.uix.popup import Popup
import configurator as config
from view.elements import *

Builder.load_file('view/screens/main/testing/HeightChangeConfirmation.kv')

class HeightChangeConfirmDialog(Popup):
    cancel = ObjectProperty(None)
    proceed = ObjectProperty(None)


class HeightChangeConfirmation(BaseScreen):

    sensor = Sensor()
    load_cell_height = StringProperty("N/A")

    def on_pre_enter(self):
        self.load_cell_height = self.get_load_cell_sensor_height()
        self.check_height_change()

    def save_new_height(self):
        self._popup.dismiss()
        config.set('height', float(self.load_cell_height))
        super(HeightChangeConfirmation, self).move_to('test_in_progress_screen')

    def check_height_change(self):
        current_height = float(config.get('height', 0))
        difference = 2.5
        new_height = float(self.load_cell_height) 
        if new_height > current_height + difference or new_height < current_height - difference:
            self.height_change_popup()
        else:
             config.set('height', float(self.load_cell_height))
             super(HeightChangeConfirmation, self).move_to('test_in_progress_screen')



    def height_change_popup(self):
        self._popup = HeightChangeConfirmDialog(cancel=self.dismiss_popup, proceed=self.save_new_height)
        self._popup.open()

    def dismiss_popup(self):
        self._popup.dismiss()
        super(HeightChangeConfirmation, self).move_to('testing_screen_auto')

    def get_load_cell_sensor_height(self):
        sensor_data = self.sensor.get_sensor_data(0)
        return str("%.2f" % sensor_data["Load Cell Height"])