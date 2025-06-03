# This file is for starting the game and accessing the shop

import db_functions as db
import time
import store

# This function checks if the user wishes to open the shop
def shopOpened(name):
    print('Would you like to open the shop? (y/n)')
    shopOpen = input()
    if shopOpen == 'Y' or shopOpen == 'y' or shopOpen == 'Yes' or shopOpen == 'yes':
        store.shop(name)
        return
    elif shopOpen == 'N' or shopOpen == 'n' or shopOpen == 'No' or shopOpen == 'no':
        return
    else:
        return

# this function checks if the user wishes to start the game
def startedGame():
    print('Please enter "s" to start the game')
    startGame = input()
    if startGame == 's' or startGame == 'S':
        return
    else:
        startedGame()

# this is the main function to initialize the game
def gameInit():
    print('\nWelcome to Flying Ball!\n')
    time.sleep(2)

    print('To play the game, press SPACE to navigate the ball through the columns. \nBut watch out, If you collide with a column, you\'re out!\n')
    time.sleep(6)

    print('First, please tell us your name:')
    name = input()

    if db.checkExists(name):
        print('\nWelcome back, ' + name + '! Your current score is ' + str(db.queryScoreForUser(name)) + '.\n')
        time.sleep(3)
        shopOpened(name)
    else:
        print('It appears that this is your first time playing the game, welcome!')
        time.sleep(4)

    startedGame()
    
    return name
