"""
This screen needs to accept information about which image to view. Then display
that image. The image can be deleted via this screen [not sure if this
feature should be kept or not], or the user can return to the ImagesViewScreen.
"""

from kivy.lang import Builder
from kivy.properties import StringProperty
from kivy.clock import Clock
from util.BaseScreen import BaseScreen
from Camera.Sensors import Sensor
import datetime

import os
from util.getKVPath import getKVPath

Builder.load_file(getKVPath(os.getcwd(), __file__))

class ImageReviewScreen(BaseScreen):
    image_name = StringProperty()

    def set_image(self, name):
        self.image_name = name

    def delete_button(self):
        os.remove("Images/" + self.image_name)
