class Book:
    def __init__(self, title, author, isbn, copies_available):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.copies_available = copies_available

class Member:
    def __init__(self, name, member_id):
        self.name = name
        self.member_id = member_id
        self.borrowed_books = []