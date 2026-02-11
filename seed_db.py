import sqlite3
import random

DB_NAME = "ussd_app.db"

def seed_users():
    conn = sqlite3.connect(DB_NAME)
    cur = conn.cursor()

    users = [
        ("Alice Mugenzi", "alice@example.com", "alice", "pass123", "buyer", "+250780000111"),
        ("Bob Niyonsenga", "bob@example.com", "bob", "pass456", "seller", "+250780000222"),
        ("Carine Uwase", "carine@example.com", "carine", "pass789", "buyer", "+250780000333"),
        ("David Mugisha", "david@example.com", "david", "pass000", "seller", "+250780000444")
    ]

    cur.executemany(
        "INSERT INTO users(fullname, email, username, password, role, phone) VALUES (?, ?, ?, ?, ?, ?)",
        users
    )
    conn.commit()
    conn.close()
    print("✅ Users seeded successfully")


def seed_products():
    conn = sqlite3.connect(DB_NAME)
    cur = conn.cursor()

    # Get seller ids from DB
    cur.execute("SELECT id FROM users WHERE role='seller'")
    sellers = [row[0] for row in cur.fetchall()]

    products = []
    for seller_id in sellers:
        for i in range(3):  # 3 products per seller
            name = f"Product_{random.randint(100, 999)}"
            price = round(random.uniform(100, 5000), 2)
            quantity = str(random.randint(1, 20))
            location = random.choice(["Kigali", "Huye", "Musanze", "Rubavu"])
            products.append((seller_id, name, price, quantity, location))

    cur.executemany(
        "INSERT INTO products(seller_id, name, price, quantity, location) VALUES (?, ?, ?, ?, ?)",
        products
    )
    conn.commit()
    conn.close()
    print("✅ Products seeded successfully")


if __name__ == "__main__":
    seed_users()
    seed_products()
