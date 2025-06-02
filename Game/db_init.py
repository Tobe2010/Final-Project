import sqlite3

# helper function to create the database
def init_db():
    conn = sqlite3.connect('game_database.db')
    cursor = conn.cursor()

    table = """ CREATE TABLE SCORE_TABLE (
                playerName TEXT,
                playerScore INTEGER,
                playerLives INTEGER
            ); """

    cursor.execute(table)

    conn.close()