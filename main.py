# main.py - Главный сервис ИС "Библиотека"
from models import Book, Reader

class LibraryService:
    def __init__(self):
        self.books = []
        self.readers = []

    def add_book(self, title, author, year):
        new_id = len(self.books) + 1
        book = Book(new_id, title, author, year)
        self.books.append(book)
        print(f"[УСПЕХ] Книга добавлена: {book}")

    def register_reader(self, name):
        new_id = len(self.readers) + 1
        reader = Reader(new_id, name)
        self.readers.append(reader)
        print(f"[УСПЕХ] Зарегистрирован: {reader}")

    def show_catalog(self):
        print("\n--- Каталог библиотеки ---")
        for b in self.books:
            print(b)

    def find_book(self, query):
        print(f"\nРезультаты поиска по запросу '{query}':")
        for b in self.books:
            if query.lower() in b.title.lower():
                print(b)	

if __name__ == "__main__":
    lib = LibraryService()
    lib.add_book("Война и мир", "Л.Н. Толстой", 1869)
    lib.add_book("Преступление и наказание", "Ф.М. Достоевский", 1866)
    lib.register_reader("Иванов Иван")
    lib.show_catalog()
    lib.find_book("война")