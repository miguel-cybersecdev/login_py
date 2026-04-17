import customtkinter as ctk
from tkinter import messagebox
from controller.auth_controller import list_one_user, update_user_data

def dashboar_screen(root, user, open_admin, open_edit):
    window = ctk.CTkToplevel(root)

    def refresh():
        window.destroy()
        dashboar_screen(root, user, open_admin, open_edit)

    user_id = user[0]
    userName = user[1]
    role = user[4]

    ctk.CTkLabel(window, text = f"Bem vindo {userName}").pack(pady = 100)

    if role == "admin":
        ctk.CTkButton(window, text = "Painel de Administrador", command = open_admin).pack(pady = 50)
    else:
        ctk.CTkButton(window, text = "Editar seu perfil", command = lambda: open_edit_user(window, user_id)).pack(pady = 50)

def open_edit_user(parent, userId):
    window = ctk.CTkToplevel(parent)
    window.title("Atualizar Seus Dados")
    window.geometry("500x400")

    user = list_one_user(userId)

    ctkUserName = ctk.StringVar(value = user[1])
    ctkEmailUser = ctk.StringVar(value = user[2])
    roleUser = user[4]


    ctk.CTkLabel(window, text="Atualizar Seus Dados", font=("Poppins", 16)).pack(pady = 10)

    entry_user = ctk.CTkEntry(window, placeholder_text= "Usuário", textvariable = ctkUserName)
    entry_user.pack(pady = 5)

    entry_email = ctk.CTkEntry(window, placeholder_text="Email", textvariable = ctkEmailUser)
    entry_email.pack(pady = 5)

    role_option = ctk.CTkOptionMenu(window, values = ["user"])
    role_option.pack(pady = 5)
    role_option.set(roleUser)

    def update():
        userName = entry_user.get()
        emailUser = entry_email.get()
        role = role_option.get()

        success, message = update_user_data(userId, userName, emailUser, role)

        if success:
            messagebox.showinfo("Sucesso", message)
            window.destroy()
            #refresh()
        else:
            messagebox.showerror("Erro", message)

    ctk.CTkButton(window, text="Atualizar", command=update).pack(pady = 10)

