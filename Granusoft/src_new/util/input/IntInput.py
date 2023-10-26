from kivy.clock import Clock
from kivy.uix.textinput import TextInput

import view.keyboard_man as km

class IntInput(TextInput):
    def __init__(self, **kwargs):
        '''Ints do not need multiple lines to input, set multiline property to
        false.'''
        super(IntInput, self).__init__(**kwargs)
        self.multiline = False

    def validate(self):
        '''Check that the input can be cast as an int.'''
        test = False
        try:
            fl = int(self.text)
            test = True
        except:
            test = False
        if test:
            self.background_color = (1, 1, 1, 1)
        else:
            self.background_color = (1, .7, .7, 1)
        return test

    def on_text_validate(self):
        '''Called when enter is pressed.'''
        self.validate()
        Clock.schedule_once(self.focus_and_select)

    def on_focus(self, instance, value):
        '''When the IntInput is focused, show a numeric keyboard.'''
        if value:
            km.show_keyboard(self, 'integer')

    def focus_and_select(self, *args):
        '''Focus the TextInput and select all of its text.'''
        self.focus = True
        self.select_all()
