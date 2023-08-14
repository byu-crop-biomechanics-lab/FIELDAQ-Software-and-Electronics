from kivy.lang import Builder

from kivy.uix.recycleview import RecycleView
from kivy.uix.recycleview.views import RecycleDataViewBehavior
from kivy.uix.label import Label
from kivy.properties import BooleanProperty
from kivy.uix.recycleboxlayout import RecycleBoxLayout
from kivy.uix.behaviors import FocusBehavior
from kivy.uix.recycleview.layout import LayoutSelectionBehavior
from kivy.uix.behaviors import ButtonBehavior

from kivy.properties import ListProperty

Builder.load_file('view/SingleSelectableList.kv')

class SingleSelectableListBehavior(RecycleDataViewBehavior):
    '''Add selection support to a Label.'''
    index = None
    selected = BooleanProperty(False)
    singleSelectable = BooleanProperty(True)

    def refresh_view_attrs(self, rv, index, data):
        '''Catch and handle data changes.'''
        self.index = index
        return super(SingleSelectableListBehavior, self).refresh_view_attrs(rv, index, data)

    def on_touch_down(self, touch):
        '''Select this item on touch down.'''
        if super(SingleSelectableListBehavior, self).on_touch_down(touch):
            return True
        if self.collide_point(*touch.pos) and self.selectable:
            ret = self.parent.select_with_touch(self.index, touch)
            self.parent.parent._interact() # SelectableList was interacted with
            return ret

    def apply_selection(self, rv, index, is_selected):
        '''Respond to the selection of items in the view.'''
        self.selected = is_selected

class SingleSelectableRecycleBoxLayout(FocusBehavior, LayoutSelectionBehavior,
                                 RecycleBoxLayout):
    ''' Adds selection and focus behaviour to the view. '''

class SingleSelectableList(RecycleView):
    '''A selectable list widget, that allows you to modify its data.

    Known issues: Changing data in a RecycleView causes "sys.excepthook' errors at close:
    https://github.com/kivy/kivy/issues/5986'''

    __events__ = ('on_interaction', 'on_deselect_all', ) # Add an event that can be defined in a kv file
    list_data = ListProperty() # List of strings to be shown in the list

    def __init__(self, **kwargs):
        '''Update the SelectableList's RecycleView data whenever list_data changes.'''
        super(SingleSelectableList, self).__init__(**kwargs)
        self.bind(list_data=self.update)

    # Abstract!
    def update(self, k, val):
        '''Uses list_data to generate SelectableListWidgets.'''

    def _interact(self):
        '''Called by a list item when it is touched. Dispatches an on_interaction
        event.'''
        self.dispatch('on_interaction') # Call the Kivy event on_interaction
        if len(self.layout_manager.selected_nodes) == 0:
            self.dispatch('on_deselect_all')

    def clear_selection(self):
        '''Clears the selection in the SelectableList'''
        lm = self.layout_manager
        lm.clear_selection()

    def get_selected(self):
        '''Returns the items currently selected.'''
        lm = self.layout_manager
        sels = []
        for i in lm.selected_nodes:
            sels.append(self.list_data[i])
        return sels

    def remove_selected(self):
        '''Removes the selection in the SelectableList.  Returns the items removed.'''
        lm = self.layout_manager
        removed = []
        for i in lm.selected_nodes:
            removed.append(self.list_data[i])
        lm.clear_selection()
        for item in removed:
            self.list_data.remove(item)
        return removed

    def add_items(self, list):
        '''Add items to the list.'''
        self.list_data = self.list_data + list

    def on_interaction(self, *largs):
        '''A Kivy event: can be defined in a kv file.  Called when the SelectableList
        gains focus.'''
        pass

    def on_deselect_all(self, *largs):
        '''A Kivy event: can be defined in a kv file.  Called when the user deselects the
        last selected item in the SelectableList are deselected.'''
        pass
