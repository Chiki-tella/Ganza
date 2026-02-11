import sqlite3

DB_NAME = "ussd_app.db"

def init_db():
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    # Users table
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        fullname TEXT,
        email TEXT,
        username TEXT,
        password TEXT,
        role TEXT,
        phone TEXT
    )
    """)

    # Product drafts table
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS product_drafts (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        seller_id INTEGER,
        name TEXT,
        price REAL,
        completed INTEGER DEFAULT 0,
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    )
    """)

    # Final products table
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS products (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        seller_id INTEGER,
        name TEXT,
        price REAL,
        quantity TEXT,
        location TEXT
    )
    """)

    conn.commit()
    conn.close()


# ---------------- USERS ----------------
def insert_user(fullname, email, username, password, role, phone):
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute("INSERT INTO users(fullname, email, username, password, role, phone) VALUES (?, ?, ?, ?, ?, ?)",
                   (fullname, email, username, password, role, phone))
    conn.commit()
    conn.close()

def authenticate_user(username, password):
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM users WHERE username=? AND password=?", (username, password))
    user = cursor.fetchone()
    conn.close()
    return user

def get_buyers():
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute("SELECT phone FROM users WHERE role='buyer'")
    buyers = cursor.fetchall()
    conn.close()
    return [b[0] for b in buyers]


# ---------------- PRODUCTS ----------------
def insert_product_draft(seller_id, name, price):
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute("INSERT INTO product_drafts(seller_id, name, price) VALUES (?, ?, ?)",
                   (seller_id, name, price))
    draft_id = cursor.lastrowid
    conn.commit()
    conn.close()
    return draft_id

def get_latest_draft(seller_id):
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM product_drafts WHERE seller_id=? AND completed=0 ORDER BY created_at DESC LIMIT 1",
                   (seller_id,))
    draft = cursor.fetchone()
    conn.close()
    return draft


def insert_product(seller_id, name, price):
    conn = sqlite3.connect("ussd_app.db")
    c = conn.cursor()
    c.execute("INSERT INTO products (seller_id, name, price) VALUES (?, ?, ?)",
              (seller_id, name, price))
    conn.commit()
    conn.close()

def get_products():
    conn = sqlite3.connect("ussd_app.db")
    c = conn.cursor()
    c.execute("SELECT name, price FROM products")
    products = c.fetchall()
    conn.close()
    return products

def complete_product(draft_id, quantity, location):
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    # Get draft
    cursor.execute("SELECT seller_id, name, price FROM product_drafts WHERE id=?", (draft_id,))
    draft = cursor.fetchone()
    if draft:
        seller_id, name, price = draft
        cursor.execute("INSERT INTO products(seller_id, name, price, quantity, location) VALUES (?, ?, ?, ?, ?)",
                       (seller_id, name, price, quantity, location))
        # Mark draft as completed
        cursor.execute("UPDATE product_drafts SET completed=1 WHERE id=?", (draft_id,))
    conn.commit()
    conn.close()
