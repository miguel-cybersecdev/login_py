import sqlite3

def connect():
    return sqlite3.connect("users.db")

def create_table():
    conn = connect()
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS users (
        idUser INTEGER PRIMARY KEY AUTOINCREMENT,
        userName TEXT UNIQUE,
        emailUser TEXT,
        passwordUser BLOB,
        role TEXT
    )
""")
    
    conn.commit()
    conn.close()