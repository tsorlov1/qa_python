import pytest


from main import BooksCollector

# класс TestBooksCollector объединяет набор тестов, которыми мы покрываем наше приложение BooksCollector
# обязательно указывать префикс Test
class TestBooksCollector:

    def test_add_new_book_two_books_add_two_books(self):
        book_collector = BooksCollector()
        book_collector.add_new_book('Зомби')
        book_collector.add_new_book('Ирония')
        assert len(book_collector.books_genre) == 2

    @pytest.mark.parametrize('name', ['Космос', 'Крик', 'Поиск', 'Мульти', 'Смех'])
    def test_add_new_book_name_book_not_genre(self, name):
        book_collector = BooksCollector()
        book_collector.add_new_book(name)
        assert book_collector.books_genre == {name: ''}

    @pytest.mark.parametrize('name, genre', [['Космос', 'Фантастика'], ['Крик', 'Ужасы'], ['Поиск', 'Детективы'], ['Мульти', 'Мультфильмы'], ['Смех', 'Комедии']])
    def test_set_book_genre_name_and_genre_book_add_genre(self, name, genre):
        book_collector = BooksCollector()
        book_collector.add_new_book(name)
        book_collector.set_book_genre(name, genre)
        assert book_collector.books_genre == {name: genre}

    @pytest.mark.parametrize('name, genre', [['Космос', 'Фантастика'], ['Крик', 'Ужасы'], ['Поиск', 'Детективы'], ['Мульти', 'Мультфильмы'], ['Смех', 'Комедии']])
    def test_get_book_genre_name_and_genre_book_get_genre(self, name, genre):
        book_collector = BooksCollector()
        book_collector.add_new_book(name)
        book_collector.set_book_genre(name, genre)
        assert book_collector.get_book_genre(name) == genre

    @pytest.mark.parametrize('name, genre', [['Космос', 'Фантастика'], ['Крик', 'Ужасы'], ['Поиск', 'Детективы'], ['Мульти', 'Мультфильмы'], ['Смех', 'Комедии']])
    def test_get_books_with_specific_genre_name_and_genre_book_get_book(self, name, genre):
        book_collector = BooksCollector()
        book_collector.add_new_book(name)
        book_collector.set_book_genre(name, genre)
        assert book_collector.get_books_with_specific_genre(genre) == [name]

    @pytest.mark.parametrize('name, genre', [['Космос', 'Фантастика'], ['Крик', 'Ужасы'], ['Поиск', 'Детективы'], ['Мульти', 'Мультфильмы'], ['Смех', 'Комедии']])
    def test_get_books_genre_name_and_genre_book_genre_books(self, name, genre):
        book_collector = BooksCollector()
        book_collector.add_new_book(name)
        book_collector.set_book_genre(name, genre)
        assert book_collector.get_books_genre() == {name: genre}

    @pytest.mark.parametrize('name, genre', [['Космос', 'Фантастика'], ['Мульти', 'Мультфильмы'], ['Смех', 'Комедии']])
    def test_get_books_for_children_name_and_genre_book_add_books_for_children(self, name, genre):
        book_collector = BooksCollector()
        book_collector.add_new_book(name)
        book_collector.set_book_genre(name, genre)
        assert book_collector.get_books_for_children() == [name]

    @pytest.mark.parametrize('name, genre', [['Крик', 'Ужасы'], ['Поиск', 'Детективы']])
    def test_get_books_for_children_forbidden_genre_not_add_books_for_children(self, name, genre):
        book_collector = BooksCollector()
        book_collector.add_new_book(name)
        book_collector.set_book_genre(name, genre)
        assert book_collector.get_books_for_children() == []

    @pytest.mark.parametrize('name', ['Космос', 'Крик', 'Поиск', 'Мульти', 'Смех'])
    def test_add_book_in_favorites_name_book_add_favorites(self, name):
        book_collector = BooksCollector()
        book_collector.add_new_book(name)
        book_collector.add_book_in_favorites(name)
        assert book_collector.favorites == [name]

    @pytest.mark.parametrize('name', ['Космос', 'Крик', 'Поиск', 'Мульти', 'Смех'])
    def test_delete_book_in_favorites_name_book_delete_favorites(self, name):
        book_collector = BooksCollector()
        book_collector.add_new_book(name)
        book_collector.add_book_in_favorites(name)
        book_collector.delete_book_from_favorites(name)
        assert book_collector.favorites == []

    @pytest.mark.parametrize('name', ['Космос', 'Крик', 'Поиск', 'Мульти', 'Смех'])
    def test_get_list_of_favorites_books_name_book_get_list(self, name):
        book_collector = BooksCollector()
        book_collector.add_new_book(name)
        book_collector.add_book_in_favorites(name)
        assert book_collector.favorites == [name]
