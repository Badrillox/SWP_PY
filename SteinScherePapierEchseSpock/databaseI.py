import sqlite3


def create_database(db_file):
    try:
        conn = sqlite3.connect(db_file)
        sqlite_table_query = ''' Create table if not exists game_outputs (
                                 id INTEGER Primary key,
                                 user TEXT not null,
                                 pc TEXT not null,
                                 game TEXT not null);'''
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
    sql = ''' INSERT INTO Game_outputs(user,pc,game)
                  VALUES(?,?,?) '''
    cur = conn.cursor()
    game = (userinput,aiinput, result)
    cur.execute(sql, game)
    conn.commit()
    return cur.lastrowid
