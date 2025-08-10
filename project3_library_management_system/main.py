# Problem Statement:

# Design a library management system where books can be borrowed, returned, and cataloged.
# Users should have different types of access (regular users and librarians), and the system 
# should ensure that borrowed books are marked unavailable.

# ---------------------------------------------------------------------------------------

# Ideia principal: - Usuários podem ser de dois tipos: leitores e bibliotecários.
#                  - Livros podem ser reservados ou devolvidos, e cada um tem as seguintes
#                    características: título, autor, ano e disponibilidade para reserva.
#                  - Usuários podem reservar livros, devolver livros, ver os livros disponíveis, 
#                    e cada um tem um nome e um ID.
#                  - Leitores podem apenas reservar ou devolver livros.
#                  - Bibliotecários podem reservar e devolver livros, como também adicionar livros
#                    à biblioteca.
#                  - Biblioteca têm um catálogo de livros, e essa classe pode: adicionar livros ao
#                    catálogo, buscar livros nele e exibir o catálogo. -> Atributos recebidos: lista
#                    de livros e lista de usuários.
#                  - EXTRA: Adicionar um histórico de empréstimos por usuário (uma lista simples).

# IDEIAS TRABALHADAS:
# - Composição (classes diferentes para usuários, livros e biblioteca)
# - Polimorfismo (diferentes usuários tem permissões diferentes)
# - Encapsulamento (métodos específicos para cada classe)
# - Dicionários

# --------------------------------------------------------------------------------------


class Book:
    def __init__(self, book_name, book_author, book_year):
        self.book_name = book_name
        self.book_author = book_author
        self.book_year = book_year
        self.available = True
    
    def __str__(self):
        return f"Book({self.book_name}, {self.book_author}, {self.book_year})"

class Library:
    def __init__(self):
        self.catalog = {}

    def add_book(self, book_name, book_author, book_year):
        # GPT helped my dealing with dictionaries, which are a relatively new concept to me
        if book_name in self.catalog:
            self.catalog[book_name]["quantity"] += 1
            print(f"Another book '{book_name}' got added to the library system.")
        else:
            self.catalog[book_name] = {"book_object": Book(book_name, book_author, book_year), "book": book_name, "author": book_author, "year": book_year, "quantity": 1}
            print(f"The book '{book_name}' got added to the library system and is now available to the readers.")

    def show_catalog(self):
        for info in self.catalog.values():
            book = info["book_object"]
            print(f"'{book.book_name}' by {book.book_author} - Quantity: {info['quantity']}")

    def search_book(self, book_name):
        if book_name in self.catalog:
            book_author = self.catalog[book_name]["author"]
            book_year = self.catalog[book_name]["year"]
            quantity = self.catalog[book_name]["quantity"]
            print()
            print("=========================")
            print(f"Book's name: {book_name}")
            print(f"Book's author: {book_author}")
            print(f"Book's year: {book_year}")
            if quantity > 0:
                print(f"Book's availability for borrowing: YES ({quantity} units available).")
            else:
                print("No units available for this book.")
            print("=========================")
            print()
        else:
            print(f"The book '{book_name}' was not found in our system.")
    
    def borrow_book(self, book_name):
        if book_name in self.catalog and self.catalog[book_name]["quantity"] > 0:
            self.catalog[book_name]["quantity"] -= 1
            print(f"You borrowed {book_name}! Good reading!")
            return True
        return False

    def return_book(self, book_name):
        if book_name in self.catalog:
            self.catalog[book_name]["quantity"] += 1
            print(f"The book '{book_name}' has been returned!")
        else:
            print(f"There is no book named '{book_name}' to be returned!")

class User:
    user_dict = {}
    def __init__(self, name, id, type):
        self.registry = []
        self.borrowed = []
        self.name = name
        self.id = id
        self.type = type          # Librarian or reader
        User.user_dict[name] = {"id": id, "type": type, "historic": self.registry, "borrowed": self.borrowed}

    def borrow(self, library, book_name):
        if book_name in library.catalog:
            quantity = library.catalog[book_name]["quantity"]
            if book_name in self.borrowed and quantity > 0:
                print("You already borrowed that book!")
            elif quantity == 0:
                print(f"There is no '{book_name}' available for borrowing!")
            elif library.borrow_book(book_name):
                self.borrowed.append(book_name)
                self.registry.append(book_name)
                print(f"The user {self.name} borrowed the book '{book_name}'.")
        else:
            print("Book not available.")
    
    def return_book(self, library, book_name):
        if book_name in self.borrowed:
            self.borrowed.remove(book_name)
            library.return_book(book_name)
            print(f"The book {book_name} was returned by {self.name}.")
        else:
            print(f"There is no book named '{book_name}' to be returned!")

    @staticmethod
    def create_user(name, id, type):
        type = type.lower()
        if type == "librarian":
            return Librarian(name, id, type)
        elif type == "reader":
            return User(name, id, type)
        else:
            print("Unkown user type.")

