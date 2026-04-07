from model.database import connect

def create_user(userName, email, password, role):
    conn = connect()
    cursor = conn.cursor()

    cursor.execute(
        "INSERT INTO users (userName, email, password, role) VALUES (?, ?, ?, ?)",
        (userName, email, password, role)
    )

    conn.commit()
    conn.close()


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

    conn.close()
    return users

def update_user(idUser, userName, email, password):
    conn = connect()
    cursor = conn.cursor()

    cursor.execute(
        "UPDATE users SET userName = ?, password = ?, email = ? WHERE idUser = ?",
        (userName, email, password, idUser)
    )

def delete_user(idUser):
    conn = connect()
    cursor = conn.cursor()

    cursor.execute("DELETE FROM users WHERE idUser = ?", (idUser,))
    conn.commit()
    conn.close()