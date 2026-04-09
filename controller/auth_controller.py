from model.user_model import *
from utils.auth import hash_password, check_password

def register_user(username, password, role="user"):
    try:
        create_user(username, hash_password(password), role)
        return True
    except:
        return False
    
def login_user(username, password):
    user = get_user(username)

    if user and check_password(password, user[2]):
        return user
    
    return None

def update_user_data(user_id, username, email, password):
    update_user(user_id, username, email, hash_password(password))

def delete_user_data(user_id):
    delete_user(user_id)

def list_user():
    return get_all_users()