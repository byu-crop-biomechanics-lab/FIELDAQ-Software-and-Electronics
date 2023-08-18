import os
from kivy.lang import Builder
import configurator as config
from view.BaseScreen import BaseScreen
from kivy.uix.screenmanager import ScreenManager, Screen

Builder.load_file('view/screens/main/testing/BarcodeConfirmation.kv')

class BarcodeConfirmation(BaseScreen):
    def use_barcode_yes(self):
        config.set('barcode_scan',"ON")

    def use_barcode_no(self):
        config.set('barcode_scan',"OFF")