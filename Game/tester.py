import db_functions as db
import db_init as init
import sqlite3
import game_start

print(db.queryDB())
game_start.gameInit()
print(db.queryDB())