# To-Do:    1. code polish (this is the rough version!)
#           2. look for text and then execute action (no image croping as it is in [sc2actions.py])
#           3. support dynamic window size in the application (not fixed size as it is currently 1920x1080) [sc2utils.py]
from sc2utils import *
from sc2actions import *
from globals import *

import time

#
# Application state
#
def checkApplicationState(windowName):
    # check if game is alive
    if GetApplicationWindow(windowName, localCapture) == False:
        return False
    else:
        return True

#
# Check in which state game is!
#
def sc2CheckGameState(cvImg):

    if checkApplicationState(windowName):
        cvImg = cv2.imread(localCapture, cv2.IMREAD_UNCHANGED)     

    # set up gamestate
    frame = cvImg.copy()                # copy buffer
    gamestate = -1

    if sc2InMainMenuStatus(frame):
        gamestate = 1                   # we are in main menu
        if sc2InScoreScreen(frame):
            gamestate = 2               # we are in score screen
        if sc2SearchStatus(frame):
            gamestate = 3               # we are searching matchup
        if sc2MainMenuSubMenu(frame):
            gamestate = 6               # we have main menu submenu on screen
    else:
        if sc2InMapLoadStatus(frame):
            gamestate = 4               # we are in map load
        if sc2InGameStatus(frame):
            gamestate = 5               # we are in game
            if sc2InGameVictory(frame):
                gamestate = 7           # we are in victory screen
            
    return gamestate

#
# Main
#
if __name__ == '__main__':

    # set global variables
    have_application = False
    is_prepareVersus = True
    gamestate = 0

    # infinite loop
    while True:
        
        # do we have active application present?
        # if we dont have, we will be stucked in infinite loop and looking for that application
        have_application = checkApplicationState(windowName)
        if have_application == False:
            while have_application != False:
                print("Game Status: Looking for: " + windowName)
                have_application = checkApplicationState(windowName)

        # point to active application
        MouseAutoClick(1,1) 

        # open captured frame from application
        cvImg = cv2.imread(localCapture, cv2.IMREAD_UNCHANGED)       

        # get application game state
        gamestate = sc2CheckGameState(cvImg)

        # we are in score screen
        if gamestate == 2:
            print("Game Status: Is in Score Screen!")
            while True:
                gamestate = sc2CheckGameState(cvImg)
                if gamestate != 2:
                    break
                else:
                    time.sleep(generalTimeDelay)
                    MouseAutoClick(426,875) # click on play again

        # we are somewhere in main menu
        if gamestate == 1:
            print("Game Status: Somewhere In Main Menu!")
            while True:
                gamestate = sc2CheckGameState(cvImg)
                if gamestate != 1:
                    break
                else:
                    if is_prepareVersus:
                        sc2PrepareVersus(modeSelect, raceSelect, matchupSelect)
                        is_prepareVersus = False

        # we are searching matchup
        if gamestate == 3:
            print("Game Status: Is Searching Matchup!")
            while True:
                gamestate = sc2CheckGameState(cvImg)
                if gamestate != 3:
                    is_prepareVersus = True
                    break
 
        # we are loading map
        if gamestate == 4:
            print("Game Status: Is Loading Map!") 
            while True:
                gamestate = sc2CheckGameState(cvImg)
                if gamestate != 4:
                    break

        # we are in the game!
        if gamestate == 5:
            print("Game Status: Is In Game!")
            while True:
                time.sleep(generalTimeDelay)
                press('F10', 'n')
                time.sleep(generalTimeDelay)

                gamestate = sc2CheckGameState(cvImg)
                if gamestate != 5:
                    break

        # we have called submenu in game
        if gamestate == 6:
            print("Game Status: In Main Menu (Sub Menu Called)!")
            while True:
                press('esc')
                time.sleep(generalTimeDelay)

                gamestate = sc2CheckGameState(cvImg)
                if gamestate != 6:
                    break

        # we are in victory screen - enemy player left earlier than us
        if gamestate == 7:
            print("Game Status: In Game Victory Screen (oopise)!")
            while True:
                press('s')
                time.sleep(generalTimeDelay)

                gamestate = sc2CheckGameState(cvImg)
                if gamestate != 7:
                    break