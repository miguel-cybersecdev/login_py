from model.database import connect

def create_user(userName, email, password, role):
    conn = connect()
    cursor = conn.cursor()

    cursor.execute(
        "INSERT INTO users (userName, emailUser, passwordUser, role) VALUES (?, ?, ?, ?)",
        (userName, email, password, role)
    )

    conn.commit()
    conn.close()

def get_user_id(idUser):
    conn = connect()
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM users WHERE idUser = ?", (idUser,))
    user = cursor.fetchone()

    conn.close()
    return user

def get_user(userName):
    conn = connect()
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM users WHERE userName = ?", (userName,))
    user = cursor.fetchone()

    conn.close()
    return user

def get_all_users():
    conn = connect()
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM users")
    users = cursor.fetchall()

    print(users)

    conn.close()
    return users

def update_user_admin(idUser, userName, email, role):
    import sqlite3

    with sqlite3.connect("users.db") as conn:
        cursor = conn.cursor()

        cursor.execute(
            "UPDATE users SET userName = ?, role = ?, emailUser = ? WHERE idUser = ?",
            (userName, role, email, idUser)
        )

        conn.commit()

        return cursor.rowcount
    

def delete_user(idUser):
    conn = connect()
    cursor = conn.cursor()

    cursor.execute("DELETE FROM users WHERE idUser = ?", (idUser,))
    conn.commit()
    conn.close()

get_all_users()