
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
































# """
# The configurator module adds an interface to read to and write from the configuration
# file ('config.json').  Reading and writing settings to the configuration file allows the
# configuration to persist beyond the application lifecycle.
# """

# import os
# import json

# CONFIG_FILE = 'config.json'

# data = {}

# def load():
#     """Loads data from the configuration file, if it exists."""
#     global data
#     if os.path.isfile(CONFIG_FILE):
#         with open(CONFIG_FILE) as f:
#             data.update(json.load(f))
#     else:
#         data = {}

# load()

# def load_from(filepath):
#     '''Loads data from a specified configuration file.  Overwrites CONFIG_FILE'''
#     global data
#     if os.path.isfile(filepath):
#         with open(filepath) as f:
#             data.update(json.load(f))
#             save()
#     else:
#         data = {}

# def save():
#     """Saves data to the configuration file."""
#     with open(CONFIG_FILE, 'w') as outfile:
#         json.dump(data, outfile, indent=4)

# def save_as(filepath):
#     '''Saves data to the specified file.'''
#     with open(filepath, 'w') as outfile:
#         json.dump(data, outfile, indent=4)

# def set(key, value):
#     """Set a key to value in the configuration JSON file."""
#     # Set key to value
#     data[key] = value
#     save()

# def get(key, default):
#     """Get a value from the configuration JSON file using a key.  If the value does not
#     exist, save the default value into the JSON file and return the default."""
#     print(data)
#     if key in data:
#         return data.get(key)
#     else:
#         set(key, default)
#         return default

# if __name__ == "__main__":
#     """If the configuration module is run as the main program, test the configurationzzzzz
#     module.  These tests ensure the module returns and saves the default value if a key
#     is not defined, returns the saved value if a key is defined, and that thez
#     configuration file contains the values saved.

#     WARNING: This will override the configuration file."""
#     assert get('a', 3) == 3
#     set('b', 5)
#     assert get('b', 1) == 5
#     set('a', 9)
#     save()
#     get('a', 33)
#     get('b', 33)
#     load()
#     assert get('a', 2) == 9
#     get('c', 21) # The file should now contain 'c': 21
#     print("Check that the configuration file contains the key-value pair 'c': 21")
