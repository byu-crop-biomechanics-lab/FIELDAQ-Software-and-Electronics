import datetime

class Dataset:

    def __init__(self, timestamp, strain8, whiskerFront, whiskerBack):
        self.timestamp = timestamp
        self.strain8 = strain8
        self.whiskerFront = whiskerFront
        self.whiskerBack  = whiskerBack
