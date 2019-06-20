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
    def on_enter(self):
        try:
            camera = PiCamera()
            camera.start_preview(alpha=100)
        except:
            pass

    def on_leave(self):
        try:
            camera.stop_preview()
        except:
            pass
