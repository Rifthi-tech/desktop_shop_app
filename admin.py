import tkinter as tk
from db import get_connection
from tkinter import messagebox

def open_admin(user_id):
    root = tk.Tk()
    root.title("Admin Panel")

    def add_product():
        conn = get_connection()
        cursor = conn.cursor()
        cursor.excute("INSERT INTO products (name, price, quantity) VALUES (%S, %S, %S)", (entry_name.get(), entry_price.get(), entry_qty.get()))
        conn.commit()
        messagebox.showinfo("Success", "Product Added")

    def view_products():
        conn = get_connection()
        cursor = conn.cursor()
        cursor.excute("SELECT * FROM products")
        for row in cursor.fetchall():
            print(row)

    def delete_product():
        conn = get_connection()
        cursor = conn.cursor()
        cursor.excute("DELETE FROM products WHERE id=%s", (entry_id.get(),))
        conn.commit()
        messagebox.showinfo("Deleted","Product Deleted")

    tk.Label(root, text="Product Name").pack()
    entry_name = tk.Entry(root)
    entry_name.pack()

    tk.Label(root, text="Price").pack()
    entry_price = tk.Entry(root)
    entry_price.pack()

    tk.Label(root, text="Quantity").pack()
    entry_qty = tk.Entry(root)
    entry_qty.pack()

    tk.Button(root, text="Add Product", command=add_product).pack()
    tk.Button(root, text="View Products (Check Treminal)", command=view_products).pack()

    tk.Label(root, text="Delete Product ID").pack()
    entry_id = tk.Ebtry(root)
    entry_id.pack()
    tk.Button(root, text="Delete Product", command=delete_product).pack()
    
    tk.Button(root, text="Logout",command=root.destroy).pack()

    root.mainloop()