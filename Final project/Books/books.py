import re

class Book:
    def __init__(self, title, author, genre):
        self.title = title
        self.author = author
        self.genre = genre
        self.available = True

    def display_info(self):
        print(f"Title: {self.title}")
        print(f"Author: {self.author}")
        print(f"Genre: {self.genre}")
        print(f"Available: {'Yes' if self.available else 'No'}")
        print("---------")


class BookManager:
    def __init__(self):
        self.library = []

    def validate_input(self, prompt):
        while True:
            value = input(prompt).strip()
            if re.match("^[a-zA-Z ]+$", value):
                return value
            print("Invalid input! Use letters and spaces only.")

    def add_book(self):
        title = input("Enter book title: ").strip()
        author = self.validate_input("Enter author's name: ")
        genre = self.validate_input("Enter genre: ")
        self.library.append(Book(title, author, genre))
        print("Book added!\n")

    def display_books(self):
        if not self.library:
            print("No books in library.\n")
        else:
            for book in self.library:
                book.display_info()

    def search_book(self):
        title = input("Enter title to search: ").strip()
        for book in self.library:
            if book.title.lower() == title.lower():
                book.display_info()
                return
        print("Book not found.\n")

    def update_book(self):
        title = input("Enter title to update: ").strip()
        for book in self.library:
            if book.title.lower() == title.lower():
                book.author = self.validate_input("Enter new author's name: ")
                book.genre = self.validate_input("Enter new genre: ")
                print("Book updated!\n")
                return
        print("Book not found.\n")

    def remove_book(self):
        title = input("Enter title to remove: ").strip()
        for book in self.library:
            if book.title.lower() == title.lower():
                self.library.remove(book)
                print("Book removed!\n")
                return
        print("Book not found.\n")

    def borrow_book(self):
        title = input("Enter title to borrow: ").strip()
        for book in self.library:
            if book.title.lower() == title.lower():
                if book.available:
                    book.available = False
                    print("Book borrowed!\n")
                else:
                    print("Book already borrowed.\n")
                return
        print("Book not found.\n")

    def return_book(self):
        title = input("Enter title to return: ").strip()
        for book in self.library:
            if book.title.lower() == title.lower():
                if not book.available:
                    book.available = True
                    print("Book returned!\n")
                else:
                    print("Book already available.\n")
                return
        print("Book not found.\n")

    def sort_books(self):
        criterion = input("Sort by (title/author/genre): ").strip().lower()
        if criterion in ["title", "author", "genre"]:
            self.library.sort(key=lambda x: getattr(x, criterion).lower())
            print(f"Books sorted by {criterion}!\n")
        else:
            print("Invalid sort criterion.\n")

    def total_books(self):
        print(f"Total books: {len(self.library)}\n")


def main():
    manager = BookManager()

    while True:
        print("\n--- Library Menu ---")
        print("1. Add Book")
        print("2. Display All Books")
        print("3. Search Book")
        print("4. Update Book")
        print("5. Remove Book")
        print("6. Sort Books")
        print("7. Borrow Book")
        print("8. Return Book")
        print("9. Total Books")
        print("0. Exit")

        choice = input("Choose option (0-9): ").strip()

        if choice == "1":
            manager.add_book()
        elif choice == "2":
            manager.display_books()
        elif choice == "3":
            manager.search_book()
        elif choice == "4":
            manager.update_book()
        elif choice == "5":
            manager.remove_book()
        elif choice == "6":
            manager.sort_books()
        elif choice == "7":
            manager.borrow_book()
        elif choice == "8":
            manager.return_book()
        elif choice == "9":
            manager.total_books()
        elif choice == "0":
            print("Goodbye!")
            break
        else:
            print("Invalid option. Try again.\n")


if __name__ == "__main__":
    main()
