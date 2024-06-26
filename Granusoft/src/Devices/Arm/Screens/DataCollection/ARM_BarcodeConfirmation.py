import os
from kivy.lang import Builder
import Devices.Arm.Settings.configurator as config
from kivy.uix.screenmanager import ScreenManager, Screen
from util.BaseScreen import BaseScreen
from util.getKVPath import getKVPath

Builder.load_file(getKVPath(os.getcwd(), __file__))

class ARM_BarcodeConfirmation(BaseScreen):
    def use_barcode_yes(self):
        config.set('barcode_scan',"ON")

    def use_barcode_no(self):
        config.set('barcode_scan',"OFF")