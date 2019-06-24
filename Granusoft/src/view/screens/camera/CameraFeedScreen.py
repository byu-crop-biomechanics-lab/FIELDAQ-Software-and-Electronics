"""
The main screen contains four buttons for navigation:
Settings, Testing, Live Feed, and Exit

It also shows environment data: Temperature, Humidity, Location, and Time.
"""

from kivy.lang import Builder
from kivy.properties import StringProperty
from kivy.clock import Clock
from view.BaseScreen import BaseScreen
import datetime
from Sensor import Sensor

try:
    from picamera import PiCamera
except:
    pass

Builder.load_file('view/screens/camera/CameraFeedScreen.kv')

class CameraFeedScreen(BaseScreen):
    try:
        camera = PiCamera(resolution=(1120,920))
    except:
        pass

    def on_enter(self):
        try:
            self.camera.start_preview(rotation=180,fullscreen=False,window=(230,10,560,460))
        except:
            print('No Camera Found')
    def captureImage(self):
        try:
            sensor = Sensor()
            sensor.get_header_data()
            location = [str("%.5f" % sensor_data["Location"][0]), str("%.5f" % sensor_data["Location"][1])]
            camera.exif_tags['GPS.GPSLatitude'] = location[0]
            camera.exif_tags['GPS.GPSLongitude'] = location[1]
        except:
            print('Location Data not added')
        try:
            dt = datetime.datetime.now()
            filename = 'Images/Stalk_' + dt.strftime('%Y_%m_%d_%H_%M_%S') + '.jpg'
            self.camera.capture(filename)
        except:
            print('Taking Imaginary Picture')

    def on_leave(self):
        try:
            self.camera.stop_preview()
        except:
            pass
