import sqlite3

def init_db():
    conn = sqlite3.connect("library.db")
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS books (
            id TEXT PRIMARY KEY,
            title TEXT,
            author TEXT,
            status TEXT
        )
    """)

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS members (
            member_id INTEGER PRIMARY KEY,
            name TEXT,
            fine REAL
        )
    """)

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS issued_books (
            book_id TEXT,
            member_id INTEGER,
            issue_date TEXT
        )
    """)

    conn.commit()
    conn.close()

if __name__ == "__main__":
    init_db()
    print("Database initialized.")