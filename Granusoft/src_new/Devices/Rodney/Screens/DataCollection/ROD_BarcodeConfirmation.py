import os
from kivy.lang import Builder
from Devices.Rodney.Settings.configurator import SettingsSingleton as settings
from kivy.uix.screenmanager import ScreenManager, Screen
from util.BaseScreen import BaseScreen
from util.getKVPath import getKVPath

Builder.load_file(getKVPath(os.getcwd(), __file__))

class ROD_BarcodeConfirmation(BaseScreen):
    def use_barcode_yes(self):
        self.config.set('barcode_scan',"ON")

    def use_barcode_no(self):
        self.config.set('barcode_scan',"OFF")