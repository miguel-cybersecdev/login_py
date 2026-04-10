import customtkinter as ctk
from tkinter import messagebox
from controller.auth_controller import login_user

def login_screen(root, open_dashboard):
    frame = ctk.CTkFrame(root)
    frame.pack(pady = 100)

    entry_user = ctk.CTkEntry(frame, placeholder_text = "Usuário")
    entry_user.pack(pady = 5)

    entry_pass = ctk.CTkEntry(frame, placeholder_text = "Senha", show = "*")
    entry_pass.pack(pady = 5)

    def login():
        user = login_user(entry_user.get(), entry_pass.get())

        if user:
            open_dashboard(user)
        else:
            messagebox.showerror("Erro", "Login inválido")

    ctk.CTkButton(frame, text = "Entrar", command = login).pack(pady = 10)