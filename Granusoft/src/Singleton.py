import os
import json

class BorgSingleton(object):
  _shared_borg_state = {}
   
  def __new__(cls, *args, **kwargs):
    obj = super(BorgSingleton, cls).__new__(cls, *args, **kwargs)
    obj.__dict__ = cls._shared_borg_state
    return obj


class SettingsSingleton(BorgSingleton):
    _shared_borg_state = {}
    CONFIG_FILE = 'config.json'
    device = ""
    
    def __init__(self):
        super(SettingsSingleton, self).__init__()
        
    def clear_all(self):
        self._shared_borg_state = {}
        self.device = ""
        
    def load(self):
        """Loads data from the configuration file, if it exists."""
        global data
        if os.path.isfile(self.CONFIG_FILE):
            with open(self.CONFIG_FILE) as f:
                data.update(json.load(f))
        else:
            data = {}

    def load_from(self, filepath):
        '''Loads data from a specified configuration file.  Overwrites CONFIG_FILE'''
        global data
        if os.path.isfile(filepath):
            with open(filepath) as f:
                data.update(json.load(f))
                save()
        else:
            data = {}

    def save(self):
        """Saves data to the configuration file."""
        with open(self.CONFIG_FILE, 'w') as outfile:
            json.dump(data, outfile, indent=4)

    def save_as(self, filepath):
        '''Saves data to the specified file.'''
        with open(filepath, 'w') as outfile:
            json.dump(data, outfile, indent=4)

    def set(self, key, value):
        """Set a key to value in the configuration JSON file."""
        # Set key to value
        data[key] = value
        self.save()

    def get(self, key, default):
        """Get a value from the configuration JSON file using a key.  If the value does not
        exist, save the default value into the JSON file and return the default."""
        if key in data:
            return data.get(key)
        else:
            set(key, default)
            return default


class TestSingleton(BorgSingleton):
    _shared_borg_state = {}
    height = ""
    plot = ""
    pre_notes = ""
    post_notes = []
    operator = ""
    timestamp = ""
    datasets = []
    break_height = ""
    
    def __init__(self):
        super(TestSingleton, self).__init__()
        
    def clear_all(self):
        self._shared_borg_state = {}
        self.height = ""
        self.plot = ""
        self.pre_notes = ""
        self.post_notes = []
        self.operator = ""
        self.timestamp = ""
        self.datasets = []
        self.break_height = ""
        
    def print_test(self):
        print("Timestamp:", self.timestamp)
        print("Height:", self.height)
        print("Plot:", self.plot)
        print("Operator:", self.operator)
        print("Break Height:", self.break_height)
        print("Pre Notes:", self.pre_notes)
        print("Post Notes:", self.post_notes)
        print("First Dataset Temp:", self.datasets[0].temperature)
        print("Second Dataset Temp:", self.datasets[1].temperature)

    def get_height(self):
        return self.height

    def set_height(self, height):
        self.height = height

    def get_plot(self):
        return self.plot

    def set_plot(self, plot):
        self.plot = plot

    def get_pre_notes(self):
        return self.pre_notes
        
    def set_pre_notes(self, pre_notes):
        self.pre_notes = pre_notes

    def get_post_notes(self):
        return self.post_notes

    def set_post_notes(self, post_notes):
        self.post_notes = post_notes

    def get_operator(self):
        return self.operator
    
    def set_operator(self, operator):
        self.operator = operator

    def get_timestamp(self):
        return self.timestamp
    def set_timestamp(self, timestamp):
        self.timestamp = timestamp

    def get_datasets(self):
        return self.datasets
    
    def set_datasets(self, datasets):
        self.datasets = datasets

    def get_break_height(self):
        return self.break_height
    
    def set_break_height(self, break_height):
        self.break_height = break_height

# class TestSingleton:
#     class __TestSingleton:
#         def __init__(self):
#             self.clear_all()
#         def clear_all(self):
#             self.height = ""
#             self.plot = ""
#             self.pre_notes = ""
#             self.post_notes = []
#             self.operator = ""
#             self.timestamp = ""
#             self.datasets = []
#             self.break_height = ""
            
#     instance = None
#     def __init__(self):
#         if not TestSingleton.instance:
#             TestSingleton.instance = TestSingleton.__TestSingleton()

#     def clear_all(self):
#         self.instance.clear_all()

#     def print_test(self):
#         print("Timestamp:", self.instance.timestamp)
#         print("Height:", self.instance.height)
#         print("Plot:", self.instance.plot)
#         print("Operator:", self.instance.operator)
#         print("Break Height:", self.instance.break_height)
#         print("Pre Notes:", self.instance.pre_notes)
#         print("Post Notes:", self.instance.post_notes)
#         print("First Dataset Temp:", self.instance.datasets[0].temperature)
#         print("Second Dataset Temp:", self.instance.datasets[1].temperature)

#     def get_height(self):
#         return self.instance.height

#     def set_height(self, height):
#         self.instance.height = height

#     def get_plot(self):
#         return self.instance.plot

#     def set_plot(self, plot):
#         self.instance.plot = plot

#     def get_pre_notes(self):
#         return self.instance.pre_notes
        
#     def set_pre_notes(self, pre_notes):
#         self.instance.pre_notes = pre_notes

#     def get_post_notes(self):
#         return self.instance.post_notes

#     def set_post_notes(self, post_notes):
#         self.instance.post_notes = post_notes

#     def get_operator(self):
#         return self.instance.operator
#     def set_operator(self, operator):
#         self.instance.operator = operator

#     def get_timestamp(self):
#         return self.instance.timestamp
#     def set_timestamp(self, timestamp):
#         self.instance.timestamp = timestamp

#     def get_datasets(self):
#         return self.instance.datasets
#     def set_datasets(self, datasets):
#         self.instance.datasets = datasets

#     def get_break_height(self):
#         return self.instance.break_height
#     def set_break_height(self, break_height):
#         self.instance.break_height = break_height
