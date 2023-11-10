# TODO: No proper calibration routine for the IMU currently exists. However it doesn't
# really need one as the angle will always be accurate, only the 0 location needs adjusting.

from .connections import *
from math import acos, floor, degrees
import configurator as config

class IMU:

    def __init__(self):
        self.config_data = config.get('sensors', {})
        try:
            self.offset = self.config_data['IMU Angle']['offset']
        except:
            self.offset = 0

    def get_data(self, raw_out = 0):
        y_raw, z_raw, x_raw = [value / adafruit_lis3dh.STANDARD_GRAVITY for value in \
                    lis3dh.acceleration]
        # X points directly out the back, opposite of the screen
        # Y points directly left of the box
        # Z points directly down, aligned with the gland connectors and towards the user

        # Ensures acos() doesn't throw an error when z_raw exceeds +-1 (i.e. the box is bumped)
        if z_raw > 1.0:
            z_raw = 1.0
        elif z_raw < -1.0:
            z_raw = -1.0

        angle = degrees(acos(z_raw))

        # Flips angle from 0-180 to 180-360 when passing a vertical z-axis
        if x_raw < 0:
            angle = 360.0 - angle

        # Wraps angle so it stays in -180 to 180 deg range
        angle -= 360.0 * floor((angle + 180.0) * (1 / 360))

        if raw_out == 1:
            return angle
        else:
            angle -= self.offset
            return angle
