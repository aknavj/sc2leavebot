from globals import *
from sc2utils import *
from cv2 import *

import pytesseract
import time

# setup tesseract
pytesseract.pytesseract.tesseract_cmd = tesseractPath

#
#   Crop area display and detect what is on the screen - return as string
#
def sc2CropDetectMethod(cvImg, x1, y1, x2, y2):
    copy = cvImg.copy()
    refPoint = [(x1, y1), (x2, y2)]

    source = copy[refPoint[0][1]:refPoint[1][1], refPoint[0][0]:refPoint[1][0]]
    tess_source = cv2.cvtColor(source, cv2.COLOR_BGR2RGB)
    tess_source_str = pytesseract.image_to_string(tess_source)
    return str(tess_source_str or '')

#
# Prepare Versus Mode
#
def sc2PrepareVersus(modeSelect, raceSelect, matchupSelect):

    print("Game Status: In Main Menu - Prepare Versus Mode:")

    # reset mouse pos
    MouseAutoClick(0, 0)

    # versus mode
    MouseAutoClick(477,44)

    ######################
    # mode select
    ######################
    line_y = 97
    if (modeSelect == '1v1' or modeSelect == '1V1'):
        MouseAutoClick(404, line_y) # 1v1 only
    else:
        MouseAutoClick(322, line_y) # click on teams

    line_y = 503
    if (modeSelect == 'archon' or modeSelect == 'ARCHON'):
        MouseAutoClick(360,line_y)

    if (modeSelect == '2v2' or modeSelect == '2V2'):
        MouseAutoClick(487,line_y)

    if (modeSelect == '3v3' or modeSelect == '3V3'):
        MouseAutoClick(616,line_y)

    if (modeSelect == '4v4' or modeSelect == '4V4'):
        MouseAutoClick(743, line_y)   
    print("\tMode: " + modeSelect)

    ######################
    # race select
    ######################
    time.sleep(1)
    line_y = 344
    if (raceSelect == 'terran' or raceSelect == 'TERRAN'):
        MouseAutoClick(174, line_y)

    if (raceSelect == 'zerg' or raceSelect == 'ZERG'):
        MouseAutoClick(356, line_y)

    if (raceSelect == 'protoss' or raceSelect == 'PROTOSS'):
        MouseAutoClick(533, line_y)

    if (raceSelect == 'random' or raceSelect == 'RANDOM'):
        MouseAutoClick(718, line_y)
    print("\tRace: " + raceSelect)
    
    ######################
    # matchup select
    ######################
    time.sleep(1.5)
    line_y = 964
    if (matchupSelect == 'ranked' or matchupSelect == 'RANKED'):
        MouseAutoClick(218, line_y)

    if (matchupSelect == 'unranked' or matchupSelect == 'UNRANKED'):
        MouseAutoClick(497, line_y)
    print("\tMatchup: " + matchupSelect)

#
# Score screen Detection
# Play Again (Search Status Queue)
#
def sc2InScoreScreen(cvImg):
    str = sc2CropDetectMethod(cvImg, 293, 88, 530, 122)
    if 'DEFEAT!' in str:
        return True
    if 'VICTORY!' in str:
        return True
    return False
    
#
# Loading Screen Area (Map name) + (Our Player Name) + (Enemy Player Name)
# currently supported only 1v1!
#
def sc2InMapLoadStatus(cvImg):
    str = sc2CropDetectMethod(cvImg, 702, 685, 1236, 744)
    if str != "":
        return True
    return False
#
# In Game Detection (looking for TIMER!)
#
def sc2InGameStatus(cvImg):
    str = sc2CropDetectMethod(cvImg, 269, 749, 331, 798)
    if str:
        #if use_debug:
        #    print("sc2InGameStatus(): Timer " + str)
        return True
    return False
#
# Campain Button -> indicates we are in Main Menu
#
def sc2InMainMenuStatus(cvImg):
    str = sc2CropDetectMethod(cvImg, 74, 0, 267, 64)
    if 'CAMPAIGN' in str:
        return True
    return False
#
# Search Matchup
#
def sc2SearchStatus(cvImg):
    str = sc2CropDetectMethod(cvImg, 181, 1020, 430, 1038)
    if 'INITIALIZING' in str:
        return True
    if 'SEARCHING' in str:
        return True
    if 'GAME' in str:
        return True
    return False
#
# Main Menu (Sub Menu)
#
def sc2MainMenuSubMenu(cvImg):
    str = sc2CropDetectMethod(cvImg, 800, 328, 1117, 823)
    if 'options' in str:
        return True
    return False

#
# Victory Screen (oopsie!)
#
def sc2InGameVictory(cvImg):
    str = sc2CropDetectMethod(cvImg, 743, 227, 1169, 281)
    if 'VICTORY!' in str:
        return True
    return False