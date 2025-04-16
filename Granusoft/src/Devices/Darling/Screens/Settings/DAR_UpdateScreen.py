from kivy.lang import Builder
from util.TestLog import TestLog
from util.BaseScreen import BaseScreen
from util.getKVPath import getKVPath
import os

Builder.load_file(getKVPath(os.getcwd(), __file__))

class DAR_UpdateScreen(BaseScreen):
    def on_enter(self):
        
        log=TestLog()
        log.connection("Entered DAR_UpdateScreen")
    pass
