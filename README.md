# sc2leavebot
StarCraft 2 Leave Bot utilizing OpenCV, Tesseract-OCR and Win32 API

# How it works?
The principle of this Python script is pretty simple. The script will basically grab image frame from the application (utilizing python win32 API), then it looks for specific regions, something like the area of interests in the image (utilizing OpenCV) and if it is able to detect string information (utilizing tesseract OCR), then the action is called.

This script won't read anything from application process memory, it is not working on any kind of injection method or something similar to it. It is more likely trying to simulate and execute what "human eyes" see, in this case, what is on the display screen.

# What i would like to add/or fix in future!
- faster application snapshot grabber!
- setup application run scenario using parameters
    - matchup, race, mode
    - what is a goal for final (dropped) MMR?
- proper detection method and mouse pointing, area selection (instead of hard-coded, here you go mouse (x,y coords)!)
- detail gathering of information like:
    - profile player
        - mmr 
    - matchup map load screen
        - player names
        - map name
        - map snapshot
    - in game
        - gather chat log
    - score screen
        - map name
        - lenght of a game - timer
        - Base MMR of both players (or team)
        - decrease or increase of MMR of players (or team)
- do you have any additional ideas?

# Installation

## Basic packages
- Install latest Python 3.8.3 [64-bit](https://www.python.org/ftp/python/3.8.3/python-3.8.3-amd64.exe) or [32-bit](https://www.python.org/ftp/python/3.8.3/python-3.8.3.exe)
-- Do not forget add Python into your PATH!
- Install latest Tesseract OCR (tesseract-ocr-w32-setup-v5.0.0-alpha) [64-bit](https://digi.bib.uni-mannheim.de/tesseract/tesseract-ocr-w64-setup-v5.0.0-alpha.20200328.exe) or [32-bit](https://digi.bib.uni-mannheim.de/tesseract/tesseract-ocr-w32-setup-v5.0.0-alpha.20200328.exe)
## Python Modules
After installing Python and Tesseract OCR we need to fetch a few packages via pip, start your command line 

```python -m pip install --upgrade pip ``` -- this will upgrade your pip

```pip install pywin32``` -- install WIN32 API support for python

```pip install win32gui``` -- install WIN32 API GUI support for python

```pip install opencv-python``` -- install opencv for python

```pip install pytesseract``` -- install tesseract-ocr for python

## Execution / Run script
1. Run StarCraft II
2. Wait for game come up to Main Screen (after Login Screen) and run
```python main.py```

## Modfiication of Variables
Just open globals.py in text editor and edit it depending your needs!
