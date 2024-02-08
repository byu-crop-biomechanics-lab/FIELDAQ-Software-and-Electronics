# FIELDAQ

## TODO 
Fix the Rename function in the fodler system 

## Overview and Resources
The software for the FIELDAQ is written in python, using the kivy library. Versioning is managed using git via GitHub. The layout and functionality are based on the old DARLING software. With the addition of a touchscreen, kivy was utilized over pygame.

- [Resources for Python](https://www.python.org/about/gettingstarted/)
- Resources for kivy can be found in [Documentation/Kivy Training Resources](https://github.com/pr1ce1227/REAPER/blob/main/Documentation/Kivy%20Training%20Resources.docx)
- [Resources for git](https://guides.github.com/introduction/git-handbook/)
  - [The old DARLING repository](https://github.com/byu-crop-biomechanics-lab/DARLING_Software.git)

## Running the Software
Run the following commands in a bash terminal to download, build and run the projcet. This build script will build a python environment and download the necessary packages. It then will build the project and run it to verify that everything is working correctly. 
```
git clone git@github.com:byu-crop-biomechanics-lab/FIELDAQ-Software-and-Electronics.git
cd FIELDAQ-Software-and-Electronics/
source build_project
```

After installing python and the nessesary [libraries](https://github.com/pr1ce1227/REAPER/blob/main/libraries.txt), the software is run by navigating into the [Granusoft/src](https://github.com/pr1ce1227/REAPER/tree/main/Granusoft/src) directory and running the [main.py](https://github.com/pr1ce1227/REAPER/blob/main/Granusoft/src/main.py) file.

The [main.py](https://github.com/byu-crop-biomechanics-lab/FIELDAQ/blob/master/Granusoft/src/main.py) file imports the necessary kivy library elements, and builds the kivy app. The companion [main.kv](https://github.com/pr1ce1227/REAPER/blob/main/Granusoft/src/main.kv) file imports the widgets (GUI screen elements), created for the use across the GUI, and imports the views that will be displayed throughout the app. These views are each composed of a python file and kivy file. More detail can be found in [Documentation/Kivy Screen Management.docx](https://github.com/pr1ce1227/REAPER/blob/main/Documentation/Kivy%20Screen%20Management.docx).

## Documentation Directory
The Documentation directory contains many useful files, some of which have been mentioned previously. Documentation that has been found to be the most useful is listed here:
- [Setup Software for Non-RPi Computers.txt](https://github.com/pr1ce1227/REAPER/blob/main/Documentation/Setup%20Software%20for%20Non-RPi%20Computers.txt) -  Information on how to get the GUI running on a non-RaspberryPi computer for software development.
- [Software Update Procedure.md](https://github.com/pr1ce1227/REAPER/blob/main/Documentation/Software%20Update%20Procedure.md) - Information on how to utilize a USB drive or Github when updating the on-device software.
- [FIELDAQ_Software_Diagrams.pdf](https://github.com/pr1ce1227/REAPER/blob/main/Documentation/FIELDAQ_Software_Diagrams.pdf) - Information about the screen navigation for the GUI and how each screen is built using kivy elements/widgets (flowchart is outdated).
- [Example_Adding the Camera Module.docx](https://github.com/pr1ce1227/REAPER/blob/main/Documentation/Example_Adding%20the%20Camera%20Module.docx) - A reflection on how the camera screens were added.
- [Example_Adding a Boot Screen.docx](https://github.com/pr1ce1227/REAPER/blob/main/Documentation/Example_Adding%20a%20Boot%20Screen.docx) - A hypothetical situation where a boot screen is created to choose between the Camera test mode and the Stalk Push testing mode.


Additionaly, a brief overview of all the documentation is provide here:
### Structural Information of the Code Base (how is it assembled)
- [Directory Tree.txt](https://github.com/pr1ce1227/REAPER/blob/main/Documentation/Directory%20Tree.txt) -  Overview of the directories in the repository. With information about the contents of each directory.
- [FIELDAQ_Software_Diagrams.pdf](https://github.com/pr1ce1227/REAPER/blob/main/Documentation/FIELDAQ_Software_Diagrams.pdf) - 	Information about the screen navigation for the GUI and how each screen is built using kivy elements/widgets (flowchart is outdated).
- [Software Flowchart and Logic.docx](https://github.com/pr1ce1227/REAPER/blob/main/Documentation/Software%20Flowchart%20and%20Logic.docx) - 	Supplementary to FIELDAQ_Software_Diagrams, this document contains more information about the purpose of each screen.
- [Software Documentation Outdated.pdf](https://github.com/pr1ce1227/REAPER/blob/main/Documentation/Software%20Documentation%20Outdated.pdf) - 	An old resource containing the Classes and Methods contained in every file. This was last updated at the end of capstone, and may contain some useful information still. An updated version can be compiled using [DoxyGen](https://www.doxygen.nl/index.html) (version. 1.8.15).
### Background Information (how do the pieces work)
- [Kivy Screen Management.docx](https://github.com/pr1ce1227/REAPER/blob/main/Documentation/Kivy%20Screen%20Management.docx) - 	Information on how kivy navigates between screens and how screens can be added to the GUI.
- [Kivy Training Resources.docx](https://github.com/pr1ce1227/REAPER/blob/main/Documentation/Kivy%20Training%20Resources.docx) - 	A list of resources on how to learn kivy for those who are unfamiliar with the libraries.
- [Setup Software for Non-RPi Computers.txt](https://github.com/pr1ce1227/REAPER/blob/main/Documentation/Setup%20Software%20for%20Non-RPi%20Computers.txt) -  Information on how to get the GUI running on a non-RaspberryPi computer for software development.
- [Software Coding Standard.docx](https://github.com/pr1ce1227/REAPER/blob/main/Documentation/Software%20Coding%20Standard.docx) -	The Coding Standard for coding used throughout the software.
- [Software Update Procedure.md](https://github.com/pr1ce1227/REAPER/blob/main/Documentation/Software%20Update%20Procedure.md) - 	Information on how to utilize GitHub when updating the on-device software.
- Supplementary Directory:
  - [Kivy Clock Summary.docx](https://github.com/pr1ce1227/REAPER/blob/main/Documentation/Supplementary/Kivy%20Clock%20Summary.docx) - 	Information recorded by the capstone team about the logic for using the clock the way they did.
  - [Raspberry Pi Setup.docx](https://github.com/pr1ce1227/REAPER/blob/main/Documentation/Supplementary/Raspberry%20Pi%20Setup.docx) - 	Information on how to set up a new raspberry pi from scratch to host the software.
### Examples
- [Example_Adding the Camera Module.docx](https://github.com/pr1ce1227/REAPER/blob/main/Documentation/Example_Adding%20the%20Camera%20Module.docx) - A reflection on how the camera screens were added.
- [Example_Adding a Boot Screen.docx](https://github.com/pr1ce1227/REAPER/blob/main/Documentation/Example_Adding%20a%20Boot%20Screen.docx) - A hypothetical situation where a boot screen is created to choose between the Camera test mode and the Stalk Push testing mode.
