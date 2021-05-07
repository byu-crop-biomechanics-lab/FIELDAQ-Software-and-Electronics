# FIELDAQ

## Overview and Resources
The software for the FIELDAQ is written in python, using the kivy library. Versioning is managed using git via GitHub. The layout and functionality are based on the old DARLING software. With the addition of a touchscreen, kivy was utilized over pygame.

- Resources for Python can be found at: https://www.python.org/about/gettingstarted/
- Resources for kivy can be found in the file: Documentation/Kivy Training Resources.docx
  - OR at: https://kivy.org/doc/stable/gettingstarted/index.html
- Resources for git can be found at: https://guides.github.com/introduction/git-handbook/
  - The old DARLING repository is found at: https://github.com/byu-crop-biomechanics-lab/DARLING_Software.git

## Running the Software
The software is run by navigating into the FIELDAQ/Granusoft/src directory and running the main.py file.

The main.py file imports the necessary kivy library elements, and builds the kivy app. The companion main.kv file imports the widgets (GUI screen elements), created for the use across the GUI, and imports the views that will be displayed throughout the app. These views are each composed of a python file and kivy file. More detail can be found in the file: Documentation/Kivy Screen Management.docx

The software is designed to be run on the RaspberryPi, but can also be run on any computer with python3 and kivy. This approach is useful for development and testing purposes. The code is structured to use false sensor input data when the sensor connections can not be properly detected.

## Documentation Directory
The Documentation directory contains many useful files, some of which have been mentioned previously. A brief overview of these files is provide here:
### Structural Information of the Code Base (how is it assembled)
- Directory Tree.txt -  Overview of the directories in the repository. With information about the contents of each directory.
- FIELDAQ_Software_Diagrams.pdf - 	Information about the screen navigation for the GUI and how each screen is built using kivy elements/widgets.
- Software Flowchart and Logic.docx - 	Supplementary to FIELDAQ_Software_Diagrams, this document contains more information about the purpose of each screen.
- Software Documentation Outdated.pdf - 	An old resource containing the Classes and Methods contained in every file. This was last updated at the end of capstone, and may contain some useful information still. An updated version can be compiled using DoxyGen (version. 1.8.15).
### Background Information (how do the pieces work)
- Kivy Screen Management.docx - 	Information on how kivy navigates between screens and how screens can be added to the GUI.
- Kivy Training Resources.docx - 	A list of resources on how to learn kivy for those who are unfamiliar with the libraries.
- Setup Software for Non-RPi Computers.txt -  Information on how to get the GUI running on a non-RaspberryPi computer for software development.
- Software Coding Standard.docx -	The Coding Standard for coding used throughout the software.
- Software Update Procedure.txt - 	Information on how to utilize GitHub when updating the on-device software.
- Supplementary Directory:
  - Kivy Clock Summary.docx - 	Information recorded by the capstone team about the logic for using the clock the way they did.
  - Raspberry Pi Setup.docx - 	Information on how to set up a new raspberry pi from scratch to host the software.
### Examples
- Example_Adding the Camera Module.docx - A reflection on how the camera screens were added.
- Example_Adding a Boot Screen.docx - A hypothetical situation where a boot screen is created to choose between the Camera test mode and the Stalk Push testing mode.
### Plans for Future Changes and Improvements
- ...
