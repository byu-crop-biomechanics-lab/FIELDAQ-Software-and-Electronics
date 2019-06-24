"""
Fill in this summary later
"""


from kivy.lang import Builder

from kivy.properties import ListProperty
import configurator as config



from view.BaseScreen import BaseScreen
from view.SingleSelectableList import SingleSelectableList, SingleSelectableListBehavior, SingleSelectableRecycleBoxLayout
from view.elements import *

from os import listdir
from os.path import isfile, join

from kivy.garden.graph import Graph, MeshLinePlot

Builder.load_file('view/screens/camera/ImagesViewScreen.kv')

class Image(SingleSelectableListBehavior, Label):
    pass

class ImageList(SingleSelectableList):
    def update(self, k, val):
        self.data = [{'text': str(x)} for x in self.list_data]

class ImagesViewScreen(BaseScreen):
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
        self.test_filenames = [f for f in listdir("Images") if isfile(join("Images", f))]



        self.default_buttons()

        self.ids['images_list'].list_data = self.test_filenames


    def go_back(self, obj):
        super(TestsScreen, self).back()

    def remove_tests(self, obj):
        print("We should remove all tests!")

    def export_tests(self, obj):
        print("We should export all tests!")

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
        pass
