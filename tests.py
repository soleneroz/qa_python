import pytest
from main import BooksCollector

class TestBooksCollector:
    def test_add_new_book_add_two_books(self):
        collector = BooksCollector()
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')
        assert len(collector.get_books_genre()) == 2


    def test_add_new_book_already_have_book(self):
        collector = BooksCollector()
        collector.add_new_book('100 лет одиночества')
        collector.add_new_book('100 лет одиночества')
        assert len(collector.get_books_genre()) == 1


    def test_set_book_genre_to_already_have_book(self):
        collector = BooksCollector()
        collector.add_new_book('Оно')
        collector.set_book_genre('Оно', 'Ужасы')
        assert collector.get_books_genre() == {'Оно': 'Ужасы'}


    @pytest.mark.parametrize('name', ['Гарри Поттер и Кубок огня', 'Превращение', 'Вторая жизнь Уве'])
    def test_add_new_book_in_list(self, name, book_collection):
        book_collection.add_new_book(name)
        assert name in book_collection.get_books_genre()


    def test_set_book_genre_to_dont_have_book(self):
        collector = BooksCollector()
        collector.set_book_genre('Американский пирог', 'Комедия')
        assert collector.get_books_genre() == {}


    def test_set_book_genre_to_dont_have_genre(self):
        collector = BooksCollector()
        collector.add_new_book('Бедный папа, богатый папа')
        collector.set_book_genre('Бедный папа, богатый папа', 'Биография')
        assert collector.get_books_genre() == {'Бедный папа, богатый папа': ''}


    @pytest.mark.parametrize('name, genre', [('Доктор сон', 'Ужасы'), ('Ведьмак', 'Фантастика')])
    def test_get_book_genre_by_name(self, name, genre):
        collector = BooksCollector()
        collector.add_new_book(name)
        collector.set_book_genre(name, genre)
        assert collector.get_book_genre(name) == genre


    @pytest.mark.parametrize('name, genre', [('Кладбище домашних животных', 'Ужасы')])
    def test_get_books_specific_genre_by_genre(self, name, genre):
        collector = BooksCollector()
        collector.add_new_book(name)
        collector.set_book_genre(name, genre)
        assert collector.get_books_with_specific_genre(genre) == [name]


    def test_get_books_with_specific_genre_by_dont_have_genre(self, my_book_collection):
        assert len(my_book_collection.get_books_with_specific_genre('Биография')) == 0


    def test_add_book_in_favorites_book(self, my_book_collection):
        my_book_collection.add_book_in_favorites('Оно')
        my_book_collection.add_book_in_favorites('Оно')
        assert 'Оно' in my_book_collection.get_list_of_favorites_books() and len(my_book_collection.get_list_of_favorites_books()) == 1

    def test_delete_book_from_favorites(self, my_book_collection):
        my_book_collection.add_book_in_favorites('Ведьмак')
        my_book_collection.delete_book_from_favorites('Ведьмак')
        assert len(my_book_collection.get_list_of_favorites_books()) == 0

    def test_get_books_for_children(self):
        collector = BooksCollector()
        collector.add_new_book('Сказка для детей')
        collector.set_book_genre('Сказка для детей', 'Мультфильмы')
        assert collector.get_books_for_children()
