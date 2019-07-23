from .connections import *

class IMU:

    def __init__(self):
        pass

    def get_data(self):
        x, y, z = [value / adafruit_lis3dh.STANDARD_GRAVITY for value in \
                    lis3dh.acceleration]
        # return "x = {0:0.3f} G \n y = {1:0.3f} G \n z = {2:0.3f} G".format(x, y, z)
        return x
