import sqlite3
import gamelogic_a
def create_database(db_file):
    try:
        conn = sqlite3.connect(db_file)
        sqlite_table_query = ''' CREATE TABLE IF NOT EXISTS game_outputs (
                                 id INTEGER PRIMARY KEY,
                                 user TEXT NOT NULL,
                                 pc TEXT NOT NULL,
                                 game TEXT NOT NULL
                                 );'''
        cursor = conn.cursor()
        print("Successfully Connected to SQLite")
        cursor.execute(sqlite_table_query);
        conn.commit()
        print("SQLlite table created")
        cursor.close()

    except sqlite3.Error as error:
        print("Error while connecting to sqlite", error)
    finally:
        if conn:
            conn.close()
            print("The SQLite connection is closed")


def insert(db_file, userinput, aiinput, result):
    conn = sqlite3.connect(db_file)
    sql = ''' INSERT INTO game_outputs(user,pc,game)
                  VALUES(?,?,?) '''
    cur = conn.cursor()
    game = (userinput, aiinput, result)
    cur.execute(sql, game)
    conn.commit()
    cur.close()
    conn.close()

def selectResult(db_file):
    conn = sqlite3.connect(db_file)
    sqlWin = "SELECT count(game) FROM game_outputs WHERE game = 'win'"
    sqlLose = "SELECT count(game) FROM game_outputs WHERE game = 'lose'"
    sqlDraw = "SELECT count(game) FROM game_outputs WHERE game = 'draw'"
    cur = conn.cursor()
    cur.execute(sqlWin)
    rowsWins = cur.fetchall()
    cur.execute(sqlLose)
    rowsLose = cur.fetchall()
    cur.execute(sqlDraw)
    rowsDraw = cur.fetchall()
    cur.close()
    conn.close()
    for a in rowsWins:
        wins = int(a[0])
    for a in rowsLose:
        lose = int(a[0])
    for a in rowsDraw:
        draw = int(a[0])
    print("Wins:",wins,"\nLose:",lose,"\nDraw:",draw)

def selectUser(db_file):
    conn = sqlite3.connect(db_file)
    sql = "SELECT user FROM game_outputs GROUP BY user ORDER BY user limit 1"
    sqlCount = "SELECT count(user) FROM game_outputs group BY user order BY user limit 1"
    cur = conn.cursor()
    cur.execute(sql)
    rowUser = cur.fetchall()
    cur.execute(sqlCount)
    rowCount = cur.fetchall()
    cur.close()
    conn.close()
    for a in rowUser:
       user = str(a[0])
    for a in rowCount:
       count = int(a[0])
    print("\nMost used by AI:",user,"\nHow often used by PC:", count)

def selectAI(db_file):
    conn = sqlite3.connect(db_file)
    sql = "SELECT pc FROM game_outputs GROUP BY pc ORDER BY pc limit 1"
    sqlCount = "SELECT count(pc) FROM game_outputs GROUP BY pc ORDER BY pc limit 1"
    cur = conn.cursor()
    cur.execute(sql)
    rowPc = cur.fetchall()
    cur.execute(sqlCount)
    rowCount = cur.fetchall()
    cur.close()
    conn.close()
    for a in rowPc:
       pc = str(a[0])
    for a in rowCount:
       count = int(a[0])
    print("\nMost used by AI:",pc,"\nHow often used by PC:", count)
