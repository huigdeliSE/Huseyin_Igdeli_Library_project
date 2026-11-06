import loan_system
import book_system
import member_system
class Library:
    def __init__(self, name, book: book_system, loan: loan_system, member: member_system):
        self.name = name
        self.Book = book
        self.Member = member
        self.loan = loan
