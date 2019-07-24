from .connections import *
from math import cos, radians

class IMU:

    def __init__(self):
        pass

    def get_data(self, raw_out = 0):
        x, y, z = [value / adafruit_lis3dh.STANDARD_GRAVITY for value in \
                    lis3dh.acceleration]
        x_raw = x
        # return "x = {0:0.3f} G \n y = {1:0.3f} G \n z = {2:0.3f} G".format(x, y, z)
        if raw_out == 1:
            return x_raw
        else:
            x = 90 * cos(radians(90 * x_raw))
            return x
