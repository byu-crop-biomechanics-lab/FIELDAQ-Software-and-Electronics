import os
from kivy.lang import Builder
import Darling.configurator as config
from util.BaseScreen import BaseScreen
from kivy.uix.screenmanager import ScreenManager, Screen
from util.getKVPath import getKVPath
import os

Builder.load_file(getKVPath(os.getcwd(), __file__))

class DAR_BarcodeConfirmation(BaseScreen):
    def use_barcode_yes(self):
        config.set('barcode_scan',"ON")

    def use_barcode_no(self):
        config.set('barcode_scan',"OFF")