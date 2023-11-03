"""
The Camera Feed Screen is designed to preview the camera and allow the user to
take a picture by pressing a button.

EXIF tags are added to the image to record important, relevant, information.

A try/except mechanism is used here so that the code may still be tested on
computers for debugging.
"""

from kivy.lang import Builder
from kivy.properties import StringProperty
from kivy.clock import Clock
from view.BaseScreen import BaseScreen
import datetime
from Sensor import Sensor
import configurator as config

try:
    from picamera import PiCamera
except:
    pass

Builder.load_file('view/screens/camera/CameraFeedScreen.kv')

class CameraFeedScreen(BaseScreen):
    try:
        camera = PiCamera(resolution=(2240,1840))
    except:
        pass
    try:
        camera.exif_tags['IFD0.Artist']=str(config.get('operator', 0))
        camera.exif_tags['IFD0.ImageDescription']=str('PLOT: ' + str(config.get('plot_num', 0)) + ', HEIGHT: ' + str(config.get('height', 0)))
        camera.exif_tags['IFD0.Copyright'] = 'Copyright (c) 2019 BYU Crop Biomechanics Laboratory'
    except:
        pass # print('No Operator Data Added')

    def on_pre_enter(self):
        sensor = Sensor()
        sensor.clear_gps_memory()

    def on_enter(self):
        try:
            self.camera.start_preview(rotation=180,fullscreen=False,window=(230,10,560,460))
        except:
            pass # print('No Camera Found')
    def captureImage(self):
        try:
            def decdeg2dms(dd):
                dd = abs(dd)
                minutes,seconds = divmod(dd*3600,60)
                degrees,minutes = divmod(minutes,60)
                return (degrees,minutes,seconds)
            sensor = Sensor()
            sensor.get_header_data()
            sensor_data = sensor.get_sensor_data()
            location = [sensor_data["Location"][0], sensor_data["Location"][1]]
            latdms = decdeg2dms(location[0])
            londms = decdeg2dms(location[1])
        except:
            # print('Location Data not found')
            location = [0, 0]
        try:
            self.camera.exif_tags['GPS.GPSLatitudeRef'] = 'N' if location[0] > 0 else 'S'
            self.camera.exif_tags['GPS.GPSLongitudeRef'] = 'E' if location[1] > 0 else 'W'
            self.camera.exif_tags['GPS.GPSLatitude'] = '%d/1,%d/1,%d/100' % (latdms[0], latdms[1], latdms[2])
            self.camera.exif_tags['GPS.GPSLongitude'] = '%d/1,%d/1,%d/100' % (londms[0], londms[1], londms[2])
        except:
            pass # print('Location Data not added')
        try:
            dt = datetime.datetime.now()
            filename = 'Images/Stalk_' + dt.strftime('%Y_%m_%d_%H_%M_%S') + '.jpg'
            self.camera.capture(filename)
        except:
            pass # print('Taking Imaginary Picture')

    def on_leave(self):
        try:
            self.camera.stop_preview()
        except:
            pass
