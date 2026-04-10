from model.user_model import *
from utils.auth import hash_password, check_password
from utils.validator import validate_password

def register_user(userName, email, password, role = "user"):
        valid, message = validate_password(password)
        if not valid:
            return False, message
        try:
            hashed = hash_password(password)
            create_user(userName, email, hashed, role)
            return True, "Usuário criado com sucesso"
        except:
            return False, "Usuário já existe"
    
def login_user(userName, password):
    user = get_user(userName)

    if user and check_password(password, user[3]):
        return user
    
    return None

def update_user_data(user_id, userName, email, password):
    update_user(user_id, userName, email, hash_password(password))

def delete_user_data(user_id):
    delete_user(user_id)

def list_user():
    return get_all_users()