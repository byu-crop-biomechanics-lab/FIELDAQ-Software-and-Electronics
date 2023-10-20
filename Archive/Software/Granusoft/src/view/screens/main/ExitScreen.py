"""
Four buttons to select from: Back, Exit, Restart, and Shut Down
"""

from kivy.lang import Builder
import os
from view.BaseScreen import BaseScreen

Builder.load_file('view/screens/main/ExitScreen.kv')

class ExitScreen(BaseScreen):
    def shutD(self):
        os.system("sudo shutdown now")
        #pass

    def restart_OS(self):
        os.system("reboot")
