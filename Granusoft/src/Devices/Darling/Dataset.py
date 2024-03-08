import datetime

class Dataset:

    def __init__(self, timestamp, x_load, y_load, pot_angle, imu_angle, data_rate):
        self.timestamp = timestamp
        self.x_load = x_load
        self.y_load = y_load
        self.pot_angle = pot_angle
        self.imu_angle = imu_angle
        self.data_rate = data_rate
