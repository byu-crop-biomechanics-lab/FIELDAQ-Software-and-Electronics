import datetime
from math import sin
import math

class Sensor:

    def __init__(self):
        self.REAL_DATA = False
        self.keys = ["Temperature","Humidity","Location","Time","X Load","Y Load","Pot Angle","IMU Angle"]
        self.time = datetime.datetime.now().strftime("%I:%M:%S %p")
        self.sensor_data = {}
        self.cpu_time = 0
        self.temp_fake = 0
        self.hum_fake = 0
        self.loc_fake = [40.2463, -111.6475]
        self.x_fake = 0
        self.y_fake = 0
        self.pot_fake = 22.5
        self.imu_fake = 21.9
        self.elapsed_time = 20

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
        self.y_fake = float("nan")
        self.pot_fake = 90 + math.fabs(90 - math.fmod(2*(self.elapsed_time - 90/2),2*90))
        self.imu_fake = 90 + math.fabs(90 - math.fmod(2*(self.elapsed_time - 90/2.1),2*90))
        if self.pot_fake <= 180:
            self.x_fake = 16 * math.asin((self.pot_fake - 90)/90)
        else:
            self.x_fake = 23
        self.elapsed_time += 0.1
        self.sensor_data["Time"] = self.time
        self.sensor_data["Temperature"] = self.temp_fake
        self.sensor_data["Humidity"] = self.hum_fake
        self.sensor_data["Location"] = self.loc_fake
        self.sensor_data["X Load"] = self.x_fake
        self.sensor_data["Y Load"] = self.y_fake
        self.sensor_data["Pot Angle"] = self.pot_fake
        self.sensor_data["IMU Angle"] = self.imu_fake
        return self.sensor_data

    def clear_gps_memory(self):
        pass
        # print('Clear GPS memory')

    def get_sensor_keys(self):
        return self.keys
