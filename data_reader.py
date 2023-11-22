import sqlite3

def read_user_data(database_file="user_data.db"):
    conn = sqlite3.connect(database_file)
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM users")
    rows = cursor.fetchall()

    conn.close()

    return rows

def print_user_data(rows):
    print("ID  | Username | Password | Apples Price | Book Price | Car Price")
    print("----|----------|----------|--------------|------------|----------")
    for row in rows:
        print(f"{row[0]:<3} | {row[1]:<8} | {row[2]:<8} | {row[3]:<12} | {row[4]:<10} | {row[5]:<8}")

# Example usage:
if __name__ == "__main__":
    data = read_user_data()
    print_user_data(data)
