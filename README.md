The software for the FIELDAQ is written in python, using the kivy library.

Resources for Python can be found at: https://www.python.org/about/gettingstarted/
Resources for kivy can be found in the file: Documentation/Kivy Training Resources.docx
			      OR at: https://kivy.org/doc/stable/gettingstarted/index.html

The software is run by navigating into the FIELDAQ/Granusoft/src directory and running the main.py file.

The main.py file imports the necessary kivy library elements, and builds the kivy app. The companion main.kv file imports the widgets (GUI screen elements), created for the use across the GUI, and imports the views that will be displayed throughout the app. These views are each composed of a python file and kivy file. More detail can be found in the file: Documentation/Kivy Screen Management.docx

