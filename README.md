# Flask Tkinter E-Commerce Dashboard

A simple **desktop E-Commerce dashboard** built with **Python Tkinter** and **MySQL**, featuring separate Admin and Customer panels.

---

## Features

### Admin Panel
- Add new products
- View all products
- Delete products by ID

### Customer Panel
- View all products
- Search products by name
- Buy products (updates quantity automatically)
- Simple text-based product display

---

## Installation

1. **Clone the repository**
```bash
git clone <your-repo-url>
cd <your-repo-folder>
Install dependencies


Set up the database

Create a MySQL database named shop (or update db.py connection settings)

Create a products table and a users table:

CREATE TABLE products (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255),
    price FLOAT,
    quantity INT
);

CREATE TABLE users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    username VARCHAR(50),
    password VARCHAR(50),
    role VARCHAR(10)
);
Run the app

python login.py

```
Notes
Admin and Customer roles are handled separately.

Database connection info is in db.py. Update according to your local setup.
