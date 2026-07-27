import sqlite3
from datetime import date
import logging

logging.basicConfig(
    filename="library.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)


class BookNotAvailableError(Exception):
    pass


class Library:
    def __init__(self, db_name="library.db"):
        self.conn = sqlite3.connect(db_name)
        self.cursor = self.conn.cursor()

    def add_book(self, id, title, author):
        self.cursor.execute(
            "INSERT INTO books (id, title, author, status) VALUES (?, ?, ?, ?)",
            (id, title, author, "Available")
        )
        self.conn.commit()
        logging.info(f"Book added: {title} ({id})")

    def add_member(self, member_id, name):
        self.cursor.execute(
            "INSERT INTO members (member_id, name, fine) VALUES (?, ?, ?)",
            (member_id, name, 0.0)
        )
        self.conn.commit()
        logging.info(f"Member added: {name} ({member_id})")

    def find_book(self, id):
        self.cursor.execute("SELECT * FROM books WHERE id = ?", (id,))
        return self.cursor.fetchone()

    def find_member(self, member_id):
        self.cursor.execute("SELECT * FROM members WHERE member_id = ?", (member_id,))
        return self.cursor.fetchone()

    def issue_book(self, id, member_id):
        try:
            book = self.find_book(id)
            member = self.find_member(member_id)

            if book is None:
                raise ValueError("Book not found.")
            if member is None:
                raise ValueError("Member not found.")
            if book[3] == "Issued":
                raise BookNotAvailableError(f"'{book[1]}' is already issued.")

            self.cursor.execute("UPDATE books SET status = ? WHERE id = ?", ("Issued", id))
            self.cursor.execute(
                "INSERT INTO issued_books (book_id, member_id, issue_date) VALUES (?, ?, ?)",
                (id, member_id, str(date.today()))
            )
            self.conn.commit()
            print(f"'{book[1]}' issued to {member[1]}.")
            logging.info(f"Issued '{book[1]}' to {member[1]}")

        except (ValueError, BookNotAvailableError) as e:
            print(f"Error: {e}")
            logging.error(str(e))

    def return_book(self, id, member_id):
        try:
            book = self.find_book(id)
            member = self.find_member(member_id)

            if book is None:
                raise ValueError("Book not found.")
            if member is None:
                raise ValueError("Member not found.")
            if book[3] != "Issued":
                raise ValueError("This book was not issued.")

            self.cursor.execute(
                "SELECT issue_date FROM issued_books WHERE book_id = ? AND member_id = ?",
                (id, member_id)
            )
            row = self.cursor.fetchone()
            issue_date = date.fromisoformat(row[0])
            days_borrowed = (date.today() - issue_date).days
            days_late = days_borrowed - 14

            fine = 0.0
            if days_late > 0:
                fine = days_late * 10
                self.cursor.execute(
                    "UPDATE members SET fine = fine + ? WHERE member_id = ?",
                    (fine, member_id)
                )

            self.cursor.execute("UPDATE books SET status = ? WHERE id = ?", ("Available", id))
            self.cursor.execute(
                "DELETE FROM issued_books WHERE book_id = ? AND member_id = ?",
                (id, member_id)
            )
            self.conn.commit()

            print(f"'{book[1]}' returned by {member[1]}.")
            if fine > 0:
                print(f"Late fine charged: {fine}")
            else:
                print("No fine, returned on time.")
            logging.info(f"Returned '{book[1]}' by {member[1]}, fine: {fine}")

        except ValueError as e:
            print(f"Error: {e}")
            logging.error(str(e))

    def search_by_title(self, keyword):
        self.cursor.execute("SELECT * FROM books WHERE title LIKE ?", (f"%{keyword}%",))
        return self.cursor.fetchall()

    def search_by_author(self, keyword):
        self.cursor.execute("SELECT * FROM books WHERE author LIKE ?", (f"%{keyword}%",))
        return self.cursor.fetchall()

    def filter_available_books(self):
        self.cursor.execute("SELECT * FROM books WHERE status = ?", ("Available",))
        return self.cursor.fetchall()

    def close(self):
        self.conn.close()