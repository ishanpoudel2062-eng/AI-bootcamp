

class Library:
    def __init__(self):
        self.books = []

    def add_book(self):
        book = input("Enter book name: ")
        self.books.append(book)
        print("Book added!")

    def show_books(self):
        if len(self.books) == 0:
            print("No books available.")
        else:
            print("Books in Library:")
            for boook in self.books:
                print(boook)


library = Library()

while True:
    print("1. Add Book")
    print("2. Show Books")
    print("3. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        library.add_book()

    elif choice == "2":
        library.show_books()

    elif choice == "3":
        print("Thank You!")
        break

    else:
        print("Invalid Choice")