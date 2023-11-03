from kivy.lang import Builder
from kivy.clock import Clock
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import StringProperty, ListProperty, NumericProperty
from kivy.properties import ObjectProperty

from view.BaseScreen import BaseScreen
from view.SelectableList import SelectableList, SelectableListBehavior, SelectableRecycleBoxLayout
from view.elements import *

import numpy

import configurator as config

Builder.load_file('view/screens/settings/CalibrateScreen.kv')

class PointDisplay(SelectableListBehavior, Label):
    adc = NumericProperty()
    real = NumericProperty()

class PointsList(SelectableList):
    def update(self, k, val):
        self.data = [{'adc': x[0], 'real': x[1]} for x in self.list_data]

class CalibrateScreen(BaseScreen):
    sensor_name = StringProperty()
    points_list = ListProperty()
    slope = NumericProperty()
    intercept = NumericProperty()

    def __init__(self, **kwargs):
        super(CalibrateScreen, self).__init__(**kwargs)
        self.config_data = {}
        def gui_init(dt):
            self.calibrate_point_screen = self.manager.get_screen('calibrate_point_screen')
            self.parent_screen = self
        Clock.schedule_once(gui_init)

    def on_pre_enter(self):
        self.points_List = self.ids['point_list']
        self.points_List.clear_selection()
        removeButton = self.ids['removal_button']
        removeButton.bind(on_release = self.remove_point)
        addPointButton = self.ids['add_point_button']
        addPointButton.bind(on_release = self.to_points_screen)

    def set_sensor(self, name):
        self.sensor_name = name
        self.config_data = config.get('sensors', {})
        if name in self.config_data:
            self.points_list = self.config_data[name]['points_list']
            self.slope = self.config_data[name]['slope']
            self.intercept = self.config_data[name]['intercept']
        else:
            self.points_list = []
            self.slope = 1
            self.intercept = 0

    def to_points_screen(self, obj):
        self.calibrate_point_screen.set_sensor(self.sensor_name)
        self.parent_screen.move_to('calibrate_point_screen')

    def add_point(self, adc, real):
        self.points_list.append((adc, real))
        # Calculate line of best fit using Least Square Method
        adc_points = [x[0] for x in self.points_list]
        real_points = [x[1] for x in self.points_list]
        if len(self.points_list) > 1:
            poly = numpy.polyfit(adc_points, real_points, 1) # Linear regression
            self.slope = numpy.float(poly[0])
            self.intercept =numpy.float(poly[1])
        else:
            self.slope = 1.0
            self.intercept = 0.0

    def remove_point(self, obj):
        selection = self.points_List.get_selected()
        for items in selection:
            ADC = str(items[0])
            REAL = str(items[1])
            for elem in self.points_list:
                if ADC == str(elem[0]) and REAL == str(elem[1]):
                    try:
                        self.points_list.remove(elem)
                    except:
                        pass
        # Calculate line of best fit using Least Square Method
        try:
            adc_points = [x[0] for x in self.points_list]
            real_points = [x[1] for x in self.points_list]
        except:
            self.points_list = []
        if len(self.points_list) > 1:
            poly = numpy.polyfit(adc_points, real_points, 1) # Linear regression
            self.slope = numpy.float(poly[0])
            self.intercept =numpy.float(poly[1])
        else:
            self.slope = 1.0
            self.intercept = 0.0
        try:
            self.points_List.clear_selection()
        except:
            pass

    def save(self):
        self.config_data[self.sensor_name] = {
            'slope': self.slope,
            'intercept': self.intercept,
            'points_list': self.points_list
        }
        config.set('sensors', self.config_data)
        return True
