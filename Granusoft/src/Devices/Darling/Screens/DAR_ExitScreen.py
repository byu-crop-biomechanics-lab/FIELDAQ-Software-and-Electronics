"""
Four buttons to select from: Back, Exit, Restart, and Shut Down
"""

from kivy.lang import Builder
import os
from util.BaseScreen import BaseScreen
from util.getKVPath import getKVPath
from util.TestLog import TestLog

Builder.load_file(getKVPath(os.getcwd(), __file__))

class DAR_ExitScreen(BaseScreen):
    def shutD(self):
        os.system("sudo shutdown now")

    def restart_OS(self):
        os.system("reboot")

    def on_enter(self):
        log=TestLog()
        log.connection("Entered DAR_ExitScreen")
