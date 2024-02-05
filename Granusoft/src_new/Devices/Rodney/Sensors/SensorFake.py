import datetime
from math import sin
import math

class Sensor:

    def __init__(self):
        self.REAL_DATA = False
        self.keys = ["Temperature","Humidity","Location","Time","strain8","whiskers","IMU Angle", "Load Cell Height"]
        self.time = datetime.datetime.now().strftime("%I:%M:%S %p")
        self.sensor_data = {}
        self.cpu_time = 0
        self.temp_fake = 0
        self.hum_fake = 0
        #self.loc_fake = [40.2463, -111.6475]
        self.loc_fake=[24.52485137129533, 54.434341223292826]
        self.strain8_fake = [0.0, 0.0, 0.0, 0.0]
        self.whiskers_fake = [0.0, 0.0]
        self.imu_fake = 21.9
        self.elapsed_time = 20
        self.load_cell_height_fake = 95.5

    def get_header_data(self):
        self.sensor_data["Temperature"] = "5"
        self.sensor_data["Humidity"] = "5"
        self.sensor_data["Location"] = "5"

    def get_sensor_data(self, adc_out = 0):
        self.time = datetime.datetime.now().strftime("%I:%M:%S %p")
        self.temp_fake = float("nan")
        self.hum_fake = float("nan")
        self.loc_fake[0] += 0.00000003
        self.loc_fake[1] += 0.00000005
        self.strain8_fake[0] = 900 + math.fabs(90 - math.fmod(2*(self.elapsed_time - 90/2), 2*90))
        self.strain8_fake[1] = 900 + math.fabs(90 - math.fmod(2*(self.elapsed_time - 90/2), 2*90))
        self.strain8_fake[2] = 900 + math.fabs(90 - math.fmod(2*(self.elapsed_time - 90/2), 2*90))
        self.strain8_fake[3] = 900 + math.fabs(90 - math.fmod(2*(self.elapsed_time - 90/2), 2*90))
        self.whiskers_fake[0] = 9000 + math.fabs(90 - math.fmod(2*(self.elapsed_time - 90/2), 2*90))
        self.whiskers_fake[1] = 9000 + math.fabs(90 - math.fmod(2*(self.elapsed_time - 90/2), 2*90))
        self.imu_fake = 90 + math.fabs(90 - math.fmod(2*(self.elapsed_time - 90/2.1), 2*90))
        self.elapsed_time += 0.1
        self.sensor_data["Time"] = self.time
        self.sensor_data["Temperature"] = self.temp_fake
        self.sensor_data["Humidity"] = self.hum_fake
        self.sensor_data["Location"] = self.loc_fake
        self.sensor_data["strain8"] = self.strain8_fake
        self.sensor_data["whiskers"] = self.whiskers_fake
        self.sensor_data["IMU Angle"] = self.imu_fake
        self.sensor_data["Load Cell Height"] = self.load_cell_height_fake
        return self.sensor_data

    def clear_gps_memory(self):
        pass
        # print('Clear GPS memory')

    def get_sensor_keys(self):
        return self.keys
