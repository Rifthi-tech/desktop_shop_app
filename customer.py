import tkinter as tk
from db import get_connection
from tkinter import messagebox

print("Admin file loaded")

def open_admin(user_id):
    root = tk.Tk()
    root.title("Admin Panel")
    root.geometry("400x400")

    def add_product():
        try:
            conn = get_connection()
            cursor = conn.cursor()
            cursor.execute(
                "INSERT INTO products (name, price, quantity) VALUES (%s, %s, %s)",
                (entry_name.get(), entry_price.get(), entry_qty.get())
            )
            conn.commit()
            messagebox.showinfo("Success", "Product Added")
        except Exception as e:
            messagebox.showerror("Error", str(e))

    def view_products():
        try:
            conn = get_connection()
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM products")
            rows = cursor.fetchall()
            print("---- Products ----")
            for row in rows:
                print(row)
        except Exception as e:
            messagebox.showerror("Error", str(e))

    def delete_product():
        try:
            conn = get_connection()
            cursor = conn.cursor()
            cursor.execute(
                "DELETE FROM products WHERE id=%s",
                (entry_id.get(),)
            )
            conn.commit()
            messagebox.showinfo("Deleted", "Product Deleted")
        except Exception as e:
            messagebox.showerror("Error", str(e))

    tk.Label(root, text="Product Name").pack()
    entry_name = tk.Entry(root)
    entry_name.pack()

    tk.Label(root, text="Price").pack()
    entry_price = tk.Entry(root)
    entry_price.pack()

    tk.Label(root, text="Quantity").pack()
    entry_qty = tk.Entry(root)
    entry_qty.pack()

    tk.Button(root, text="Add Product", command=add_product).pack(pady=5)
    tk.Button(root, text="View Products", command=view_products).pack(pady=5)

    tk.Label(root, text="Delete Product ID").pack()
    entry_id = tk.Entry(root)
    entry_id.pack()

    tk.Button(root, text="Delete Product", command=delete_product).pack(pady=5)

    tk.Button(root, text="Logout", command=root.destroy).pack(pady=10)

    root.mainloop()
