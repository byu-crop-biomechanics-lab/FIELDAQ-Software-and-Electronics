# Top Directory
The program is ran from this directory using the the following command. 
```
python3 main.py
```
Be sure that the virtual environment has been activated from the Top level directory before running this command. You can activate it from this directory by running the following the command. 
```
source ../../myenv/bin/activate
```
The ModeSelect file is also located in this top Directory due to all the other devices being dependent on this screen.

# Devices 
There are currently 4 devices supported by this system (Arm, Camera, Darling, Rodney). When a user selects a device the corresponding Kivy files are imported into the screen manager. All 4 of these devices are based on the original darling software. Kivy requires that each screen has a unique name. This is why you will see a 3 letter prefix added to each device file due to many of the files being replicated across devices. These files needed to be replicated because the lab wanted to keep the devices completly independent of one another. 

## Devices sub-directories 
* **Data:** This holds the python files that are using for calculating / processing the data but they don't have a corresponding screen attached.<br>

* **Screns**: This directory holds all the source code for the graphics. The .kv files decide the layout of the screen while the corresponding .py file holds the control for the screen for things like what to do when the screen is entered, during operation and what to do when leaving the screen. There is a UML flow diagram stored under the labs Lucid chart account. The easiest way to find which screen you are looking at on the device is to follow this diagram as you click through the screens. <br>
   * **DatatCollection**: This sub-directory holds all the screens that are used when the Data Collection button is pressed from the main menu. 
   * **Settings**: This sub_directory holds all the screens that are used when the settings button is pressed from the main menu.<br>

* **Sensors**: This hold all the sensor interface files. It is also where the device decides to use real or fake data based on whether or not the device is found. 

* **Settings**: This holds the configuration settings for the system. Upon start up the system creates a config.json file where all settings are stored, such as the operator, folder and so forth. You will see in the code where we are pulling and writing data to this file.

# PubSub:
This was built as a why to allow prcesses to communicated with eachother throught the publisher subscriber model. This is not currently being implemented in the main system however can be used in future work if it is decided that the system is to slow and we want it to run on multiple cores. 

# Util
There are several kivy widgets that are used across all devices. These base models are stored here to be referenced by the other projects. They are not the specific widgets on the screens however they are inherited from to build the current screens. 

# TODO: 
1. Fix the option to see the contents of a file from the device. It attempts to re-graph the data. However when we changed the variable names and set up of the strain gauges it caused this build process to fail. To fix this I would look under the darling device to see how they did it. Then come back to the rodney, find the new variable names and match what they did. 

2. Exporting to USB. This function does currently work if you go through "Select location" and find the USB plugged in under the media directory. The save to USB button was hardcoded all over the project by the previous lab and the path that it's using is no longer valid. It goes through the /mount folder however the PI now stores USB devices under /media. So to fix this these hard coded paths need to be changed or you can remove that button and just have the "Select location" option start in the /media folder. 

3. Update with USB button has the same issue as noted in problem 2. I personally would just remove this button. The update with github button now works and is much simpler. As long as you have a valid WIFI connection the device will update everything with just a click of a button. NOTE: THe byuwifi, doesn't work on the PI. It appears to severely limit what traffic is allowed. You will need to use edu roam while on campus. I've added an example below on how to connect to edu roam from a PI. 
![alt text](EDUROAM.png)





