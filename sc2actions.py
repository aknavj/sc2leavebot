from sc2utils import *
from cv2 import *
import pytesseract
import time

pytesseract.pytesseract.tesseract_cmd = "C:\\Program Files (x86)\\Tesseract-OCR\\tesseract.exe"

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
    play_again_crop = cvImg[88:122, 293:530]
    tess_play_again = cv2.cvtColor(play_again_crop, cv2.COLOR_BGR2RGB)
    tess_play_again_str = pytesseract.image_to_string(tess_play_again)

    if 'DEFEAT!' in tess_play_again_str:
        return True

    if 'VICTORY!' in tess_play_again_str:
        return True

    return False
#
# Loading Screen Area (Map name) + (Our Player Name) + (Enemy Player Name)
# currently supported only 1v1!
#
def sc2InMapLoadStatus(cvImg):
    mapname_crop = cvImg[685:744, 702:1236]
    tess_mapname = cv2.cvtColor(mapname_crop, cv2.COLOR_BGR2RGB)
    tess_mapname_str = pytesseract.image_to_string(tess_mapname)

    if tess_mapname_str != "":
        map_crop = cvImg[202:640,751:1167]

        player1_crop = cvImg[449:467,256:511]
        tess_player1 = cv2.cvtColor(player1_crop, cv2.COLOR_BGR2RGB)
        tess_player1_str = pytesseract.image_to_string(tess_player1)

        player2_crop = cvImg[449:467,1416:1671]
        tess_player2 = cv2.cvtColor(player2_crop, cv2.COLOR_BGR2RGB)
        tess_player2_str = pytesseract.image_to_string(tess_player2)

        #if use_debug:
        #    print(tess_player1_str + " versus " + tess_player2_str + " on: " + tess_mapname_str)
        
        return True

    return False
#
# In Game Detection (looking for TIMER!)
#
def sc2InGameStatus(cvImg):
    ingame_timer_crop = cvImg[749:798, 269:331]
    tess_ingame_timer = cv2.cvtColor(ingame_timer_crop, cv2.COLOR_BGR2RGB)
    tess_ingame_timer_str = pytesseract.image_to_string(tess_ingame_timer)

    if tess_ingame_timer_str:
        #if use_debug:
        #    print("sc2InGameStatus(): Timer " + tess_ingame_timer_str)
        
        return True

    return False
#
# Campain Button -> indicates we are in Main Menu
#
def sc2InMainMenuStatus(cvImg):
    menu_crop = cvImg[0:64, 74:267] 
    tess_menu = cv2.cvtColor(menu_crop, cv2.COLOR_BGR2RGB)
    tess_menu_str = pytesseract.image_to_string(tess_menu)

    if 'CAMPAIGN' in tess_menu_str:
        return True

    return False
#
# Search Matchup
#
def sc2SearchStatus(cvImg):
    # Search Status
    search_crop = cvImg[1020:1038, 181:430] 
    tess_search = cv2.cvtColor(search_crop, cv2.COLOR_BGR2RGB)
    tess_search_str = pytesseract.image_to_string(tess_search)

    if 'INITIALIZING' in tess_search_str:
        return True

    if 'SEARCHING' in tess_search_str:
        return True

    if 'GAME' in tess_search_str:
        return True

    return False
#
# Main Menu (Sub Menu)
#
def sc2MainMenuSubMenu(cvImg):
    submainmenu_crop = cvImg[328:823, 800:1117] 
    tess_submainmenu = cv2.cvtColor(submainmenu_crop, cv2.COLOR_BGR2RGB)
    tess_submainmenu_str = pytesseract.image_to_string(tess_submainmenu)

    if 'options' in tess_submainmenu_str:
        return True

    return False

#
# Victory Screen (oopsie!)
#
def sc2InGameVictory(frame):
    victory_crop = cvImg[227:281, 743:1169] 
    tess_victory = cv2.cvtColor(victory_crop, cv2.COLOR_BGR2RGB)
    tess_victory_str = pytesseract.image_to_string(tess_victory)

    if 'VICTORY!' in tess_victory_str:
        return True

    return False
