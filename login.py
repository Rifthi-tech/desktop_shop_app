import tkinter as tk
from tkinter import messagebox
from db import get_connection
import admin
import customer

def login_user():
    username = entry_username.get()
    password = entry_password.get()

    try:
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute(
            "SELECT id, role FROM users WHERE username=%s AND password=%s",
            (username, password)
        )
        result = cursor.fetchone()

        if result:
            user_id, role = result
            root.destroy()
            if role == 'admin':
                admin.open_admin(user_id)
            else:
                customer.open_customer(user_id)
        else:
            messagebox.showerror("Error", "Invalid credentials")

    except Exception as e:
        messagebox.showerror("Database Error", str(e))


# CREATE WINDOW OUTSIDE FUNCTION
root = tk.Tk()
root.title("Login")
root.geometry("300x200")

tk.Label(root, text="Username").pack()
entry_username = tk.Entry(root)
entry_username.pack()

tk.Label(root, text="Password").pack()
entry_password = tk.Entry(root, show="*")
entry_password.pack()

tk.Button(root, text="Login", command=login_user).pack(pady=10)

root.mainloop()
