"""
Four buttons to select from: Back, Exit, Restart, and Shut Down
"""

from kivy.lang import Builder

from view.BaseScreen import BaseScreen

Builder.load_file('view/screens/main/ExitScreen.kv')

class ExitScreen(BaseScreen):
    pass
