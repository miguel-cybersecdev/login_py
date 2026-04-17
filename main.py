import customtkinter as ctk
from model.database import create_table, create_admin
from view.admin_view import admin_panel
from view.login_view import login_screen
from view.dashboard_view import dashboar_screen
from controller.auth_controller import update_user_data, register_user

ctk.set_appearance_mode("dark")


create_table()
create_admin()


root = ctk.CTk()
root.title("Sistema CRUD com login")

def open_dashboard(user):
    dashboar_screen(root, user, open_admin, open_edit)

def open_admin():
    admin_panel(root, open_edit)

def open_edit(user_id):
    def save(userName, password, email):
        update_user_data(user_id, userName, email)


login_screen(root, open_dashboard)

root.mainloop()