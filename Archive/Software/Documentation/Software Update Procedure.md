## Performing a Software Update on the Device

### Method 1: Load files onto USB stick and move files
1. Format a flash drive to use the FAT file system. This can be done on Windows or on a Mac; look this up online if you're not sure how to do it.
2. Download latest files from this github repository. https://github.com/byu-crop-biomechanics-lab/FIELDAQ/archive/refs/heads/master.zip
3. Unzip the downloaded files and put them on the flash drive. The files should be in a folder named "FIELDAQ" in the root directory of the flash drive, meaning the first thing you should see when you open the flash drive is the folder "FIELDAQ" with "Documentation", "Granusoft", etc. inside that folder.
4. Plug the flash drive into the FIELDAQ device and power it on.
5. Once the main screen has loaded, exit it. You should see a command window once you've exited the main screen.
6. We now needs to run some commands in this command window. This can be done three different ways, but only needs to be done once so pick whichever method is easiest for you:
- Scan this qr code with a barcode scanner. If your barcode scanner is set up to scan qr codes then this code will run all the commands we need at once.

![alt text](https://github.com/byu-crop-biomechanics-lab/FIELDAQ/blob/master/Documentation/USB_update_command.png)

- Plug in a keyboard and type out the following list of commands in the order they are listed. Make sure to type in the commands EXACLTLY as listed and hit enter once done. Give each command a few seconds to finish before doing the next one.

```sudo mount -t vfat -o uid=pi,gid=pi /dev/sda1 /mnt/usbStick```

```sudo cp -r /mnt/usbStick/FIELDAQ ~/```

```sudo umount /mnt/usbStick```

```python3 main.py```

- If you are running software version 2.3.0 or later (the main screen shows the software version) then there is a button in the settings that will run these commands for you. Simply go to the settings page and press "Update with USB".
7. The software will then reboot and should now be updated. If it updated properly then the version number should show the latest version number on the main page (latest version is 2.3.0 at time of writing).

### Method 2: Connecting to internet and pulling changes directly from github (Outdated)
1. Enter the command line on the pi device. The granusoft box interface can be exited on the main screen by selecting "Exit", then "Exit" again.
2. Plug in a USB keyboard. (SSH can also be used, but a keyboard is easier and this guide will assume you are using a keyboard.)
3. Connect the device to internet. This can usually be done by running "sudo raspi-config" and using the menu that provides. If more instructions
   are needed, refer to: https://www.raspberrypi.org/documentation/configuration/wireless/wireless-cli.md
   You can also use an ethernet cable instead of a wireless connection.
4. Ensure you are in the FIELDAQ file directory. The command line will list your current directory. It should say ```~/FIELDAQ/Granusoft/src```
   If you just exited the granusoft software then you should already be in the correct directory.
   If you are not in the correct directory, type ```cd ~/FIELDAQ/Granusoft/src```
5. Type ```git pull``` into the command line. This will download the latest update onto your device.
6. The device is now updated! You can enter the updated software by either turning the device off and on again or running the command ```python3 main.py```
