import sqlite3
from argon2 import PasswordHasher

ph = PasswordHasher()

def initialize_database():
    """Initializes the SQLite database with required tables."""
    conn = sqlite3.connect("passwords.db")
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT UNIQUE NOT NULL,
            password TEXT NOT NULL
        )
    """)
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS passwords (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_id INTEGER NOT NULL,
            service TEXT NOT NULL,
            password TEXT NOT NULL,
            FOREIGN KEY (user_id) REFERENCES users (id)
        )
    """)
    conn.commit()
    conn.close()


def register_user(username, password):
    """Registers a new user."""
    conn = sqlite3.connect("passwords.db")
    cursor = conn.cursor()
    try:
        hashed_password = ph.hash(password)
        cursor.execute("INSERT INTO users (username, password) VALUES (?, ?)", (username, hashed_password))
        conn.commit()
        return True
    except sqlite3.IntegrityError:
        return False
    finally:
        conn.close()

def verify_user(username, password):
    """Verifies user credentials."""
    conn = sqlite3.connect("passwords.db")
    cursor = conn.cursor()
    cursor.execute("SELECT password FROM users WHERE username = ?", (username,))
    record = cursor.fetchone()
    conn.close()
    if record:
        try:
            return ph.verify(record[0], password)
        except:
            return False
    return False

def add_password(user_id, service, password):
    """Adds a new password for a service."""
    conn = sqlite3.connect("passwords.db")
    cursor = conn.cursor()
    cursor.execute("INSERT INTO passwords (user_id, service, password) VALUES (?, ?, ?)", (user_id, service, password))
    conn.commit()
    conn.close()

def get_user_id(username):
    """Fetches user ID by username."""
    conn = sqlite3.connect("passwords.db")
    cursor = conn.cursor()
    cursor.execute("SELECT id FROM users WHERE username = ?", (username,))
    record = cursor.fetchone()
    conn.close()
    return record[0] if record else None

def get_passwords(user_id):
    """Fetches all stored passwords for a user."""
    conn = sqlite3.connect("passwords.db")
    cursor = conn.cursor()
    cursor.execute("SELECT service, password FROM passwords WHERE user_id = ?", (user_id,))
    records = cursor.fetchall()
    conn.close()
    return records


def delete_account(user_id):
    """Deletes a user's account and associated data."""
    conn = sqlite3.connect("passwords.db")
    cursor = conn.cursor()
    cursor.execute("DELETE FROM passwords WHERE user_id = ?", (user_id,))
    cursor.execute("DELETE FROM users WHERE id = ?", (user_id,))
    conn.commit()
    conn.close()
