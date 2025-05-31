import sqlite3

def insertData (playerName, playerScore):
       conn = sqlite3.connect('game_database.db')
       cursor = conn.cursor()
       
       if checkExists(playerName):
              cursor.execute('INSERT INTO SCORE_TABLE (playerName, playerScore) VALUES (?, ?)', (playerName, playerScore))
       else:
              updateScoreForUser(playerName, playerScore)
       
       conn.commit()
       conn.close()
      
def queryDB ():
       conn = sqlite3.connect('game_database.db')
       cursor = conn.cursor()
       
       data = cursor.execute('SELECT * FROM SCORE_TABLE')
       for row in data:
              print(row)

       conn.close()
       
def queryScoreForUser (playerName):
       conn = sqlite3.connect('game_database.db')
       cursor = conn.cursor()
       
       cursor.execute("SELECT playerScore FROM SCORE_TABLE WHERE playerName = '" + playerName + "'")
       
       i = cursor.fetchone()
       
       conn.close()
       
       return i[0]
       
def updateScoreForUser (playerName, newScore):
       conn = sqlite3.connect('game_database.db')
       cursor = conn.cursor()
       
       cursor.execute('UPDATE SCORE_TABLE SET playerScore = ' + str(newScore + queryScoreForUser(playerName)) + " WHERE playerName = '" + playerName + "'")
       
       conn.commit()
       conn.close()
       
def checkExists(playerName):
       conn = sqlite3.connect('game_database.db')
       cursor = conn.cursor()
       i = 0
       
       data = cursor.execute("SELECT playerName FROM SCORE_TABLE WHERE playerName = '" + playerName + "'")
       
       for row in data:
              i += 1
       
       conn.commit()
       conn.close()
       
       return (i == 0)