from kivy.lang import Builder
from kivy.uix.recycleview import RecycleView
from kivy.uix.recycleview.views import RecycleDataViewBehavior
from kivy.uix.label import Label
from kivy.uix.recycleboxlayout import RecycleBoxLayout
from kivy.properties import ListProperty

Builder.load_file('view/StaticList.kv')

class StaticRecycleBoxLayout(RecycleBoxLayout):
    pass

class StaticLabel(RecycleDataViewBehavior, Label):
    '''Refresh Labels when list is changed.'''
    index = None

    def refresh_view_attrs(self, rv, index, data):
        '''Catch and handle data changes.'''
        self.index = index
        return super(StaticLabel, self).refresh_view_attrs(rv, index, data)

class StaticList(RecycleView):
    '''A static list widget.

    Known issues: Changing data in a RecycleView causes "sys.excepthook' errors at close:
    https://github.com/kivy/kivy/issues/5986'''

    list_data = ListProperty() # List of strings to be shown in the list

    def __init__(self, **kwargs):
        '''Update the StaticList's RecycleView data whenever list_data changes.'''
        super(StaticList, self).__init__(**kwargs)
        self.bind(list_data=self._update)

    def _update(self, k, val):
        '''Uses list_data to generate StaticLabels.'''
        self.data = [{'text': str(x)} for x in self.list_data]
