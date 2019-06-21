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

try:
    from picamera import PiCamera
except:
    pass

Builder.load_file('view/screens/camera/CameraFeedScreen.kv')

class CameraFeedScreen(BaseScreen):
    try:
        camera = PiCamera()
    except:
        pass

    def on_enter(self):
        try:
            self.camera.start_preview(alpha=250)
        except:
            pass

    def on_leave(self):
        try:
            self.camera.stop_preview()
        except:
            pass
