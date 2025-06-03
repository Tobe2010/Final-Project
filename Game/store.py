# This file is for using the store

import db_functions as db

# buys one extra life for the user
def buyALife(name):
    if db.queryScoreForUser(name) >= 100:
        db.updateScoreForUser(name, -100)
        db.addLivesForUser(name)
        print('Purchase completed!')
        return
    else:
        print('You don\'t have enough points to complete this purchase!')
        return

# changes the ball color for the user
def setColor(name):
    if db.queryScoreForUser(name) >= 10:
        db.updateScoreForUser(name, -10)
        
        red = -1
        while int(red) < 0 or int(red) > 255:
            print('Please choose a number between 0-255 for the red value:')
            red = input()
        
        green = -1
        while int(green) < 0 or int(green) > 255:
            print('Please choose a number between 0-255 for the green value:')
            green = input()
        
        blue = -1
        while int(blue) < 0 or int(blue) > 255:
            print('Please choose a number between 0-255 for the blue value:')
            blue = input()
        
        db.setRed(name, red)
        db.setGreen(name, green)
        db.setBlue(name, blue)
        return
    else:
        print('You don\'t have enough points to complete this purchase!')
        return
    
# purchase for score multiplier, price and multiplier double every purchase.
def upgradeMultiplier(name):
    if db.queryScoreForUser(name) >= 10 * db.getUserMultiply(name):
        db.updateScoreForUser(name, -10 * db.getUserMultiply(name))
        db.upgradeUserMultiply(name)
        print('Purchase completed!')
        return
    else:
        print('You don\'t have enough points to complete this purchase!')
        return

# user shop function
def shop(name):

    '''
    THE COLLISION CHECKS IN game.py DID NOT ALLOW FOR THE LIVES TO WORK
    print('Would you like to purchase an extra life for 100 points? (y/n)')
    userWantsLife = input()
    if userWantsLife == 'y' or userWantsLife == 'Y':
        buyALife(name)
    '''

    print('Would you like to change the ball color for 10 points? (y/n)')
    userWantsColor = input()
    if userWantsColor == 'y' or userWantsColor == 'Y':
        setColor(name)

    print('Would you like to multiply earned points by 2x for ' + str(db.getUserMultiply(name) * 10) + ' points? (y/n)')
    userWantsMult = input()
    if userWantsMult == 'y' or userWantsMult == 'Y':
        upgradeMultiplier(name)
    
    print('Would you like to exit the shop? (y/n)')
    exitShop = input()
    if exitShop == 'n' or exitShop == 'N':
        shop(name)
