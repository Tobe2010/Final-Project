# This file is for using the store

import db_functions as db
import time

def buyALife(name):
    if db.queryScoreForUser(name) >= 100:
        db.updateScoreForUser(name, -100)
        db.addLivesForUser(name)
        print('Purchase completed!')
        return
    else:
        print('You don\'t have enough points to complete this purchase!')
        return

def shop(name):
    print('Would you like to purchase an extra life for 100 points? (y/n)')
    userWantsLife = input()
    if userWantsLife == 'y' or userWantsLife == 'Y':
        buyALife(name)
    time.sleep(2)
    
    print('Would you like to exit the shop? (y/n)')
    exitShop = input()
    if exitShop == 'n' or exitShop == 'N':
        shop(name)
