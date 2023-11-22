import sqlite3

def create_table():
    conn = sqlite3.connect("user_data.db")
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT,
            password TEXT,
            apples_price REAL,
            book_price REAL,
            car_price REAL
        )
    ''')
    conn.commit()
    conn.close()

def save_user_data(username, password, apples_price, book_price, car_price):
    conn = sqlite3.connect("user_data.db")
    cursor = conn.cursor()
    cursor.execute('''
        INSERT INTO users (username, password, apples_price, book_price, car_price)
        VALUES (?, ?, ?, ?, ?)
    ''', (username, password, apples_price, book_price, car_price))
    conn.commit()
    conn.close()
