"""
Test in Progress
"""


from kivy.lang import Builder

from kivy.properties import ListProperty
from kivy.properties import ObjectProperty
import configurator as config

from TestSingleton import TestSingleton
from shutil import copyfile


from kivy.uix.popup import Popup

from view.BaseScreen import BaseScreen
from view.SingleSelectableList import SingleSelectableList, SingleSelectableListBehavior, SingleSelectableRecycleBoxLayout
from view.elements import *
import os
from os import listdir
from os.path import isfile, join

from kivy.garden.graph import Graph, MeshLinePlot

Builder.load_file('view/screens/main/testing/TestsScreen.kv')

class Test(SingleSelectableListBehavior, Label):
    pass

class TestList(SingleSelectableList):
    def update(self, k, val):
        self.data = [{'text': str(x)} for x in self.list_data]

class SaveTestDialog(Popup):
    '''A dialog to save a file.  The save and cancel properties point to the
    functions called when the save or cancel buttons are pressed.'''
    save = ObjectProperty(None)
    cancel = ObjectProperty(None)

class TestsScreen(BaseScreen):

    def __init__(self, **kwargs):
        super(BaseScreen, self).__init__(**kwargs)
        self.back_button = GranuSideButton(text = 'Back')
        self.back_button.bind(on_release = self.go_back)
        self.remove_button = GranuSideButton(text = 'Remove\nAll')
        self.remove_button.bind(on_release = self.remove_tests)
        self.export_button = GranuSideButton(text = 'Export\nAll')
        self.export_button.bind(on_release = self.export_tests)
        self.test_details_button = GranuSideButton(text = 'Test\nDetails')
        self.test_details_button.bind(on_release = self.test_details)

    def on_pre_enter(self):
        self.test_filenames = [f for f in listdir("Tests") if (isfile(join("Tests", f)) and f != ".gitignore")]

        self.default_buttons()

        self.ids['tests_list'].list_data = self.test_filenames

    def go_back(self, obj):
        super(TestsScreen, self).back()

    def remove_tests(self, obj):
        for name in self.test_filenames:
            if name != '.gitignore':
                os.remove('Tests/' + name)
        self.test_filenames = [f for f in listdir("Tests") if (isfile(join("Tests", f)) and f != ".gitignore")]
        self.ids['tests_list'].list_data = self.test_filenames
        # print("We should remove all tests!")

    def dismiss_popup(self):
        self._popup.dismiss()

    def export_tests(self, obj):
        USB_TEST_FOLDERS_PATH = '/dev/usbStick'
        try:
            os.system("sudo mount -t vfat -o uid=pi,gid=pi /dev/sda1 /mnt/usbStick")
        except:
            print("USB Not Mounted")
        if os.path.exists('/dev/usbStick/Tests'):
            pass
        else:
            try:
                os.makedirs('/dev/usbStick/Tests')
            except:
                print("Couldn't create Tests folder on USB")
        self._popup = SaveTestDialog(save=self.save, cancel=self.dismiss_popup)
        self._popup.open()
        # print("We should export all tests!")

    def save(self, path):
        config.save_as(os.path.join(path, "test"))
        for name in self.test_filenames:
            if name != '.gitignore':
                copyfile('Tests/' + name, path + "/" + name)
                os.remove('Tests/' + name)
            self.dismiss_popup()

    def set_test_name(self):
        ts = TestSingleton()
        filename = self.ids['tests_list'].remove_selected()
        ts.set_test_details_name(filename[0])

    def test_details(self, obj):
        print("We should show test details!")

    # Button Changes

    def default_buttons(self):
        buttons = self.ids['tests_buttons']
        buttons.clear_widgets()
        buttons.add_widget(self.back_button)
        buttons.add_widget(self.remove_button)
        buttons.add_widget(self.export_button)
        buttons.add_widget(Widget())

    def test_buttons(self):
        buttons = self.ids['tests_buttons']
        buttons.clear_widgets()
        buttons.add_widget(self.back_button)
        buttons.add_widget(self.remove_button)
        buttons.add_widget(self.export_button)
        buttons.add_widget(self.test_details_button)


    def on_leave(self):
        try:
            os.system("sudo umount /mnt/usbStick")
        except:
            print('USB not Unmounted')
