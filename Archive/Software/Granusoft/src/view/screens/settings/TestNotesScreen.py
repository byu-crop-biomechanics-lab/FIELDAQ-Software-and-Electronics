from kivy.lang import Builder
from kivy.properties import ListProperty
from kivy.clock import Clock

import configurator as config
from view.BaseScreen import BaseScreen
from view.SelectableList import SelectableList, SelectableListBehavior, SelectableRecycleBoxLayout
from view.elements import *
import csv

Builder.load_file('view/screens/settings/TestNotesScreen.kv')

class Notes(SelectableListBehavior, Label):
    pass

class NotesList(SelectableList):
    def update(self, k, val):
        self.data = [{'text': str(x)} for x in self.list_data]

class TestNotesScreen(BaseScreen):
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
        self.pre_test_notes = []
        self.post_test_notes = []
        self.notes_bank = []

    def on_pre_enter(self):
        """Before the Screen loads, read the configuration file to get the current
        list of notes. Show the default buttons."""
        current_notes = config.get('notes', {
            "pretest": [],
            "posttest": [],
            "bank": []
        })
        # Get notes from config file
        foldername = "Tests/"+config.get('selected_folder',0)+'/'
        with open(foldername + str(self.fileName)) as testFile:
            readCSV = csv.reader(testFile, delimiter=',')
            testData = 0
            for row in readCSV:
                if 'POST' in row[0]:
                    if len(row[1]) !=0:
                        self.post_test_notes.append(str(row[1]))

                if 'PRE' in row[0]:
                    if len(row[1]) !=0:
                        self.pre_test_notes.append(str(row[1]))      
        # Set the data
        self.ids['pre_test_notes'].list_data = self.pre_test_notes
        self.ids['post_test_notes'].list_data = self.post_test_notes

        for note in current_notes["bank"]:
            if note in self.pre_test_notes or note in self.post_test_notes:
                pass
            else:
                self.notes_bank.append(note)

        self.ids['notes_bank'].list_data = self.notes_bank

        # Add Buttons
        self.default_buttons()

    def _save_config(self):
        '''Save the notes to the configuration file.'''
        config.set('test_notes', {
            "pretest": self.ids['pre_test_notes'].list_data,
            "posttest": self.ids['post_test_notes'].list_data,
            "bank": []# self.ids['notes_bank'].list_data
        })


    # Button Changes

    def default_buttons(self):
        buttons = self.ids['notes_buttons']
        buttons.clear_widgets()
        buttons.add_widget(self.save_button)
        buttons.add_widget(self.new_button)
        buttons.add_widget(Widget())
        buttons.add_widget(Widget())

    def test_buttons(self):
        buttons = self.ids['notes_buttons']
        buttons.clear_widgets()
        buttons.add_widget(self.save_button)
        buttons.add_widget(self.new_button)
        buttons.add_widget(Widget())
        buttons.add_widget(self.remove_button)

    def bank_buttons(self):
        buttons = self.ids['notes_buttons']
        buttons.clear_widgets()
        buttons.add_widget(self.save_button)
        buttons.add_widget(self.new_button)
        buttons.add_widget(Widget())
        buttons.add_widget(self.delete_button)

    # Button Actions

    def save(self, obj):
        self.save_note_changes()
        self.reset_individual_test_notes()
        super(TestNotesScreen, self).back()

    def new(self, obj):
        self._save_config()
        self.reset_individual_test_notes()
        self.move_to('new_test_note_screen')

    def remove(self, obj):
        '''Move selected notes to the Note Bank'''
        notes = self.ids['pre_test_notes'].remove_selected() \
            + self.ids['post_test_notes'].remove_selected()
        self.ids['notes_bank'].add_items(notes)
        self.default_buttons()

    def delete(self, obj):
        self.ids['notes_bank'].remove_selected()
        self.default_buttons()

    # Content Buttons

    def move_to_pretest(self):
        notes = self.ids['pre_test_notes'].remove_selected() \
            + self.ids['post_test_notes'].remove_selected() \
            + self.ids['notes_bank'].remove_selected()
        self.ids['pre_test_notes'].add_items(notes)

    def move_to_posttest(self):
        notes = self.ids['pre_test_notes'].remove_selected() \
            + self.ids['post_test_notes'].remove_selected() \
            + self.ids['notes_bank'].remove_selected()
        self.ids['post_test_notes'].add_items(notes)

    def move_to_bank(self):
        notes = self.ids['pre_test_notes'].remove_selected() \
            + self.ids['post_test_notes'].remove_selected() \
            + self.ids['notes_bank'].remove_selected()
        self.ids['notes_bank'].add_items(notes)

    def reset_individual_test_notes(self):
        self.pre_test_notes = []
        self.post_test_notes = []
        self.notes_bank = []

    def set_file(self, filename):
          self.fileName = filename

    def save_note_changes(self):
        foldername = "Tests/"+config.get('selected_folder',0)+'/'
        pretest_start = 15
        posttest_start = 20
        r = csv.reader(open(foldername + str(self.fileName)))
        lines = list(r)

        for i in range(5):
            try:
                lines[pretest_start][1]=self.ids['pre_test_notes'].list_data[i]
            except:
                lines[pretest_start][1]=''
            pretest_start+=1

        for i in range(5):
            try:
                lines[posttest_start][1] = self.ids['post_test_notes'].list_data[i]
            except:
                lines[posttest_start][1]=''
            posttest_start+=1

        writer = csv.writer(open(foldername + str(self.fileName), 'w+',newline=''))
        writer.writerows(lines)