#CREATE BOOK CLASS
class Book:
    def __init__(self, title, author, availability_status = "available"):
        self.title = title
        self.author = author
        self.availability_status = availability_status

    def __str__(self):
        return "{} by {} is {}".format(self.title, self.author, self.availability_status)

book1 = Book("1984","George Orwell")
book2 = Book("Python Programming","John Smith")
book3 = Book("The Hobbit", "J.R.R. Tolkien")
book4 = Book("Animal Farm", "George Orwell")

#CREATE LIBRARY CLASS TO STORE BOOKS
class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)

    def search(self, search_item):
        matched_book = []
        for book in self.books:
            if search_item.lower() in book.title.lower() or search_item.lower() in book.author.lower():
                matched_book.append(book)

        if not matched_book:
            print(f"No book is found for {search_item}")

        return matched_book

    def check_out(self, search_term):
        matches = self.search(search_term)

        if len(matches) == 0:
            return

        elif len(matches) == 1:
            book = matches[0]
            if book.availability_status == "available":
                book.availability_status = "unavailable"
                print(f"Successfully checked out '{book.title}'")
            else:
                print("it's already checked out")

        else:  # len(matches) > 1
            print(f"Multiple books found for '{search_term}':")
            for i, book in enumerate(matches, 1):
                print(f"{i}. {book}")
            print("Please be more specific in your search.")

    def return_book(self, search_term):
        matches = self.search(search_term)

        if len(matches) == 0:
            return

        elif len(matches) == 1:
            book = matches[0]
            if book.availability_status == "unavailable":
                book.availability_status = "available"
                print(f"Successfully return '{book.title}'")
            else:
                print("it's still checked out")

    def display_books(self):
        available_books = []
        unavailable_books = []
        if not self.books:
            print(f"There is no book in the library")

        for book in self.books:
            if book.availability_status == "available":
                available_books.append(book)
            else:
                unavailable_books.append(book)

        #PRINT AVAILABLE BOOKS
        print(f"There are {len(available_books)} available books")
        print("-" * 50)
        for i, book in enumerate(available_books, 1):
            print(i,".", book)
        #PRINT UNAVAILABLE BOOKS
        print("-" * 50)
        print(f"There are {len(unavailable_books)} unavailable books")
        print("-" * 50)
        for i, book in enumerate(unavailable_books, 1):
            print(i,".", book)



library = Library()
library.add_book(book1)
library.add_book(book2)
library.add_book(book3)
library.add_book(book4)

# print(f"Lirary has {len(library.books)} books")

# print("Searching for '1984':")
# results = library.search("python")
# for book in results:
#     print(book)

library.check_out('1984')
# library.display_books()


print("Searching for 'george':")
results = library.search("george")
for book in results:
    print(book)

# library.check_out('1984')

# library.return_book('1984')
# print("Searching for '1984':")
# results = library.search("1984")
# for book in results:
#     print(book)
