"""
The configurator module adds an interface to read to and write from the configuration
file ('config.json').  Reading and writing settings to the configuration file allows the
configuration to persist beyond the application lifecycle.
"""

import os
import json

CONFIG_FILE = 'config.json'

data = {}

def load():
    """Loads data from the configuration file, if it exists."""
    global data
    if os.path.isfile(CONFIG_FILE):
        with open(CONFIG_FILE) as f:
            data.update(json.load(f))
    else:
        data = {}

def load_from(filepath):
    '''Loads data from a specified configuration file.  Overwrites CONFIG_FILE'''
    global data
    if os.path.isfile(filepath):
        with open(filepath) as f:
            data.update(json.load(f))
            save()
    else:
        data = {}

def save():
    """Saves data to the configuration file."""
    with open(CONFIG_FILE, 'w') as outfile:
        json.dump(data, outfile, indent=4)

def save_as(filepath):
    '''Saves data to the specified file.'''
    with open(filepath, 'w') as outfile:
        json.dump(data, outfile, indent=4)

def set(key, value):
    """Set a key to value in the configuration JSON file."""
    # Set key to value
    data[key] = value
    save()

def get(key, default):
    """Get a value from the configuration JSON file using a key.  If the value does not
    exist, save the default value into the JSON file and return the default."""
    if key in data:
        return data.get(key)
    else:
        set(key, default)
        return default

if __name__ == "__main__":
    """If the configuration module is run as the main program, test the configuration
    module.  These tests ensure the module returns and saves the default value if a key
    is not defined, returns the saved value if a key is defined, and that the
    configuration file contains the values saved.

    WARNING: This will override the configuration file."""
    assert get('a', 3) == 3
    set('b', 5)
    assert get('b', 1) == 5
    set('a', 9)
    save()
    get('a', 33)
    get('b', 33)
    load()
    assert get('a', 2) == 9
    get('c', 21) # The file should now contain 'c': 21
    print("Check that the configuration file contains the key-value pair 'c': 21")
