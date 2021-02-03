# task2_160121
"""
Library
Write a class structure that implements a library. Classes:
1) Library - name, books = [], authors = []
2) Book - name, year, author (author must be an instance of Author class)
3) Author - name, country, birthday, books = []
Library class
Methods:
- new_book(name: str, year: int, author: Author) - returns an instance of Book class and
adds the book to the books list for the current library.
- group_by_author(author: Author) - returns a list of all books grouped by the specified author
- group_by_year(year: int) - returns a list of all the books grouped by the specified year
All 3 classes must have a readable __repr__ and __str__ methods.
Also, the book class should have a class variable which holds the amount of all existing books
"""


class Author:
    def __init__(self, name, country, birthday):
        self.name = name
        self.country = country
        self. birthday = birthday
        self.books = []

    def __str__(self):
        return f'Name: {self.name}\nCountry: {self.country}\nBirthday: {self.birthday},\nBooks: {self.books}'

    def __repr__(self):
        return f'{self.name}'


class Book:
    book_count = 0

    def __init__(self, name, year, author: Author):
        self.name = name
        self.year = year
        self.author = author
        Book.book_count += 1

    def __str__(self):
        return f'Name: {self.name}\nYear: {self.year}\nAuthor: {self.author}'

    def __repr__(self):
        return f'{self.name}'


class Library:
    def __init__(self, name):
        self.name = name
        self.books = []
        self.authors = []

    def __str__(self):
        return f'Name: {self.name}\nBooks: {self.books}\nAuthors: {self.authors}'

    def __repr__(self):
        return f'{self.name}'

    def new_book(self, name: str, year: int, author: Author):
        book = Book(name, year, author)
        if book not in self.books:
            self.books.append(book)
        if book not in author.books:
            author.books.append(book)
        if author not in self.authors:
            self.authors.append(author)
        return book

    def group_by_author(self, author: Author):
        if author in self.authors:
            return author.books

    def group_by_year(self, year: int):
        return [book for book in self.books if book.year == year]


if __name__ == "__main__":
    a1 = Author('Vasya', 'USA', '01012000')
    a2 = Author('Petya', 'UK', '02022001')
    my_library = Library('my_library')
    my_library.new_book('Book1', 2020, a1)
    my_library.new_book('Book2', 2021, a2)
    my_library.new_book('Book3', 2021, a1)
    print(my_library)
    print(my_library.group_by_author(a1))
    print(my_library.group_by_year(2021))



