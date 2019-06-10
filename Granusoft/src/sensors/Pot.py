from .connections import *

class Pot:

    def __init__(self):
        self.pot = 0.0

    def get_data(self):
        try:
            self.pot = POT_CHAN.value
            return self.pot
        except:
            return self.pot
