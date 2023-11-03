from kivy.clock import Clock
from kivy.uix.textinput import TextInput

import view.keyboard_man as km

class StrInput(TextInput):
    def validate(self):
        '''Make sure the string is not empty or all whitespace.'''
        notempty = len(self.text) > 0 # String is not empty or all whitespace
        notspace = not self.text.isspace()
        test = notempty and notspace
        if test:
            self.show_valid()
        else:
            self.show_invalid()
        return test

    def show_invalid(self):
        '''Colors the textinput red.'''
        self.background_color = (1, .7, .7, 1)

    def show_valid(self):
        '''Colors the textinput white.'''
        self.background_color = (1, 1, 1, 1)

    def on_text_validate(self):
        '''Called when enter is pressed.'''
        self.validate()
        Clock.schedule_once(self.focus_and_select)

    def on_focus(self, instance, value):
        '''When the StrInput is focused, show a qwerty keyboard.'''
        if value:
            km.show_keyboard(self, 'text')

    def focus_and_select(self, *args):
        '''Focus the TextInput and select all of its text.'''
        self.focus = True
        self.select_all()
