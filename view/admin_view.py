import customtkinter as ctk
from tkinter import messagebox
from controller.auth_controller import list_user, delete_user_data, register_user

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

        ctk.CTkButton(frame, text = "Editar", command = lambda uid = user_id: open_edit(uid)).pack(side="left", padx=5)
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