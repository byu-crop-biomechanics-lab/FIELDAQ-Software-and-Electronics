from kivy.lang import Builder

import configurator as config
from view.BaseScreen import BaseScreen
from view.input.StrInput import StrInput

Builder.load_file('view/screens/settings/CalibratePointsScreen.kv')

class CalibratePointScreen(BaseScreen):
    def on_pre_enter(self):
        adc_input = self.ids['adc']
        adc_input.text = ''
        real_input = self.ids['real']
        real_input.text = ''

    def on_enter(self):
        """Once the Screen loads, focus the Texinputnput"""
        input = self.ids['real']
        input.focus = True

    def add(self):
        adc_input = self.ids['adc']
        real_input = self.ids['real']
        if adc_input.validate() and real_input.validate():
            calib_screen = self.manager.get_screen('calibrate_screen')
            calib_screen.add_point(float(adc_input.text), float(real_input.text))
            return True
        else:
            return False
