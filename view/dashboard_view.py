import customtkinter as ctk

def dashboar_screen(root, user, open_admin, open_edit):
    window = ctk.CTkToplevel(root)

    user_id = user[0]
    userName = user[1]
    role = user[4]

    ctk.CTkLabel(window, text = f"Bem vindo {userName}").pack(pady = 100)

    if role == "admin":
        ctk.CTkButton(window, text = "Painel de Administrador", command = open_admin).pack(pady = 50)
    else:
        ctk.CTkButton(window, text = "Editar seu perfil", command = lambda: open_edit(user_id)).pack(pady = 50)

