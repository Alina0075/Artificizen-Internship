from libraray import Library

library = Library()
while True:
    print("\n========== Library Management System ==========")
    print("1. Add Book")
    print("2. Add Member")
    print("3. Search Book")
    print("4. Issue Book")
    print("5. Return Book")
    print("6. Display All Books")
    print("7. Display All Members")
    print("8. Exit")

    choice = input("Enter your choice: ")
    try:
        if choice == "1":
            title = input("Enter Book Title: ")
            author = input("Enter Author Name: ")
            isbn = input("Enter ISBN: ")
            copies = int(input("Enter Number of Copies: "))
            library.add_book(title, author, isbn, copies)
            print("\nBook added successfully!")

        elif choice == "2":
            name = input("Enter Member Name: ")
            member_id = input("Enter Member ID: ")
            library.add_member(name, member_id)
            print("\nMember added successfully!")
            
        elif choice == "3":
            isbn = input("Enter ISBN: ")
            book = library.search_book(isbn)
            print("\nBook Found")
            print("-----------------------")
            print(f"Title : {book.title}")
            print(f"Author : {book.author}")
            print(f"ISBN : {book.isbn}")
            print(f"Copies Available : {book.copies_available}")

        elif choice == "4":
            isbn = input("Enter ISBN: ")
            member_id = input("Enter Member ID: ")
            library.issue_book(isbn, member_id)
            print("\nBook issued successfully!")

        elif choice == "5":
            isbn = input("Enter ISBN: ")
            member_id = input("Enter Member ID: ")
            library.return_book(isbn, member_id)
            print("\nBook returned successfully!")

        elif choice == "6":
            library.display_books()

        elif choice == "7":
            library.display_members()

        elif choice == "8":
            print("\nThank you for using Library Management System.")
            break

        else:
            print("\nInvalid choice.")

    except Exception as e:
        print("\nError:", e)