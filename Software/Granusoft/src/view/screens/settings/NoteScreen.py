from kivy.lang import Builder
from kivy.properties import ListProperty

import configurator as config
from view.BaseScreen import BaseScreen
from view.SelectableList import SelectableList, SelectableListBehavior, SelectableRecycleBoxLayout
from view.elements import *

Builder.load_file('view/screens/settings/NoteScreen.kv')

class Note(SelectableListBehavior, Label):
    pass

class NoteList(SelectableList):
    def update(self, k, val):
        self.data = [{'text': str(x)} for x in self.list_data]

class NoteScreen(BaseScreen):
    '''Manages the Notes.

    Be careful not to make a shallow copy of list_data for any SelectableList'''

    # Setup!

    def __init__(self, **kwargs):
        '''Creates Kivy Buttons to be able to dynamically change the sidebar actions
        based on interaction with the lists.'''
        super(BaseScreen, self).__init__(**kwargs)

        self.save_button = GranuSideButton(text = 'Back')
        self.save_button.bind(on_release = self.save)
        self.new_button = GranuSideButton(text = 'New')
        self.new_button.bind(on_release = self.new)
        self.remove_button = GranuSideButton(text = 'Remove')
        self.remove_button.bind(on_release = self.remove)
        self.delete_button = GranuSideButton(text = 'Delete')
        self.delete_button.bind(on_release = self.delete)

    def on_pre_enter(self):
        """Before the Screen loads, read the configuration file to get the current
        list of notes. Show the default buttons."""

        # Get notes from config file
        notes = config.get('notes', {
            "pretest": [],
            "posttest": [],
            "bank": []
        })
        # Set the data
        self.ids['pretest'].list_data = notes["pretest"]
        self.ids['posttest'].list_data = notes["posttest"]
        self.ids['bank'].list_data = notes["bank"]

        # Add Buttons
        self.default_buttons()

    def _save_config(self):
        '''Save the notes to the configuration file.'''
        config.set('notes', {
            "pretest": self.ids['pretest'].list_data,
            "posttest": self.ids['posttest'].list_data,
            "bank": self.ids['bank'].list_data
        })


    # Button Changes

    def default_buttons(self):
        buttons = self.ids['note_buttons']
        buttons.clear_widgets()
        buttons.add_widget(self.save_button)
        buttons.add_widget(self.new_button)
        buttons.add_widget(Widget())
        buttons.add_widget(Widget())

    def test_buttons(self):
        buttons = self.ids['note_buttons']
        buttons.clear_widgets()
        buttons.add_widget(self.save_button)
        buttons.add_widget(self.new_button)
        buttons.add_widget(Widget())
        buttons.add_widget(self.remove_button)

    def bank_buttons(self):
        buttons = self.ids['note_buttons']
        buttons.clear_widgets()
        buttons.add_widget(self.save_button)
        buttons.add_widget(self.new_button)
        buttons.add_widget(Widget())
        buttons.add_widget(self.delete_button)

    # Button Actions

    def save(self, obj):
        self._save_config()
        super(NoteScreen, self).back()

    def new(self, obj):
        self._save_config()
        self.move_to('new_note_screen')

    def remove(self, obj):
        '''Move selected notes to the Note Bank'''
        notes = self.ids['pretest'].remove_selected() \
            + self.ids['posttest'].remove_selected()
        self.ids['bank'].add_items(notes)
        self.default_buttons()

    def delete(self, obj):
        self.ids['bank'].remove_selected()
        self.default_buttons()

    # Content Buttons

    def move_to_pretest(self):
        notes = self.ids['pretest'].remove_selected() \
            + self.ids['posttest'].remove_selected() \
            + self.ids['bank'].remove_selected()
        self.ids['pretest'].add_items(notes)

    def move_to_posttest(self):
        notes = self.ids['pretest'].remove_selected() \
            + self.ids['posttest'].remove_selected() \
            + self.ids['bank'].remove_selected()
        self.ids['posttest'].add_items(notes)

    def move_to_bank(self):
        notes = self.ids['pretest'].remove_selected() \
            + self.ids['posttest'].remove_selected() \
            + self.ids['bank'].remove_selected()
        self.ids['bank'].add_items(notes)