class Librarian(User):
    def add_book_to_library(self, library, title, author, year):
        library.add_book(title, author, year)




livro = Book("1984", "eu", 1238)
print(livro)


# Test script for Library System (from GPT)

# Creating library
library = Library()

# Creating users
librarian = User.create_user("Alice", 1, "librarian")
reader1 = User.create_user("Bob", 2, "reader")
reader2 = User.create_user("Charlie", 3, "reader")

# 1) Llbrarian adds books
librarian.add_book_to_library(library, "1984", "George Orwell", 1949)
librarian.add_book_to_library(library, "Brave New World", "Aldous Huxley", 1932)
librarian.add_book_to_library(library, "The Hobbit", "J.R.R. Tolkien", 1937)

# 2) Adding the same book to raise its quantity
librarian.add_book_to_library(library, "1984", "George Orwell", 1949)

# 3) Showing initial catalog
print("\n📚 Initial catalog:")
library.show_catalog()

# 4) Search existing book
print("\n🔍 Search '1984':")
library.search_book("1984")

# 5) Search non-existing book
print("\n🔍 Search 'The Great Gatsby':")
library.search_book("The Great Gatsby")

# 6) User borrows a book
print("\n➡ Bob borrows '1984':")
reader1.borrow(library, "1984")

# 7) User tries to borrow the same book twice
print("\n➡ Bob tries borrowing '1984' again:")
reader1.borrow(library, "1984")

# 8) Other user borrows the same book
print("\n➡ Charlie borrows '1984':")
reader2.borrow(library, "1984")

# 9) User tries to borrow unavailable book
print("\n➡ Bob tries borrowing '1984' again after it runs out:")
reader1.borrow(library, "1984")

# 10) User returns book
print("\n↩ Bob returns '1984':")
reader1.return_book(library, "1984")

# 11) Show final catalog
print("\n📚 Final catalog:")
library.show_catalog()

# 12) User histories
print("\n📜 User histories:")
print(User.user_dict)


# More tests!
print("\n================ STARTING TESTS =================")

# 1) Adding books
print("\n1) Librarian adds books:")
librarian.add_book_to_library(library, "Dune", "Frank Herbert", 1965)
librarian.add_book_to_library(library, "Neuromancer", "William Gibson", 1984)

# 2) Adding copies
print("\n2) Adding more copies of Dune:")
librarian.add_book_to_library(library, "Dune", "Frank Herbert", 1965)

# 3) Showing catalog
print("\n3) Updated catalog:")
library.show_catalog()

# 4) Search existing book
print("\n4) Searching 'Dune':")
library.search_book("Dune")

# 5) Search non-existing book
print("\n5) Searching 'The Lord of the Rings':")
library.search_book("The Lord of the Rings")

# 6) Reader borrows available book
print("\n6) Bob borrows 'Dune':")
reader1.borrow(library, "Dune")

# 7) Reader tries to borrow the same book
print("\n7) Bob tries to borrow 'Dune' again:")
reader1.borrow(library, "Dune")

# 8) Another reader borrows the last copy
print("\n8) Charlie borrows 'Dune':")
reader2.borrow(library, "Dune")

# 9) Try to borrow unavailable book
print("\n9) Bob tries to borrow 'Duna', but it is unavailable:")
reader1.borrow(library, "Dune")

# 10) Bob returns book
print("\n10) Bob returns 'Dune':")
reader1.return_book(library, "Dune")

# 11) Try to return non-borrowed book
print("\n11) Bob tries to return 'Neuromancer' without having it borrowed:")
reader1.return_book(library, "Neuromancer")

# 12) User histories
print("\n12) Final user historic:")
print(User.user_dict)

print("\n================ ENDING TESTS =================")