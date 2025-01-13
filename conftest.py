import pytest
from main import BooksCollector

@pytest.fixture
def my_book_collection(book_collection):
    collection = book_collection
    books = ['100 лет одиночества', 'Ведьмак', 'Капоте', 'Сказка для детей', 'Оно']
    genre = ['Драма', 'Ужасы', 'Фантастика', 'Детектив', 'Мультфильмы']
    for i in range(5):
        collection.add_new_book(books[i])
    for i in range(5):
        collection.set_book_genre(books[i], genre[i])
    return collection


@pytest.fixture
def book_collection():
    book_collection = BooksCollector()
    return book_collection