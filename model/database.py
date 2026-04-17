import sqlite3
from utils.auth import hash_password

def connect():
    return sqlite3.connect("users.db")

def create_table():
    conn = connect()
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS users (
        idUser INTEGER PRIMARY KEY AUTOINCREMENT,
        userName TEXT UNIQUE,
        emailUser TEXT UNIQUE,
        passwordUser BLOB,
        role TEXT
    )
""")
    
    conn.commit()
    conn.close()

def create_admin():
    conn = connect()
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM users WHERE userName = 'admin'")
    if not cursor.fetchone():
        cursor.execute(
            "INSERT INTO users (userName, emailUser, passwordUser, role) VALUES (?, ?, ?, ?)",
            ("admin", "miguel.snts14.cybersecdev@gmail.com", hash_password("Pr0j3t0!"), "admin")
        )
        conn.commit()

    conn.close()
"""

def view_users():
    conn = connect()
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM users")
    users = cursor.fetchall()

    print(users)

    conn.close()

view_users()




  
def create_admin():
    conn = connect()
    cursor = conn.cursor()

    cursor.execute("""
#    INSERT INTO users (userName, emailUser, passwordUser, role) VALUES ("admin", "miguel.snts14.cybersecdev@gmail.com", "Pr0j3t0!", "admin")
""")
    
    conn.commit()
    conn.close()

*\
"""