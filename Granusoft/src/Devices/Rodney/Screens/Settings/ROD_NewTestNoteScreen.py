"""
An input text box that, when selected, allows the user to type in a new note via a touch
screen keyboard that will pop up. The input text box will iniinputally be empty.
"""

from kivy.lang import Builder
from util.TestLog import TestLog
from Devices.Rodney.Settings.configurator import SettingsSingleton as settings
from util.BaseScreen import BaseScreen
from util.getKVPath import getKVPath
import os

Builder.load_file(getKVPath(os.getcwd(), __file__))

class ROD_NewTestNoteScreen(BaseScreen):
    def on_pre_enter(self):
        input = self.ids['note']
        input.text = ''
        self.config = settings()

    def on_enter(self):
        """Once the Screen loads, focus the Texinputnput"""
        
        log = TestLog()
        log.connection("Entering ROD_NewTestNoteScreen")
        input = self.ids['note']
        input.focus = True

    def save(self):
        notes = self.config.get('notes', {
            "pretest": [],
            "posttest": [],
            "bank": []
        })

        test_notes = self.config.get('test_notes', {
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
            self.config.set('notes', notes)
            return True
        else:
            input.show_invalid()
            input.focus = True
            return False

    def clear_config(self):
        test_notes = self.config.get('test_notes', {
            "pretest": [],
            "posttest": [],
            "bank": []
        })
        
        self.config.set('test_notes',test_notes)