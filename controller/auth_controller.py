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
        except Exception as e:
            print("Erro: ", e)
            return False, "Usuário já existe"
    
def login_user(userName, password):
    user = get_user(userName)

    if user and check_password(password, user[3]):
        return user
    
    return None

def list_one_user(user_id):
    user = get_user_id(user_id)
    return user

def update_user_data(user_id, userName, email, role):
    try:
        rows = update_user_admin(user_id, userName, email, role)

        if rows == 0:
            return False, "Nenhuma alteração feita"
        
        return True, "Usuário atualizado"
    
    except Exception as e:
        print("Erro: ", e)
        return False, f"Erro: {e}"

def delete_user_data(user_id):
    delete_user(user_id)

def list_user():
    return get_all_users()