# Cozmonitor
Use the Anki Cozmo as a monitor (mirrored) on pc.

# What is this?
Cozmonitor is a way to use the Anki Cozmo as a (mirrored) monitor through Python. It uses Pycozmo and pyautogui to get a screenshot, then set it to your cozmos screen, effectively acting as a monitor

# Requirements
Cozmonitor requires Python 3.12, Pycozmo, PyAutoGui, toml, and pillow.
To install the requirements, run this in the directory with cozmo.py
```
pip install -r requirements.txt
```

# Running
(Before you try running, make sure you have installed all requirements)
1. Connect to cozmos wifi on the computer your running
2. Run ```cozmo.py```
Thats it! If it worked, you should be looking at a (poorly rendered) version of your desktop/primary monitor!

# Other Info
* This has not been tested on any linux distro. If you are on linux, use this, and encounter errors, please make an issue about it
* You can change what fps it allows itself to go to in config.toml under Screenshots then fps (default is 60)
  
