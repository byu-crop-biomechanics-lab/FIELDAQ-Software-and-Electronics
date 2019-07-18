from sensors.Temperature import Temperature
from sensors.Humidity import Humidity
from sensors.Location import Location
from sensors.X_Load import X_Load
from sensors.Y_Load import Y_Load
from sensors.Pot import Pot
from sensors.IMU import IMU
import datetime
import board
import busio
import adafruit_ads1x15.ads1015 as ADS
from adafruit_ads1x15.analog_in import AnalogIn

class Sensor:

    def __init__(self):
        self.REAL_DATA = True
        self.keys = ["Temperature","Humidity","Location","Time","X Load","Y Load","Pot Angle","IMU Angle"]
        self.temp = Temperature()
        self.hum = Humidity()
        self.location = Location()
        self.x_load = X_Load()
        self.y_load = Y_Load()
        self.pot_angle = Pot()
        self.imu_angle = IMU()
        self.time = datetime.datetime.now().strftime("%I:%M:%S %p")
        self.sensor_data = {}
        self.cpu_time = 0
        self.temp_fake = 0
        self.hum_fake = 0
        self.loc_fake = 0
        self.x_fake = 0
        self.y_fake = 0
        self.pot_fake = 0
        self.imu_fake = 0

    def get_header_data(self):
        self.sensor_data["Temperature"] = self.temp.get_data()
        self.sensor_data["Humidity"] = self.hum.get_data()
        self.sensor_data["Location"] = self.location.get_data()

    def get_sensor_data(self):
        self.sensor_data["X Load"] = round(self.x_load.get_data(),4)
        self.sensor_data["Y Load"] = round(self.y_load.get_data(),4)
        self.sensor_data["Pot Angle"] = round(self.pot_angle.get_data(),3)
        self.sensor_data["IMU Angle"] = round(self.imu_angle.get_data(),3)
        return self.sensor_data

    def clear_gps_memory(self):
        self.location.update_gps_location()

    def get_sensor_keys(self):
        return self.keys

if __name__ == "__main__":
    sensor = Sensor()
    print("\n **********Beginning Sensor Test********** \n")
    print("Sensor Data: ")
    data_array = sensor.get_sensor_data()
    for key in sensor.get_sensor_keys():
        print(key, data_array[key])
    print("\n **********Ending Sensor Test********** \n")
