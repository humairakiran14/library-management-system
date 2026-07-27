from library import Library
import hashlib
import logging

USERNAME = "admin"
PASSWORD_HASH = hashlib.sha256("admin123".encode()).hexdigest()


def login():
    attempts = 3
    while attempts > 0:
        user = input("Username: ")
        pwd = input("Password: ")
        if user == USERNAME and hashlib.sha256(pwd.encode()).hexdigest() == PASSWORD_HASH:
            print("Login successful.\n")
            return True
        attempts -= 1
        print(f"Invalid credentials. Attempts left: {attempts}")
    return False


def menu():
    lib = Library()
    while True:
        print("\n1. Add Book\n2. Add Member\n3. Issue Book\n4. Return Book\n5. Search by Title\n6. Search by Author\n7. Show Available Books\n8. Exit")
        try:
            choice = int(input("Choose an option: "))
        except ValueError:
            print("Please enter a number.")
            continue

        if choice == 1:
            id = input("Book ID: ")
            title = input("Title: ")
            author = input("Author: ")
            lib.add_book(id, title, author)
        elif choice == 2:
            member_id = int(input("Member ID: "))
            name = input("Name: ")
            lib.add_member(member_id, name)
        elif choice == 3:
            id = input("Book ID: ")
            member_id = int(input("Member ID: "))
            lib.issue_book(id, member_id)
        elif choice == 4:
            id = input("Book ID: ")
            member_id = int(input("Member ID: "))
            lib.return_book(id, member_id)
        elif choice == 5:
            keyword = input("Title keyword: ")
            for b in lib.search_by_title(keyword):
                print(b)
        elif choice == 6:
            keyword = input("Author keyword: ")
            for b in lib.search_by_author(keyword):
                print(b)
        elif choice == 7:
            for b in lib.filter_available_books():
                print(b)
        elif choice == 8:
            lib.close()
            print("Goodbye.")
            break
        else:
            print("Invalid option.")


if __name__ == "__main__":
    if login():
        menu()
    else:
        print("Too many failed attempts. Exiting.")
        logging.warning("Login failed - locked out")