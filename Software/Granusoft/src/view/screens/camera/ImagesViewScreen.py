"""
This screen lists all of the images in src/Images that the user can interact
with. All images can be exported, or removed. Or images may be viewed
individually.
"""


from kivy.lang import Builder

from kivy.properties import ListProperty
from kivy.properties import ObjectProperty
import configurator as config

from shutil import copyfile
import shutil

from kivy.uix.popup import Popup

from view.BaseScreen import BaseScreen
from view.SingleSelectableList import SingleSelectableList, SingleSelectableListBehavior, SingleSelectableRecycleBoxLayout
from view.elements import *
import os
import datetime
from os import listdir
from os.path import isfile, join

Builder.load_file('view/screens/camera/ImagesViewScreen.kv')

class ImagePic(SingleSelectableListBehavior, Label):
    pass

class ImageList(SingleSelectableList):
    def update(self, k, val):
        self.data = [{'text': str(x)} for x in self.list_data]

class SaveImageDialog(Popup):
    '''A dialog to save a file.  The save and cancel properties point to the
    functions called when the save or cancel buttons are pressed.'''
    save = ObjectProperty(None)
    cancel = ObjectProperty(None)

class ImagesViewScreen(BaseScreen):
    USB_IMG_FOLDERS_PATH = '/mnt/usbStick'

    def __init__(self, **kwargs):
        super(BaseScreen, self).__init__(**kwargs)
        self.back_button = GranuSideButton(text = 'Back')
        self.back_button.bind(on_release = self.go_back)
        self.remove_button = GranuSideButton(text = 'Remove\nAll')
        self.remove_button.bind(on_release = self.remove_images)
        self.export_button = GranuSideButton(text = 'Export\nAll')
        self.export_button.bind(on_release = self.export_images)
        self.image_details_button = GranuSideButton(text = 'View\nImage')
        self.image_details_button.bind(on_release = self.image_details)

    def on_pre_enter(self):
        self.image_filenames = [f for f in listdir("Images") if (isfile(join("Images", f)) and f != ".gitignore")]

        self.default_buttons()

        self.ids['images_list'].list_data = self.image_filenames

    def go_back(self, obj):
        super(ImagesViewScreen, self).back()

    def remove_images(self, obj):
        super(ImagesViewScreen, self).move_to('img_delete_confirmation')

    def dismiss_popup(self):
        self._popup.dismiss()

    def export_images(self, obj):
        if not os.path.ismount(self.USB_IMG_FOLDERS_PATH):
            try:
                os.system("sudo mount -t vfat -o uid=pi,gid=pi /dev/sda1 /mnt/usbStick")
            except:
                print("USB Not Mounted")
        self._popup = SaveImageDialog(save=self.save, cancel=self.dismiss_popup)
        self._popup.open()
        # print("We should export all images!")

    def save(self, path):
        dt = datetime.datetime.now()
        subFold = 'Images_' + dt.strftime('%Y_%m_%d')
        try:
            if not os.path.exists(path + '/' + subFold):
                os.makedirs(path + '/' + subFold)
        except:
                pass
        config.save_as(os.path.join(path, "image"))
        for name in self.image_filenames:
            if name != '.gitignore':
                fromDir = 'Images/' + name
                toDir = path + "/" + subFold + '/' + name
                copyfile(fromDir, toDir)
                #os.system("cp " + fromDir + " " + toDir)
                #shutil.copy('Images/' + name, path + "/" + name)
                # os.remove('Images/' + name)
            self.dismiss_popup()
        if os.path.ismount(self.USB_IMG_FOLDERS_PATH):
            os.system("sudo umount /mnt/usbStick")

    def image_details(self, obj):
        imagename = self.ids['images_list'].remove_selected()
        img_screen = self.manager.get_screen('img_review_screen')
        img_screen.set_image(imagename[0])
        super(ImagesViewScreen, self).move_to('img_review_screen')

    # Button Changes

    def default_buttons(self):
        buttons = self.ids['images_buttons']
        buttons.clear_widgets()
        buttons.add_widget(self.back_button)
        buttons.add_widget(self.remove_button)
        buttons.add_widget(self.export_button)
        buttons.add_widget(Widget())

    def image_buttons(self):
        buttons = self.ids['images_buttons']
        buttons.clear_widgets()
        buttons.add_widget(self.back_button)
        buttons.add_widget(self.remove_button)
        buttons.add_widget(self.export_button)
        buttons.add_widget(self.image_details_button)


    def on_leave(self):
        if os.path.ismount(self.USB_IMG_FOLDERS_PATH):
            os.system("sudo umount /mnt/usbStick")
