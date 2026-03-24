import sqlite3

def init_db():
    conn = sqlite3.connect("app.db")

    conn.execute("""
    CREATE TABLE users (
        id INTEGER PRIMARY KEY,
        balance INTEGER
    )
    """)

    conn.execute("INSERT INTO users (id, balance) VALUES (1, 100)")

    conn.commit()
    conn.close()

def get_user_balance(id):
    conn = sqlite3.connect("app.db")

    res = conn.execute(f"SELECT balance FROM users WHERE id = '{id}'")

    balance = res.fetchone()

    conn.close()

    if len(balance) == 0:
        return None
    else:
        return balance[0]