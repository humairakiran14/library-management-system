class Member:
    def __init__(self,name,member_id):
        self.name=name
        self.member_id=member_id
        self.borrowed_books=[]
        self.fine=0.0


    def borrow_book(self,id):
        self.borrowed_books.append(id)
    def return_book(self,id):
        if id in self.borrowed_books:
            self.borrowed_books.remove(id)
        else:
            print("This book is not borrowed by the member.")


    def calculate_fine(self,days_late,rate_per_day=10):
        if days_late > 0:
            fine_amount=days_late*rate_per_day
            self.fine+=fine_amount
            return fine_amount
        return 0.0
    


