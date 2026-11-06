import book_system
import member_system
class Loan:
    def __init__(self, loan, book: book_system, member: member_system):
        self.loan = loan
        self.book = book
        self.member = member  
