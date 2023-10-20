"""
Test in Progress
"""


from genericpath import isdir
from kivy.lang import Builder

from kivy.properties import ListProperty
from kivy.properties import ObjectProperty
from kivy.clock import Clock
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

Builder.load_file('view/screens/main/testing/TestFoldersScreen.kv')

FOLDERNAME = "Tests/"+config.get('selected_folder',0)

class Folder(SingleSelectableListBehavior, Label):
    pass


class NavButton(Button):
    pass


class FolderList(SingleSelectableList):
    def update(self, k, val):
        self.data = [{'text': str(x)} for x in self.list_data]


class TestFoldersScreen(BaseScreen):
    USB_TEST_FOLDERS_PATH = '/mnt/usbStick'

    def __init__(self, **kwargs):
        super(BaseScreen, self).__init__(**kwargs)
        self.back_button = GranuSideButton(text='Back')
        self.back_button.bind(on_release=self.go_back)
        self.delete_button = GranuSideButton(text='Delete\nFolder')
        self.delete_button.bind(on_release=self.delete_folder)
        self.view_tests_button = GranuSideButton(text='View\nTests')
        self.view_tests_button.bind(on_release=self.view_tests)
        self.rename_folder_button = GranuSideButton(text='Rename\nFolder')
        self.rename_folder_button.bind(on_release=self.rename_folder)

        def gui_init(dt):
            self.test_screen = self.manager.get_screen('tests_screen')
            self.parent_screen = self
        Clock.schedule_once(gui_init)

    def on_pre_enter(self):
        self.test_folder_names = [f for f in listdir("Tests") if (
            isdir(join("Tests", f)) and f != ".gitignore")]

        self.default_folders_buttons()

        self.ids['folders_list'].list_data = self.test_folder_names
        self.folder_list = self.ids['folders_list']

    def go_back(self, obj):
        super(TestFoldersScreen, self).back()

    def delete_folder(self, obj):
        selected = self.folder_list.get_selected()
        config.set('unwanted_folder', str(selected[0]))
        self.parent_screen.move_to('delete_folder_confirmation')

    def view_tests(self, obj):
        selected = self.folder_list.get_selected()
        config.set('selected_folder', str(selected[0]))
        self.parent_screen.move_to('tests_screen')

    def rename_folder(self,obj):
        selected = self.folder_list.get_selected()
        config.set('selected_folder', str(selected[0]))
        self.parent_screen.move_to('rename_folder_screen')

    def default_folders_buttons(self):
        buttons = self.ids['folders_buttons']
        buttons.clear_widgets()
        buttons.add_widget(self.back_button)
        buttons.add_widget(Widget())

    def folder_buttons(self):
        buttons = self.ids['folders_buttons']
        buttons.clear_widgets()
        buttons.add_widget(self.back_button)
        buttons.add_widget(self.view_tests_button)
        buttons.add_widget(self.rename_folder_button)
        buttons.add_widget(self.delete_button)

    def on_leave(self):
        if os.path.ismount(self.USB_TEST_FOLDERS_PATH):
            os.system("sudo umount /mnt/usbStick")
