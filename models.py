# models.py - Модели данных ИС "Библиотека"

class Book:
    def __init__(self, book_id, title, author, year):
        self.book_id = book_id
        self.title = title
        self.author = author
        self.year = year

    def __str__(self):
        return f"[{self.book_id}] '{self.title}' — {self.author} ({self.year} г.)"

class Reader:
    def __init__(self, reader_id, name):
        self.reader_id = reader_id
        self.name = name

    def __str__(self):
        return f"Читатель №{self.reader_id}: {self.name}"