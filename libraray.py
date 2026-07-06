import json
from authors import Book, Member
from exceptions import *

class Library:

    def __init__(self):
        self.books = []
        self.members = []
        self.load_data()

    def add_book(self, title, author, isbn, copies):
        book = Book(title, author, isbn, copies)
        self.books.append(book)
        self.save_data()

    def add_member(self, name, member_id):
        member = Member(name, member_id)
        self.members.append(member)
        self.save_data()
        
    def search_book(self, isbn):
        for book in self.books:
            if book.isbn == isbn:
                return book
        raise BookNotFoundError("Book not found.")

    def search_member(self, member_id):
        for member in self.members:
            if member.member_id == member_id:
                return member
        raise MemberNotFoundError("Member not found.")

    def issue_book(self, isbn, member_id):
        book = self.search_book(isbn)
        member = self.search_member(member_id)
        if book.copies_available == 0:
            raise NoCopiesAvailableError("No copies available.")
        if isbn in member.borrowed_books:
            raise BookAlreadyBorrowedError(
                "Member already borrowed this book."
            )
        member.borrowed_books.append(isbn)

        book.copies_available -= 1
        self.save_data()

    def return_book(self, isbn, member_id):
        book = self.search_book(isbn)
        member = self.search_member(member_id)
        if isbn not in member.borrowed_books:
            raise BookNotBorrowedError(
                "Member never borrowed this book."
            )

        member.borrowed_books.remove(isbn)
        book.copies_available += 1
        self.save_data()

    def display_books(self):
        if len(self.books) == 0:
            print("No books available.")
            return
        for book in self.books:
            print("\n------------------------")
            print(f"Title : {book.title}")
            print(f"Author : {book.author}")
            print(f"ISBN : {book.isbn}")
            print(f"Copies Available : {book.copies_available}")
            
    def display_members(self):
        if len(self.members) == 0:
            print("No members found.")
            return
        for member in self.members:
            print("\n------------------------")
            print(f"Name : {member.name}")
            print(f"Member ID : {member.member_id}")
            print(f"Borrowed Books : {member.borrowed_books}")
            
    def save_data(self):
        data = {
            "books": [],
            "members": []
        }
        for book in self.books:
            data["books"].append({
                "title": book.title,
                "author": book.author,
                "isbn": book.isbn,
                "copies_available": book.copies_available
            })

        for member in self.members:
            data["members"].append({
                "name": member.name,
                "member_id": member.member_id,
                "borrowed_books": member.borrowed_books
            })
        with open("library_data.json", "w") as file:
            json.dump(data, file, indent=4)

    def load_data(self):
        try:
            with open("library_data.json", "r") as file:
                data = json.load(file)
                for book in data["books"]:
                    new_book = Book(
                        book["title"],
                        book["author"],
                        book["isbn"],
                        book["copies_available"]
                    )
                    self.books.append(new_book)
                for member in data["members"]:
                    new_member = Member(
                        member["name"],
                        member["member_id"]
                    )
                    new_member.borrowed_books = member["borrowed_books"]
                    self.members.append(new_member)

        except FileNotFoundError:
            self.books = []
            self.members = []