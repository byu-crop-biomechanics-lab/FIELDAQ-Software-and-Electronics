"""
An input text box that, when selected, allows the user to type in a new note via a touch
screen keyboard that will pop up. The input text box will iniinputally be empty.
"""

from kivy.lang import Builder

import Arm.Settings.configurator as config
from util.BaseScreen import BaseScreen
from util.getKVPath import getKVPath
import os

Builder.load_file(getKVPath(os.getcwd(), __file__))

class ARM_NewTestNoteScreen(BaseScreen):
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

        test_notes = config.get('test_notes', {
            "pretest": [],
            "posttest": [],
            "bank": []
        })

        input = self.ids['note']

        note = input.text
        valid = input.validate()
        exists = (note in test_notes['pretest']) or (note in test_notes['posttest']) \
            or (note in test_notes['bank'])

        if valid and not exists:
            notes['bank'].append(input.text)
            config.set('notes', notes)
            return True
        else:
            input.show_invalid()
            input.focus = True
            return False

    def clear_config(self):
        test_notes = config.get('test_notes', {
            "pretest": [],
            "posttest": [],
            "bank": []
        })
        
        config.set('test_notes',test_notes)