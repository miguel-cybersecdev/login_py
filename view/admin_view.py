import customtkinter as ctk
from tkinter import messagebox
from controller.auth_controller import list_user, delete_user_data, register_user, update_user_data, list_one_user

def admin_panel(root, open_edit):
    panel = ctk.CTkToplevel(root)
    panel.title("Painel Admin")
    panel.geometry("500x400")

    def refresh():
        panel.destroy()
        admin_panel(root, open_edit)

    ctk.CTkButton(panel, text="Criar Usuário", command= lambda: open_create_user(panel, refresh)).pack(pady = 10)

    users = list_user()

    for user in users:
        user_id, userName, emailUser, passwordUser, role = user

        frame = ctk.CTkFrame(panel)
        frame.pack(pady = 5, padx = 10, fill="x")

        ctk.CTkLabel(frame, text = f"{userName} ({role})").pack(side = "left", padx=10)

        ctk.CTkButton(frame, text = "Editar", command = lambda uid = user_id: open_edit_users(panel, refresh, uid)).pack(side="left", padx=5)
        ctk.CTkButton(frame, text = "Deletar", command = lambda uid = user_id: delete_refresh(uid, refresh)).pack(side="left", padx=5)

def delete_refresh(user_id, refresh):
    confirm = messagebox.askyesno("Confirmar", "Deseja exluir este usuário?")

    if confirm:
        delete_user_data(user_id)
        messagebox.showinfo("Sucesso!", "Usuário deletado")
        refresh()

def open_create_user(parent, refresh):
    window = ctk.CTkToplevel(parent)
    window.title("Criar Usuário")
    window.geometry("500x400")

    ctk.CTkLabel(window, text="Novo Usuário", font=("Poppins", 16)).pack(pady = 10)

    entry_user = ctk.CTkEntry(window, placeholder_text= "Usuário")
    entry_user.pack(pady = 5)

    entry_email = ctk.CTkEntry(window, placeholder_text="Email")
    entry_email.pack(pady = 5)

    entry_password = ctk.CTkEntry(window, placeholder_text="Senha", show = "*")
    entry_password.pack(pady = 5)

    role_option = ctk.CTkOptionMenu(window, values = ["user", "admin"])
    role_option.pack(pady = 5)
    role_option.set("user")

    def create():
        userName = entry_user.get()
        emailUser = entry_email.get()
        passwordUser = entry_password.get()
        role = role_option.get()

        success, message = register_user(userName, emailUser, passwordUser, role)

        if success:
            messagebox.showinfo("Sucesso", message)
            window.destroy()
            refresh()
        else:
            messagebox.showerror("Erro", message)

    ctk.CTkButton(window, text="Criar", command=create).pack(pady = 10)


def open_edit_users(parent, refresh, userId):
    window = ctk.CTkToplevel(parent)
    window.title("Atualizar Usuário")
    window.geometry("500x400")

    user = list_one_user(userId)

    ctkUserName = ctk.StringVar(value = user[1])
    ctkEmailUser = ctk.StringVar(value = user[2])
    roleUser = user[4]


    ctk.CTkLabel(window, text="Atualizar Usuário", font=("Poppins", 16)).pack(pady = 10)

    entry_user = ctk.CTkEntry(window, placeholder_text= "Usuário", textvariable = ctkUserName)
    entry_user.pack(pady = 5)

    entry_email = ctk.CTkEntry(window, placeholder_text="Email", textvariable = ctkEmailUser)
    entry_email.pack(pady = 5)

    role_option = ctk.CTkOptionMenu(window, values = ["user", "admin"])
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
            refresh()
        else:
            messagebox.showerror("Erro", message)

    ctk.CTkButton(window, text="Atualizar", command=update).pack(pady = 10)