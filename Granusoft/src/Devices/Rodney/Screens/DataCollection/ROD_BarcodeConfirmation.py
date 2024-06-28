import os
from kivy.lang import Builder
from Devices.Rodney.Settings.configurator import SettingsSingleton as settings
from kivy.uix.screenmanager import ScreenManager, Screen
from util.BaseScreen import BaseScreen
from util.getKVPath import getKVPath
from util.TestLog import TestLog
Builder.load_file(getKVPath(os.getcwd(), __file__))

class ROD_BarcodeConfirmation(BaseScreen):
    config = settings()
    def use_barcode_yes(self):
        self.config.set('barcode_scan',"ON")

    def on_enter(self):
        
        log = TestLog()
        log.connection("Entering ROD_BarcodeConfirmation")

    def use_barcode_no(self):
        self.config.set('barcode_scan',"OFF")