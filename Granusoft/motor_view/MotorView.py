from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout

Builder.load_file('MotorView.kv')

class MotorView(BoxLayout):
    def __init__(self, **kwargs):
        super(MotorView,self).__init__(**kwargs)
        self.ids['slider1'].bind(value=self.update)
        self.ids['slider2'].bind(value=self.update)
        self.ids['slider3'].bind(value=self.update)
        self.ids['slider4'].bind(value=self.update)

    def update(self, obj, value):
        value1 = self.ids['slider1'].value
        value2 = self.ids['slider2'].value
        value3 = self.ids['slider3'].value
        value4 = self.ids['slider4'].value
        print('Values:')
        print(value1)
        print(value2)
        print(value3)
        print(value4)
