import os
from kivy.lang import Builder
import Devices.Darling.configurator as config
from util.BaseScreen import BaseScreen
from kivy.uix.screenmanager import ScreenManager, Screen
from util.getKVPath import getKVPath
import os
from util.TestLog import TestLog

Builder.load_file(getKVPath(os.getcwd(), __file__))

class DAR_BarcodeConfirmation(BaseScreen):

    def on_enter(self):
        
        log=TestLog()
        log.connection("Entered DAR_BarcodeConfirmation")

    def use_barcode_yes(self):
        config.set('barcode_scan',"ON")

    def use_barcode_no(self):
        config.set('barcode_scan',"OFF")