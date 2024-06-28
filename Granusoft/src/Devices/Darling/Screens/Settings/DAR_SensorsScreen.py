import os
from kivy.lang import Builder
from kivy.clock import Clock
from kivy.uix.button import Button
from kivy.properties import ObjectProperty
from util.TestLog import TestLog
from util.BaseScreen import BaseScreen
from Devices.Darling.Sensor import Sensor
from util.getKVPath import getKVPath
import os

Builder.load_file(getKVPath(os.getcwd(), __file__))

class DAR_SensorButton(Button):
    def __init__(self, name, parent_screen, calib_screen, **kwargs):
        '''Set the sensor name (which is also the key to retrieve calibration settings
        from the config file.  Reference the parent screen for move_to() function.
        Reference the calibration screen to set it up to calibrate this setting.'''
        super(Button, self).__init__(**kwargs)
        self.name = name
        # Screen References
        self.parent_screen = parent_screen
        self.calib_screen = calib_screen
        # Kivy Properties
        self.text = name

    def on_release(self):
        if self.name == "IMU Angle":
            self.parent_screen.move_to('dar_imu_calibrate_screen')
        else:
            self.calib_screen.set_sensor(self.name)
            self.parent_screen.move_to('dar_calibrate_screen')

class DAR_SensorsScreen(BaseScreen):
    def __init__(self, **kwargs):
        '''Add a button for each sensor.'''
        super(BaseScreen, self).__init__(**kwargs)
        self.senseMan = Sensor()
        def gui_init(dt):
            '''Called once the Kivy file is parsed. Needed so we can access Kivy IDs.'''
            calib_screen = self.manager.get_screen('dar_calibrate_screen')
            for s in self.senseMan.get_sensor_keys():
                # Perhaps Location and Time should be accessed in some other way?
                if s=='Location' or s=='Time' or s=='Temperature' or s=='Humidity': continue
                if s=='Load Cell Height': s='Load Cell\nHeight'
                # Sensor name, parent screen (of button), calibration screen
                self.ids['sensor_list'].add_widget(DAR_SensorButton(s, self, calib_screen))
        Clock.schedule_once(gui_init)

    def on_enter(self):
        
        log=TestLog()
        log.connection("Entered DAR_SensorsScreen")

    def restart_OS(self):
        #os.system("python3 main.py")
        os.system("reboot")
