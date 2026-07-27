class Book:
    def __init__(self, title, author, id, status="Available"):
        self.title = title
        self.author = author
        self.id = id
        self.status = status

    def mark_issued(self):
        self.status = "Issued"

    def mark_returned(self):
        self.status = "Available"

    def display_info(self):
        print(f"Title: {self.title}")
        print(f"Author: {self.author}")
        print(f"id: {self.id}")
        print(f"Status: {self.status}")


