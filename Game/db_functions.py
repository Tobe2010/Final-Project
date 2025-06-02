# NOTE: I attempted to use single quotes when possible, but had to use double quotes when a single quote character had to be included in the SQL query/action

import sqlite3

# inserts data for a new player or updates to the score for an already existing user (void)
def insertData (playerName, playerScore):
       conn = sqlite3.connect('game_database.db')
       cursor = conn.cursor()
       
       if checkExists(playerName):
              setScoreForUser(playerName, playerScore)
       else:
              cursor.execute('INSERT INTO SCORE_TABLE (playerName, playerScore) VALUES (?, ?)', (playerName, playerScore))
       
       conn.commit()
       conn.close()
      
# prints every row in the database (void)
def queryDB ():
       conn = sqlite3.connect('game_database.db')
       cursor = conn.cursor()
       
       data = cursor.execute('SELECT * FROM SCORE_TABLE')
       for row in data:
              print(row)

       conn.close()
       
# prints the score for a specific username (int)
def queryScoreForUser (playerName):
       conn = sqlite3.connect('game_database.db')
       cursor = conn.cursor()
       
       cursor.execute("SELECT playerScore FROM SCORE_TABLE WHERE playerName = '" + playerName + "'")
       
       i = cursor.fetchone()
       
       conn.close()
       
       return i[0]

# adds to the score for a specific username (void)
def updateScoreForUser (playerName, newScore):
       conn = sqlite3.connect('game_database.db')
       cursor = conn.cursor()
       
       cursor.execute('UPDATE SCORE_TABLE SET playerScore = ' + str(newScore + queryScoreForUser(playerName)) + " WHERE playerName = '" + playerName + "'")
       
       conn.commit()
       conn.close()

# sets the score for a specific username (void)
def setScoreForUser (playerName, newScore):
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