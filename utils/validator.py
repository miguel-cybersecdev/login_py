import re

def validate_password(password):
    if len(password) < 8:
        return False, "Senha deve conter mais de 8 caracteres"
    
    if not re.search(r"[A-Z]", password):
        return False, "Senha deve conter pelo menos uma letra maiúscula"
    
    if not re.search(r"[a-z]", password):
        return False, "Senha deve conter pelo menos uma letra minúscula"
    
    if not re.search(r"\d", password):
        return False, "Senha deve conter pelo menos um número"
    
    if not re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        return False, "Senha deve conter pelo menos um caractere especial"
    
    return True, "Senha válida"