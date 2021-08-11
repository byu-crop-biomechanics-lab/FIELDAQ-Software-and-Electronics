## Performing a Software Update on the Device

### Method 1: Load files onto USB stick and move files
1. Format a flash drive to use the FAT file system. Look this up online if you're not sure how to do this.
2. Download latest files from this github page. This is done by going to the main page, clicking the green button that says "code" and clicking "download zip".
3. Unzip the downloaded files and put them on the flash drive. The files should be in a folder named "FIELDAQ" in the root directory of the flash drive, meaning the first thing you should see when you open the flash drive is the folder "FIELDAQ" with "Documentation", "Granusoft", etc. inside that folder.
4. Plug the flash drive into the FIELDAQ device and power it on. 
5. Once the main screen has loaded, exit it. You should see a command window once you've exited the main screen. 
6. Run the following command ```sudo mount -t vfat -o uid=pi,gid=pi /dev/sda1 /mnt/usbStick/FIELDAQ && sudo rm ~/FIELDAQ -r && sudo mv /mnt/usbStick ~/FIELDAQ``` This can be done with a keyboard (it needs to be EXACT), or you can scan a qr code of the command if you have a barcode scanner able to scan barcodes. 
7. After waiting a few seconds, the device should have updated itself.

### Method 2: Connecting to internet and pulling changes directly from github
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
