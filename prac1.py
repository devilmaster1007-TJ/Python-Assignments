class book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.available = True

class patron:
    def __init__(self, name):
        self.name = name
        self.borrowed_books = []

class library:
    def __init__(self):
        self.books = []
        self.patrons = []

    def add_book(self, book):
        self.books.append(book)

    print(book.title,"added successfully.")

    def register_patron(self, patron):
        self.patrons.append(patron)
        print(patron.name,"registered successfully.")

    def borrow_book(self, patron, book):
        if  book.available:
            book.available = False
            print(patron.name,"borrowed",book.title)
        else:
            print(book.title,"is not available for borrowing.")

            def return_book(self, patron, book):
                if book in patron.borrowed_books:
                    book.available = True
                    patron.borrowed_books.remove(book)
                    print(patron.name,"returned",book.title)
                else:
                    print(patron.name,"has not borrowed",book.title)

                    library = library()
                    book1 = book("The Great Gatsby", "F. Scott Fitzgerald")
                    book2 = book("To Kill a Mockingbird", "Harper Lee")
                    book3 = book("1984", "George Orwell")

                    library.add_book(book1)
                    library.add_book(book2)
                    library.add_book(book3)

                    print()

                    patron1 = patron("Ramesh")
                    patron2 = patron("Bobby")

                    library.register_patron(patron1)
                    library.register_patron(patron2)

                    print()

                    library.borrow_book(patron1, book1)
                    library.borrow_book(patron2, book2)

                    print()

                    library.borrow_book(patron2, book1)
                    print()
                    library.return_book(patron1, book1)
                    print()
                    library.borrow_book(patron2, book1)
                    print()

                    print("-----Final Status-----")
                    print("\nBooks Available:")
                    for book in library.books:
                        print(book.title, "-", book.available)
                    print("\nBooks Borrowed:")
                    for patron in library.patrons:
                        print(patron.name, "has borrowed:")
                        if len(patron.borrowed_books) == 0:
                            print("No books borrowed.")
                        else:
                            for book in patron.borrowed_books:
                                print(book.title)