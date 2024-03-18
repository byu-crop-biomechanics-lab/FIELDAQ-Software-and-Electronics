"""
Four buttons to select from: Back, Exit, Restart, and Shut Down
"""

from kivy.lang import Builder
import os
from util.BaseScreen import BaseScreen
from util.getKVPath import getKVPath

Builder.load_file(getKVPath(os.getcwd(), __file__))

class ROD_ExitScreen(BaseScreen):
    def shutD(self):
        os.system("sudo shutdown now")
        #pass

    def restart_OS(self):
        os.system("reboot")
