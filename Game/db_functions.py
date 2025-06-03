# NOTE: I attempted to use single quotes when possible, but had to use double quotes when a single quote character had to be included in the SQL query/action

import sqlite3

# inserts data for a new player or updates to the score for an already existing user (void)
def insertData(playerName, playerScore):
       conn = sqlite3.connect('game_database.db')
       cursor = conn.cursor()
       
       if checkExists(playerName):
              updateScoreForUser(playerName, playerScore)
       else:
              cursor.execute('INSERT INTO SCORE_TABLE (playerName, playerScore, playerLives, red, green, blue, scMultiply) VALUES (?, ?, ?, ?, ?, ?, ?)', (playerName, playerScore, 0, 255, 0, 0, 1))
       
       conn.commit()
       conn.close()
      
# prints every row in the database (void)
def queryDB():
       conn = sqlite3.connect('game_database.db')
       cursor = conn.cursor()
       
       data = cursor.execute('SELECT * FROM SCORE_TABLE')
       for row in data:
              print(row)

       conn.close()
       
# returns the score for a specific username (int)
def queryScoreForUser(playerName):
       conn = sqlite3.connect('game_database.db')
       cursor = conn.cursor()
       
       cursor.execute("SELECT playerScore FROM SCORE_TABLE WHERE playerName = '" + playerName + "'")
       
       i = cursor.fetchone()
       
       conn.close()
       
       return i[0]

# adds to the score for a specific username (void)
def updateScoreForUser(playerName, newScore):
       conn = sqlite3.connect('game_database.db')
       cursor = conn.cursor()
       
       cursor.execute('UPDATE SCORE_TABLE SET playerScore = ' + str(newScore + queryScoreForUser(playerName)) + " WHERE playerName = '" + playerName + "'")
       
       conn.commit()
       conn.close()

# sets the score for a specific username (void)
def setScoreForUser(playerName, newScore):
       conn = sqlite3.connect('game_database.db')
       cursor = conn.cursor()
       
       cursor.execute('UPDATE SCORE_TABLE SET playerScore = ' + str(newScore) + " WHERE playerName = '" + playerName + "'")
       
       conn.commit()
       conn.close()
       
# checks if a user exists in the database (boolean)
def checkExists(playerName):
       conn = sqlite3.connect('game_database.db')
       cursor = conn.cursor()
       i = 0
       
       data = cursor.execute("SELECT playerName FROM SCORE_TABLE WHERE playerName = '" + playerName + "'")
       
       for row in data:
              i += 1
       
       conn.commit()
       conn.close()
       
       return (i != 0)

# returns the number of extra lives for a specific username (int)
def queryLivesForUser(playerName):
       conn = sqlite3.connect('game_database.db')
       cursor = conn.cursor()
       
       cursor.execute("SELECT playerLives FROM SCORE_TABLE WHERE playerName = '" + playerName + "'")
       
       i = cursor.fetchone()
       
       conn.close()
       
       return i[0]

# manually sets the number of lives for a user (primarily used in testing) (void)
def setLivesForUser(playerName, playerLives):
       conn = sqlite3.connect('game_database.db')
       cursor = conn.cursor()
       
       cursor.execute('UPDATE SCORE_TABLE SET playerLives = ' + str(playerLives) + " WHERE playerName = '" + playerName + "'")
       
       conn.commit()
       conn.close()

# adds one extra life to a user's saved data (void)
def addLivesForUser(playerName):
       conn = sqlite3.connect('game_database.db')
       cursor = conn.cursor()
       
       cursor.execute('UPDATE SCORE_TABLE SET playerLives = ' + str(1 + queryLivesForUser(playerName)) + " WHERE playerName = '" + playerName + "'")
       
       conn.commit()
       conn.close()

# subtracts one extra life from a user's saved data (void)
def subtractLifeForUser(playerName):
       conn = sqlite3.connect('game_database.db')
       cursor = conn.cursor()
       
       cursor.execute('UPDATE SCORE_TABLE SET playerLives = ' + str(queryLivesForUser(playerName) - 1) + " WHERE playerName = '" + playerName + "'")

       conn.commit()
       conn.close()
       if queryLivesForUser(playerName) < 0:
              setLivesForUser(playerName, 0)

# sets red value for user
def setRed(playerName, redValue):
       conn = sqlite3.connect('game_database.db')
       cursor = conn.cursor()
       
       cursor.execute('UPDATE SCORE_TABLE SET red = ' + str(redValue) + " WHERE playerName = '" + playerName + "'")

       conn.commit()
       conn.close()
# sets green value for user
def setGreen(playerName, greenValue):
       conn = sqlite3.connect('game_database.db')
       cursor = conn.cursor()
       
       cursor.execute('UPDATE SCORE_TABLE SET green = ' + str(greenValue) + " WHERE playerName = '" + playerName + "'")

       conn.commit()
       conn.close()

# sets blue value for user
def setBlue(playerName, blueValue):
       conn = sqlite3.connect('game_database.db')
       cursor = conn.cursor()
       
       cursor.execute('UPDATE SCORE_TABLE SET blue = ' + str(blueValue) + " WHERE playerName = '" + playerName + "'")

       conn.commit()
       conn.close()

# returns red value for user
def userRed(playerName):
       conn = sqlite3.connect('game_database.db')
       cursor = conn.cursor()
       
       cursor.execute("SELECT red FROM SCORE_TABLE WHERE playerName = '" + playerName + "'")
       
       i = cursor.fetchone()
       
       conn.close()
       
       return i[0]

# returns green value for user
def userGreen(playerName):
       conn = sqlite3.connect('game_database.db')
       cursor = conn.cursor()
       
       cursor.execute("SELECT green FROM SCORE_TABLE WHERE playerName = '" + playerName + "'")
       
       i = cursor.fetchone()
       
       conn.close()
       
       return i[0]

# returns blue value for user
def userBlue(playerName):
       conn = sqlite3.connect('game_database.db')
       cursor = conn.cursor()
       
       cursor.execute("SELECT blue FROM SCORE_TABLE WHERE playerName = '" + playerName + "'")
       
       i = cursor.fetchone()
       
       conn.close()
       
       return i[0]

# returns score multiplier for user
def getUserMultiply(playerName):
       conn = sqlite3.connect('game_database.db')
       cursor = conn.cursor()
       
       cursor.execute("SELECT scMultiply FROM SCORE_TABLE WHERE playerName = '" + playerName + "'")
       
       i = cursor.fetchone()
       
       conn.close()
       
       return i[0]

# multiplies the user's point multiplier by 2
def upgradeUserMultiply(playerName):
       conn = sqlite3.connect('game_database.db')
       cursor = conn.cursor()
       
       cursor.execute('UPDATE SCORE_TABLE SET scMultiply = ' + str(getUserMultiply(playerName) * 2) + " WHERE playerName = '" + playerName + "'")

       conn.commit()
       conn.close()