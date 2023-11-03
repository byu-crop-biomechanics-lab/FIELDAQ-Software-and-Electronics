"""
An input text box that, when selected, allows the user to type in a new note via a touch
screen keyboard that will pop up. The input text box will iniinputally be empty.
"""

from kivy.lang import Builder

import configurator as config
from view.BaseScreen import BaseScreen
from view.input.StrInput import StrInput

Builder.load_file('view/screens/settings/NewNoteScreen.kv')

class NewNoteScreen(BaseScreen):
    def on_pre_enter(self):
        input = self.ids['note']
        input.text = ''

    def on_enter(self):
        """Once the Screen loads, focus the Texinputnput"""
        input = self.ids['note']
        input.focus = True

    def save(self):
        notes = config.get('notes', {
            "pretest": [],
            "posttest": [],
            "bank": []
        })
        input = self.ids['note']

        note = input.text
        valid = input.validate()
        exists = (note in notes['pretest']) or (note in notes['posttest']) \
            or (note in notes['bank'])

        if valid and not exists:
            notes['bank'].append(input.text)
            config.set('notes', notes)
            return True
        else:
            input.show_invalid()
            input.focus = True
            return False
