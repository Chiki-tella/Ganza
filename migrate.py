import sqlite3

conn = sqlite3.connect("ussd_app.db")
cur = conn.cursor()

cur.execute("ALTER TABLE users ADD COLUMN phone TEXT")

conn.commit()
conn.close()

print("✅ Column 'phone' added to users table")
