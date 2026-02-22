# 🛍️ Desktop Shop App

<div align="center">

[![GitHub stars](https://img.shields.io/github/stars/Rifthi-tech/desktop_shop_app?style=for-the-badge)](https://github.com/Rifthi-tech/desktop_shop_app/stargazers)
[![GitHub forks](https://img.shields.io/github/forks/Rifthi-tech/desktop_shop_app?style=for-the-badge)](https://github.com/Rifthi-tech/desktop_shop_app/network)
[![GitHub issues](https://img.shields.io/github/issues/Rifthi-tech/desktop_shop_app?style=for-the-badge)](https://github.com/Rifthi-tech/desktop_shop_app/issues)
[![GitHub license](https://img.shields.io/github/license/Rifthi-tech/desktop_shop_app?style=for-the-badge)](LICENSE) <!-- TODO: Add a LICENSE file -->

**A simple E-Commerce Dashboard with Admin and Customer panels, built with Python Tkinter and MySQL.**

</div>

## 📖 Overview

This project is a standalone desktop E-commerce Dashboard application designed to manage products and facilitate purchases. It features distinct interfaces and functionalities for two primary user roles: **Administrators** and **Customers**. The application provides a user-friendly graphical interface built with Python's Tkinter and uses MySQL as its backend database for robust data persistence. It's ideal for a small-scale shop management system or as a learning resource for desktop application development with Python and databases.

## ✨ Features

-   **🔐 Role-Based Authentication:** Secure login system with distinct panels for Admin and Customer roles.
-   **💼 Admin Panel:**
    -   ➕ Add new products (Product ID, Name, Price, Quantity).
    -   👁️ View all existing products.
    -   🗑️ Delete products from the inventory.
-   **🛒 Customer Panel:**
    -   📄 Browse available products.
    -   🔍 Search for products by name.
    -   💰 Purchase items, updating inventory in real-time.
-   **🗄️ MySQL Database Integration:** Persistent storage for product and user data.
-   **🚫 Basic Error Handling:** Provides user feedback for common issues (e.g., invalid login, insufficient stock).

## 🛠️ Tech Stack

**GUI Framework:**
![Python](https://img.shields.io/badge/Python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![Tkinter](https://img.shields.io/badge/Tkinter-Python_Built--in-blue?style=for-the-badge)

**Backend Logic:**
![Python](https://img.shields.io/badge/Python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)

**Database:**
![MySQL](https://img.shields.io/badge/MySQL-4479A1?style=for-the-badge&logo=mysql&logoColor=white)

**Database Driver:**
![mysql-connector-python](https://img.shields.io/badge/mysql--connector--python-v8.0.33-orange?style=for-the-badge)

## 🚀 Quick Start

Follow these steps to get the desktop shop application up and running on your local machine.

### Prerequisites

-   **Python 3.x:** Ensure you have Python 3 installed. You can download it from [python.org](https://www.python.org/downloads/).
-   **MySQL Server:** A running MySQL server instance is required. You can download MySQL Community Server from [mysql.com](https://dev.mysql.com/downloads/mysql/).

### Installation

1.  **Clone the repository**
    ```bash
    git clone https://github.com/Rifthi-tech/desktop_shop_app.git
    cd desktop_shop_app
    ```

2.  **Create and activate a virtual environment**
    It's recommended to use a virtual environment to manage dependencies.
    ```bash
    python -m venv venv
    # On Windows
    .\venv\Scripts\activate
    # On macOS/Linux
    source venv/bin/activate
    ```

3.  **Install dependencies**
    ```bash
    pip install mysql-connector-python
    ```
    _Note: Tkinter is usually included with standard Python distributions._

### Database Setup

1.  **Start your MySQL server.**

2.  **Connect to your MySQL server** using a client (e.g., MySQL Workbench, `mysql` command-line client) and create a new database.

    ```sql
    CREATE DATABASE shop_db;
    USE shop_db;
    ```

3.  **Create the necessary tables** (`users` and `products`) and insert initial data:

    ```sql
    -- Users Table
    CREATE TABLE users (
        username VARCHAR(255) PRIMARY KEY,
        password VARCHAR(255) NOT NULL,
        role VARCHAR(50) NOT NULL -- 'Admin' or 'Customer'
    );

    -- Products Table
    CREATE TABLE products (
        id INT AUTO_INCREMENT PRIMARY KEY,
        name VARCHAR(255) NOT NULL,
        price DECIMAL(10, 2) NOT NULL,
        quantity INT NOT NULL
    );

    -- Insert initial data (Example: Admin and Customer accounts)
    INSERT INTO users (username, password, role) VALUES ('admin', 'admin123', 'Admin');
    INSERT INTO users (username, password, role) VALUES ('customer', 'customer123', 'Customer');

    -- Insert some sample products
    INSERT INTO products (name, price, quantity) VALUES ('Laptop', 1200.00, 10);
    INSERT INTO products (name, price, quantity) VALUES ('Mouse', 25.00, 50);
    INSERT INTO products (name, price, quantity) VALUES ('Keyboard', 75.00, 20);
    ```

### Configuration

Open `db.py` and update the database connection details if they differ from the defaults (e.g., if your MySQL username or password is not `root`/empty, or if MySQL is not running on `localhost:3306`).

```python
# db.py
import mysql.connector
from tkinter import messagebox

def get_db_connection():
    try:
        conn = mysql.connector.connect(
            host="localhost", # Update if your MySQL server is elsewhere
            user="root",      # Update with your MySQL username
            password="",      # Update with your MySQL password
            database="shop_db"
        )
        return conn
    except mysql.connector.Error as err:
        messagebox.showerror("Database Error", f"Error: {err}")
        return None
```

### Run the Application

Once the database is set up and `db.py` is configured, you can run the application:

```bash
python main.py
```
This will launch the login window.

### Default Credentials

Use the following credentials to log in:

-   **Admin:**
    -   Username: `admin`
    -   Password: `admin123`
-   **Customer:**
    -   Username: `customer`
    -   Password: `customer123`

## 📁 Project Structure

```
desktop_shop_app/
├── admin.py        # Contains the Admin Panel GUI and logic for product management.
├── customer.py     # Contains the Customer Panel GUI and logic for browsing/purchasing.
├── db.py           # Handles the connection to the MySQL database and provides utility functions.
├── login.py        # Implements the user login interface and authenticates users based on roles.
├── main.py         # The main entry point of the application, which starts the login window.
├── README.md       # Project README file.
├── venv/           # Python virtual environment (ignored by Git).
└── __pycache__/    # Python compiled bytecode cache.
```

## 🤝 Contributing

We welcome contributions! If you have suggestions for improvements or new features, feel free to:

1.  Fork the repository.
2.  Create a new branch (`git checkout -b feature/YourFeature`).
3.  Make your changes.
4.  Commit your changes (`git commit -m 'Add new feature'`).
5.  Push to the branch (`git push origin feature/YourFeature`).
6.  Open a Pull Request.

## 🙏 Acknowledgments

-   **Python:** The programming language powering this application.
-   **Tkinter:** For providing a robust framework for building the graphical user interface.
-   **MySQL:** For serving as the reliable backend database.
-   **mysql-connector-python:** The official MySQL driver for Python.

## 📞 Support & Contact

-   🐛 Issues: [GitHub Issues](https://github.com/Rifthi-tech/desktop_shop_app/issues)

---

<div align="center">

**⭐ Star this repo if you find it helpful!**

Made with ❤️ by Rifthi-tech

</div>
