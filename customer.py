import tkinter as tk
from tkinter import messagebox
from db import get_connection

print("Customer file loaded")

def open_customer(user_id):
    root = tk.Tk()
    root.title("Customer Panel")
    root.geometry("500x500")

    # Function to view all products
    def view_products():
        try:
            conn = get_connection()
            cursor = conn.cursor()
            cursor.execute("SELECT id, name, price, quantity FROM products")
            rows = cursor.fetchall()

            text_area.delete("1.0", tk.END)
            text_area.insert(tk.END, "---- Products ----\n")
            for row in rows:
                text_area.insert(tk.END, f"ID: {row[0]} | Name: {row[1]} | Price: {row[2]} | Qty: {row[3]}\n")

        except Exception as e:
            messagebox.showerror("Error", str(e))

    # Function to search product by name
    def search_product():
        try:
            name = entry_search.get()
            conn = get_connection()
            cursor = conn.cursor()
            cursor.execute("SELECT id, name, price, quantity FROM products WHERE name LIKE %s", ('%' + name + '%',))
            rows = cursor.fetchall()

            text_area.delete("1.0", tk.END)
            if rows:
                for row in rows:
                    text_area.insert(tk.END, f"ID: {row[0]} | Name: {row[1]} | Price: {row[2]} | Qty: {row[3]}\n")
            else:
                text_area.insert(tk.END, "No products found with that name.\n")

        except Exception as e:
            messagebox.showerror("Error", str(e))

    # Function to buy product
    def buy_product():
        try:
            product_id = entry_buy_id.get()
            qty = int(entry_buy_qty.get())

            conn = get_connection()
            cursor = conn.cursor()

            # Check available quantity
            cursor.execute("SELECT quantity, name FROM products WHERE id=%s", (product_id,))
            result = cursor.fetchone()
            if not result:
                messagebox.showerror("Error", "Product ID not found")
                return

            available_qty, product_name = result
            if qty > available_qty:
                messagebox.showerror("Error", f"Only {available_qty} items available")
                return

            # Reduce quantity
            cursor.execute("UPDATE products SET quantity=quantity-%s WHERE id=%s", (qty, product_id))
            conn.commit()

            messagebox.showinfo("Success", f"Purchased {qty} x {product_name}")
            view_products()  # Refresh product list

        except Exception as e:
            messagebox.showerror("Error", str(e))

    # Widgets
    tk.Label(root, text=f"Welcome Customer {user_id}", font=("Arial", 14)).pack(pady=10)

    tk.Button(root, text="View All Products", command=view_products).pack(pady=5)

    # Search Section
    tk.Label(root, text="Search Product by Name").pack()
    entry_search = tk.Entry(root)
    entry_search.pack()
    tk.Button(root, text="Search", command=search_product).pack(pady=5)

    # Buy Section
    tk.Label(root, text="Buy Product").pack(pady=10)
    tk.Label(root, text="Product ID").pack()
    entry_buy_id = tk.Entry(root)
    entry_buy_id.pack()
    tk.Label(root, text="Quantity").pack()
    entry_buy_qty = tk.Entry(root)
    entry_buy_qty.pack()
    tk.Button(root, text="Buy", command=buy_product).pack(pady=5)

    # Text area to display products
    text_area = tk.Text(root, height=15, width=60)
    text_area.pack(pady=10)

    tk.Button(root, text="Logout", command=root.destroy).pack(pady=10)

    # Show products initially
    view_products()

    root.mainloop()
