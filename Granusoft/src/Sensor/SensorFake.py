import datetime
from math import sin

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
        self.pot_fake = 0
        self.imu_fake = 0

    def get_header_data(self):
        self.sensor_data["Temperature"] = "5"
        self.sensor_data["Humidity"] = "5"
        self.sensor_data["Location"] = "5"

    def get_sensor_data(self):
        self.time = datetime.datetime.now().strftime("%I:%M:%S %p")
        self.temp_fake += 1
        self.hum_fake += 2
        self.loc_fake[0] += 0.0000003
        self.loc_fake[1] += 0.0000005
        self.x_fake = 800 + 400 * sin(self.temp_fake / 500) + 0.02 * self.temp_fake
        self.y_fake += .5
        self.pot_fake = 400 + 200 * sin(self.temp_fake / 100) + 0.01 * self.temp_fake
        self.imu_fake += 4.5
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
