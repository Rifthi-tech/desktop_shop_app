import tkinter as tk
from tkinter import messagebox
from db import get_connection

print("Customer file loaded")

def open_customer(user_id):
    root = tk.Tk()
    root.title("Customer Panel")
    root.geometry("600x550")

    # ---------------- VIEW PRODUCTS ----------------
    def view_products():
        try:
            conn = get_connection()
            cursor = conn.cursor()
            cursor.execute("SELECT id, name, price, quantity FROM products")
            rows = cursor.fetchall()

            text_area.delete("1.0", tk.END)
            text_area.insert(tk.END, "---- Products ----\n")

            for row in rows:
                text_area.insert(
                    tk.END,
                    f"ID:{row[0]} | {row[1]} | Price:{row[2]} | Stock:{row[3]}\n"
                )

        except Exception as e:
            messagebox.showerror("Error", str(e))

    # ---------------- ADD TO CART ----------------
    def add_to_cart():
        try:
            product_id = entry_cart_id.get()
            qty = int(entry_cart_qty.get())

            conn = get_connection()
            cursor = conn.cursor()

            # Check product exists
            cursor.execute("SELECT quantity FROM products WHERE id=%s", (product_id,))
            result = cursor.fetchone()

            if not result:
                messagebox.showerror("Error", "Product not found")
                return

            available_qty = result[0]
            if qty > available_qty:
                messagebox.showerror("Error", f"Only {available_qty} items available")
                return

            # Insert into cart
            cursor.execute(
                "INSERT INTO cart (user_id, product_id, quantity) VALUES (%s, %s, %s)",
                (user_id, product_id, qty)
            )
            conn.commit()

            messagebox.showinfo("Success", "Added to Cart")

        except Exception as e:
            messagebox.showerror("Error", str(e))

    # ---------------- VIEW CART ----------------
    def view_cart():
        try:
            conn = get_connection()
            cursor = conn.cursor()

            cursor.execute("""
                SELECT p.name, p.price, c.quantity 
                FROM cart c
                JOIN products p ON c.product_id = p.id
                WHERE c.user_id=%s
            """, (user_id,))

            rows = cursor.fetchall()

            text_area.delete("1.0", tk.END)
            text_area.insert(tk.END, "---- Your Cart ----\n")

            total = 0

            for row in rows:
                name, price, qty = row
                subtotal = price * qty
                total += subtotal

                text_area.insert(
                    tk.END,
                    f"{name} | Price:{price} | Qty:{qty} | Subtotal:{subtotal}\n"
                )

            text_area.insert(tk.END, f"\nTotal: {total}")

        except Exception as e:
            messagebox.showerror("Error", str(e))

    # ---------------- UI ----------------

    tk.Label(root, text=f"Welcome Customer {user_id}", font=("Arial", 14)).pack(pady=10)

    tk.Button(root, text="View Products", command=view_products).pack(pady=5)

    # Add to Cart Section
    tk.Label(root, text="Add To Cart").pack(pady=10)

    tk.Label(root, text="Product ID").pack()
    entry_cart_id = tk.Entry(root)
    entry_cart_id.pack()

    tk.Label(root, text="Quantity").pack()
    entry_cart_qty = tk.Entry(root)
    entry_cart_qty.pack()

    tk.Button(root, text="Add to Cart", command=add_to_cart).pack(pady=5)

    tk.Button(root, text="View Cart", command=view_cart).pack(pady=5)

    # Display Area
    text_area = tk.Text(root, height=15, width=70)
    text_area.pack(pady=10)

    tk.Button(root, text="Logout", command=root.destroy).pack(pady=10)

    view_products()

    root.mainloop()