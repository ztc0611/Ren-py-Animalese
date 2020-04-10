# Ren'py version Readme
## Files that must be moved into another project in order to function:

-The full "pydub" folder
-the full "audio" folder
-The character callbacks in script.rpy, modified for the names of your own characters.
-speak.rpy

Enjoy making your own samples and using this Animalese generator in your projects!

IMPORTANT NOTE: TEXT SPEED (IN OPTIONS.RPY) MUST BE MODIFIED FROM INSTANT (AKA NOT EQUAL TO 0) FOR THIS TO WORK IN OTHER PROJECTS.

## Credits: 
Created by Henry from harryishuman, for his "How to speak Animalese" video: https://youtu.be/IKMjg2fEGgE (Modified and reposted with his explicit permission), Also the source of the audio samples.
Modified for Ren'py by CoolerMudkip/Zach Coleman.

===============================================================================

#Original Readme was as follows:

## What is this?
The "animalese.py" script, is a Python script intended to emulate the vocalisations of characters from the Animal Crossing series.

## Installation
In order to run this script, you will need to install Python, available from the following website: https://www.python.org/downloads/

When installing, make sure you check the box asking to add python to your $PATH variable (otherwise this will have to be done manually!).

Once Python is installed, you will require the following additional packages for Python:
- wave
- pydub

To install these files, open the command prompt:
- On Windows:
    - Press Window Key + R
    - Type in "cmd"
    - Hit ENTER
- On iOS:
    - Press Command Key + Space
    - Type in "terminal"
    - Hit ENTER

Once this window is open, type the following commands:
```bash
    pip install wave
    pip install pydub
```

## How to use
Once Python has been installed, along with the required packages, you can run the script in one of two ways:
- From command line/terminal:
    - Navigate to the same directory of animalese.py script.
    - Run the command:
        ```bash
            ./animalese.py "Text you wish to hear."
        ```
- By editing and double clicking on the file:
    - Open the file, and alter the "Hello world!" message on like 78 to the text you wish to hear.
    - Double click on the "animalese.py" file. 

## Notes
This software was created by Henry (henryishuman).
Feel free to use and modify at your own discretion.
