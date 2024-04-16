#from sensors.Temperature import Temperature
# from sensors.Humidity import Humidity
from Devices.Rodney.Sensors.Location import Location
from Devices.Rodney.Sensors.Pot import Pot
from Devices.Rodney.Sensors.IMU import IMU
from Devices.Rodney.Sensors.Height import HeightPoT
from Devices.Rodney.Sensors.Strain8 import Strain8
from Devices.Rodney.Sensors.WhiskerFront import WhiskerFront
from Devices.Rodney.Sensors.WhiskerBack import WhiskerBack
import datetime
import board
import busio
import adafruit_ads1x15.ads1015 as ADS
from adafruit_ads1x15.analog_in import AnalogIn

class Sensor:

    def __init__(self):
        self.REAL_DATA = True
        self.keys = ["Temperature","Humidity","Location","Time","strain8","WhiskerFront","WhiskerBack", "IMU Angle", "Load Cell Height"]
        self.temp = 0.0 #Temperature()
        self.hum = 0.0 #Humidity()
        self.location = Location()
        self.strain8 = Strain8()
        self.WhiskerFront =  WhiskerFront()
        self.WhiskerBack =  WhiskerBack()
        self.imu_angle = IMU()
        self.load_cell_height = HeightPoT()
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
        self.sensor_data["Location"] = self.location.get_data()

    def get_sensor_data(self, adc_out = 0):
        self.sensor_data["strain8"] = self.strain8.read_gauges()
        self.sensor_data["WhiskerFront"] = round(self.WhiskerFront.get_data(adc_out), 4)
        # self.sensor_data["WhiskerBack"] = round(self.WhiskerBack.get_data(adc_out), 4)
        self.sensor_data['WhiskerBack'] = int(0)
        # self.sensor_data["IMU Angle"] = round(self.imu_angle.get_data(adc_out),3)
        # self.sensor_data["Load Cell Height"] = round(self.load_cell_height.get_data(adc_out),2)
        self.sensor_data["IMU Angle"] = 0
        self.sensor_data["Load Cell Height"] = 0
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
