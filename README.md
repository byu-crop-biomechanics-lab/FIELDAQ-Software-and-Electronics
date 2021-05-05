#FIELDAQ

## Overview and Resources
The software for the FIELDAQ is written in python, using the kivy library. Versioning is managed using git via GitHub.

Resources for Python can be found at: https://www.python.org/about/gettingstarted/
Resources for kivy can be found in the file: Documentation/Kivy Training Resources.docx
			      OR at: https://kivy.org/doc/stable/gettingstarted/index.html
Resources for git can be found at: https://guides.github.com/introduction/git-handbook/

## Running the Software
The software is run by navigating into the FIELDAQ/Granusoft/src directory and running the main.py file.

The main.py file imports the necessary kivy library elements, and builds the kivy app. The companion main.kv file imports the widgets (GUI screen elements), created for the use across the GUI, and imports the views that will be displayed throughout the app. These views are each composed of a python file and kivy file. More detail can be found in the file: Documentation/Kivy Screen Management.docx

##Documentation Directory
The Documentation directory contains many useful files, some of which have been mentioned previously. A brief overview of these files is provide here:
	FIELDAQ_Software_Diagrams.pdf - 	Information about the screen navigation for the GUI and how each screen is built using kivy elements/widgets.	Kivy Screen Management.docx - 	Information on how kivy navigates between screens and how screens can be added to the GUI.	Kivy Training Resources.docx - 	A list of resources on how to learn kivy for those who are unfamiliar with the libraries.	Software Coding Standard.docx -	The Coding Standard for coding used throughout the software.	Software Flowchart and Logic.docx - 	Supplementary to FIELDAQ_Software_Diagrams, this document contains more information about the purpose of each screen.	Software Update Procedure.txt - 	Information on how to utilize GitHub when updating the on-device software.	Supplementary Directory:		Kivy Clock Summary.docx - 	Information recorded by the capstone team about the logic for using the clock the way they did.		Raspberry Pi Setup.docx - 	Information on how to set up a new raspberry pi from scratch to host the software.		Software Documentation Outdated.pdf - 	An old resource containing the Classes and Methods contained in every file. This was last updated at the end of capstone, and may contain some useful information still.