"""
Shows all data: Temperature, Humidity, Location, Time, and all Sensor data
"""

from kivy.lang import Builder
from kivy.properties import NumericProperty
from kivy.properties import StringProperty
from kivy.properties import ListProperty
from kivy.clock import Clock
from Sensor import Sensor
import datetime

from view.BaseScreen import BaseScreen
from view.elements import *


Builder.load_file('view/screens/main/LiveFeedScreen.kv')

INTERVAL = .004
SECOND_CAP = 1/INTERVAL

class LiveFeedScreen(BaseScreen):
    sensor = Sensor()

    run_count = 0
    transition_to_state = StringProperty("Pause")

    #temperature_label = StringProperty("Temperature")
    humidity_label = StringProperty("Humidity")
    location_label = StringProperty("Location")
    time_label = StringProperty("Time")
    x_load_label = StringProperty("X Load")
    y_load_label = StringProperty("Y Load")
    pot_angle_label = StringProperty("Pot Angle")
    imu_angle_label = StringProperty("IMU Angle")
    data_rate_label = StringProperty("Data Rate")
    load_cell_height_label = StringProperty("Load Cell Height")
    current_date_label = StringProperty("Date")

    #temperature = StringProperty("0")
    humidity = StringProperty("0")
    location = StringProperty("0.00, 0.00")
    time = StringProperty("00:00:00 AM")
    x_load = StringProperty("0.00")
    y_load = StringProperty("0.00")
    pot_angle = StringProperty("0")
    imu_angle = StringProperty("0")
    data_rate = StringProperty("0")
    current_date = StringProperty("01/01/2000")
    load_cell_height = StringProperty("0.00")

    old_time = 0
    xUnits = " lbs"
    potUnits = u'\N{DEGREE SIGN}'
    imuUnits = u'\N{DEGREE SIGN}'
    loadCellHeightUnits = 'cm'


    def on_pre_enter(self):
        self.event = Clock.schedule_interval(self.update_values, INTERVAL)
        self.transition_to_state = "Pause"
        self.sensor.clear_gps_memory()
        self.ids['adc_button_text'].text = 'ADC\nValues'
        self.adc_out = 0

    def update_values(self, obj):

        if self.run_count >= SECOND_CAP:
            self.sensor.get_header_data()
            sensor_data = self.sensor.get_sensor_data(self.adc_out)
            #self.temperature = str("%.1f" % sensor_data["Temperature"])
            #self.humidity = str("%.1f" % sensor_data["Humidity"])
            self.location = ('(' + str("%.3f" % sensor_data["Location"][0]) + ', ' + str("%.3f" % sensor_data["Location"][1]) + ')')
            self.time = datetime.datetime.now().strftime("%H:%M:%S %p")
            self.current_date = datetime.date.today().strftime("%d/%m/%Y")
            self.y_load = str("%.1f" % sensor_data["Y Load"])
            if self.adc_out == 0:
                self.x_load = str("%.3f" % sensor_data["X Load"])
                self.pot_angle = str("%.3f" % sensor_data["Pot Angle"])
            else:
                self.x_load = str("%.0f" % sensor_data["X Load"])
                self.pot_angle = str("%.0f" % sensor_data["Pot Angle"])
            self.imu_angle = str("%.3f" % sensor_data["IMU Angle"])
            self.load_cell_height = str("%.2f" % sensor_data["Load Cell Height"])
            # Calculate Data Acquisition Rate
            now = datetime.datetime.now()
            new_time = (int(now.strftime("%M")) * 60) + int(now.strftime("%S")) + (int(now.strftime("%f"))/1000000)
            time_dif = new_time - self.old_time
            self.data_rate = str("%.0f" % round(SECOND_CAP/time_dif,2))
            self.old_time = new_time
            # Reset run_count
            self.run_count = 0
        else:
            sensor_data = self.sensor.get_sensor_data()
            self.run_count = self.run_count + 1

    def adc_button_press(self):
        adcButton = self.ids['adc_button_text']
        if self.adc_out == 0:
            self.adc_out = 1
            adcButton.text = 'Real\nUnits'
            self.xUnits = ""
            self.potUnits = ""
            self.imuUnits = u'\N{DEGREE SIGN}'
        else:
            self.adc_out = 0
            adcButton.text = 'ADC\nValues'
            self.xUnits = " lbs"
            self.potUnits = u'\N{DEGREE SIGN}'
            self.imuUnits = u'\N{DEGREE SIGN}'

    def on_leave(self):
        self.event.cancel()

    def transition(self):
        if(self.transition_to_state == "Pause"):
            self.event.cancel()
            self.transition_to_state = "Resume"
        else:
            self.event = Clock.schedule_interval(self.update_values, INTERVAL)
            self.transition_to_state = "Pause"
