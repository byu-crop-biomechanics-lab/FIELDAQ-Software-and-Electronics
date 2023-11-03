"""
Test in Progress
"""


from kivy.lang import Builder

from kivy.properties import ListProperty
from kivy.properties import ObjectProperty
import configurator as config

from TestSingleton import TestSingleton
from shutil import copyfile
import datetime

from kivy.uix.popup import Popup

from view.BaseScreen import BaseScreen
from view.SingleSelectableList import SingleSelectableList, SingleSelectableListBehavior, SingleSelectableRecycleBoxLayout
from view.elements import *
import os
from os import listdir
from os.path import isfile, join

from kivy.garden.graph import Graph, MeshLinePlot

Builder.load_file('view/screens/settings/ArchiveScreen.kv')

class TestArch(SingleSelectableListBehavior, Label):
    pass

class ArchNavButton(Button):
    pass

class TestListArch(SingleSelectableList):
    def update(self, k, val):
        self.data = [{'text': str(x)} for x in self.list_data]

class SaveTestDialogArch(Popup):
    '''A dialog to save a file.  The save and cancel properties point to the
    functions called when the save or cancel buttons are pressed.'''
    save = ObjectProperty(None)
    cancel = ObjectProperty(None)

class SaveConfirmDialogArch(Popup):
    '''A dialog to save a file.  The save and cancel properties point to the
    functions called when the save or cancel buttons are pressed.'''
    save = ObjectProperty(None)
    pathSelector = ObjectProperty(None)
    cancel = ObjectProperty(None)

class NoUsbDialogArch(Popup):
    '''A dialog to save a file.  The save and cancel properties point to the
    functions called when the save or cancel buttons are pressed.'''
    cancel = ObjectProperty(None)

class ArchiveScreen(BaseScreen):
    USB_TEST_FOLDERS_PATH = '/mnt/usbStick'

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
        self.test_filenames = [f for f in listdir("TestArchive") if (isfile(join("TestArchive", f)) and f != ".gitignore")]

        self.default_buttons()

        self.ids['tests_list'].list_data = self.test_filenames

    def go_back(self, obj):
        super(ArchiveScreen, self).back()

    def remove_tests(self, obj):
        super(ArchiveScreen, self).move_to('test_delete_confirmation')

    def dismiss_popup(self):
        self._popup.dismiss()

    def export_tests(self, obj):
        if not os.path.ismount(self.USB_TEST_FOLDERS_PATH):
            try:
                os.system("sudo mount -t vfat -o uid=pi,gid=pi /dev/sda1 /mnt/usbStick")
            except:
                print("USB Not Mounted")
        self._popup = SaveConfirmDialog(save=self.usbSave, pathSelector=self.pathSelector, cancel=self.dismiss_popup)
        self._popup.open()
        # print("We should export all tests!")

    def pathSelector(self): # , obj):
        self.dismiss_popup()
        self._popup = SaveTestDialog(save=self.save, cancel=self.dismiss_popup)
        self._popup.open()

    def usbSave(self, path):
        if os.path.ismount(self.USB_TEST_FOLDERS_PATH):
            self.save(path)
        else:
            self.noUSB()

    def noUSB(self):
        self.dismiss_popup()
        self._popup = NoUsbDialog(cancel=self.dismiss_popup)
        self._popup.open()

    def save(self, path):
        dt = datetime.datetime.now()
        configName = 'config_' + dt.strftime('%Y_%m_%d_%H_%M_%S') + '.txt'
        subFold = 'Tests_' + dt.strftime('%Y_%m_%d')
        try:
            if not os.path.exists(path+'/'+subFold):
                os.makedirs(path + '/' + subFold)
        except:
            pass
        try:
            config.save_as(os.path.join(path + '/' + subFold, configName))
            for name in self.test_filenames:
                if name != '.gitignore':
                    copyfile('TestArchive/' + name, path + '/' + subFold + "/" + name)
                    # os.remove('TestArchive/' + name)
                self.dismiss_popup()
        except:
            config.save_as(os.path.join(path, configName))
            for name in self.test_filenames:
                if name != '.gitignore':
                    copyfile('TestArchive/' + name, path + "/" + name)
                    # os.remove('TestArchive/' + name)
                self.dismiss_popup()
        self.test_filenames = [f for f in listdir("Tests") if (isfile(join("Tests", f)) and f != ".gitignore")]
        self.ids['tests_list'].list_data = self.test_filenames

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
        if os.path.ismount(self.USB_TEST_FOLDERS_PATH):
            os.system("sudo umount /mnt/usbStick")
