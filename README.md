# Rune-inator

A simple python script that takes runes from https://www.murderbridge.com (for ARAMs) and configures the runes in the League of Legends client.

## TODOs

Note that currently it only supports clients of size 1280x720. To support other sizes the positions and the GridView.png image need to be scaled.

![Window size set to 1280x720](./images/ClientSize.PNG)

## Requirements
First you need to download python3 from https://www.python.org/downloads/ 

You will need to install the following modules using pip. For windows the commands look like: 
  - C:\Users\YourUsername\AppData\Local\Programs\Python\Python39>python.exe -m pip install requests-html
  - C:\Users\YourUsername\AppData\Local\Programs\Python\Python39>python.exe -m pip install pyautogui
  - C:\Users\YourUsername\AppData\Local\Programs\Python\Python39>python.exe -m pip install Pillow
  - C:\Users\YourUsername\AppData\Local\Programs\Python\Python39>python.exe -m pip install opencv-python

## Running the script
To run the script, navigate to where you have python installed and run the "rune-inator.py" script:

```C:\Users\YourUsername\AppData\Local\Programs\Python\Python39>python.exe C:\Users\YourUsername\Rune-inator\rune-inator.py```

## Example
These were the recommended runes for Lux: ![LuxRunes](./images/MurderBridgeLuxRunes.PNG)

Here is the script running(Note there is a dialog when starting the script to input the name of the champion, that dialog was not recorded):
[Link to imgur](https://i.imgur.com/Kl5Cnau.mp4)
