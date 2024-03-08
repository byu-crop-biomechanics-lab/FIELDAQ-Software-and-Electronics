
import os
import json


class SettingsSingleton():
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(SettingsSingleton, cls).__new__(cls)
            cls.device = ""
            cls.CONFIG_FILE = 'Devices/Rodney/Settings/config.json'
            cls.data = {}
            cls.load(cls)
        return cls._instance
        
    def clear_all(self):
        self.device = ""
        self.CONFIG_FILE = 'Devices/Rodney/Settings/config.json'
        self.data = {}
        
    def load(self):
        """Loads data from the configuration file, if it exists."""
        self.data = {}
        if os.path.isfile(self.CONFIG_FILE):
            with open(self.CONFIG_FILE) as f:
                self.data.update(json.load(f))
        else:
            self.data = {}

    def load_from(self, filepath):
        '''Loads data from a specified configuration file.  Overwrites CONFIG_FILE'''
        if os.path.isfile("Devices/Rodney/Settings/config.json"):
            with open("Devices/Rodney/Settings/config.json") as f:
                self._shared_borg_state.update(json.load(f))
                self.save()
        else:
            self.data = {}

    def save(self):
        """Saves data to the configuration file."""
        with open(self.CONFIG_FILE, 'w') as outfile:
            json.dump(self.data, outfile, indent=4)

    def save_as(self, filepath):
        '''Saves data to the specified file.'''
        with open(filepath, 'w') as outfile:
            json.dump(self.data, outfile, indent=4)

    def set(self, key, value):
        """Set a key to value in the configuration JSON file."""
        # Set key to value
        self.data[key] = value
        self.save()

    def get(self, key, default):
        """Get a value from the configuration JSON file using a key.  If the value does not
        exist, save the default value into the JSON file and return the default."""
        if key in self.data:
            return self.data.get(key)
        else:
            self.set(key, default)
            return default


