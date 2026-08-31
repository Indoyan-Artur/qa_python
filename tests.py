import pytest


from main import BooksCollector

# класс TestBooksCollector объединяет набор тестов, которыми мы покрываем наше приложение BooksCollector
# обязательно указывать префикс Test
class TestBooksCollector:

    # пример теста:
    # обязательно указывать префикс test_
    # дальше идет название метода, который тестируем add_new_book_
    # затем, что тестируем add_two_books - добавление двух книг
    def test_add_new_book_add_two_books(self):
        # создаем экземпляр (объект) класса BooksCollector
        collector = BooksCollector()

        # добавляем две книги
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')

        # проверяем, что добавилось именно две
        # словарь books_rating, который нам возвращает метод get_books_rating, имеет длину 2
        assert len(collector.get_books_rating()) == 2
    # напиши свои тесты ниже
    # чтобы тесты были независимыми в каждом из них создавай отдельный экземпляр класса BooksCollector()

    # фикстура добавления книги
    @pytest.fixture
    def add_book(self):
        collector = BooksCollector()
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Что делать, если ваш кот хочет вас любить')
        return collector

    #фикстура добавление жанра
    @pytest.fixture
    def add_genre(self, add_book):
        name_detective = ('Гордость и предубеждение и зомби')
        name_fantasy  = ('Что делать, если ваш кот хочет вас любить')
        add_book.set_book_genre(name_detective, 'Детективы')
        add_book.set_book_genre(name_fantasy, 'Фантастика')
        return add_book

    @pytest.fixture
    def add_favorites(self, add_book, add_genre):
        name_detective = ('Гордость и предубеждение и зомби')
        name_fantasy  = ('Что делать, если ваш кот хочет вас любить')
        add_book.add_book_in_favorites(name_detective)
        add_book.add_book_in_favorites(name_fantasy)
        return add_book

    # проверяем, что книга не добавится если такая книга уже есть
    def test_add_new_book_add_existing_book(self, add_book):
        name = ('Гордость и предубеждение и зомби')
        add_book.add_new_book(name)
        genres = add_book.get_books_genre()

        assert name in genres 
        assert list(genres.keys()).count(name) == 1
        assert genres[name] == '' 

    #проверка устанавливки жанра
    def test_set_book_genre_add_genre(self, add_book, add_genre):
        name = ('Гордость и предубеждение и зомби')

        assert add_book.get_book_genre(name) == 'Детективы'

    #Поскольку тест выше еще и тестирует получение жанра книги, протестируем, что метод get_book_genre не падает с ошибкое если передали пустой name
    def test_get_book_genre_not_valid_name(self, add_book, add_genre):
        name = ('')
        result = add_book.get_book_genre(name)

        assert result is None

    # Проверяем, что метод get_books_with_specific_genre возвращает имена тех жанров которые запрашиваем
    def test_get_books_with_specific_genre_request_genre(self, add_book, add_genre):
        name = ('Гордость и предубеждение и зомби')
        genre = ('Детективы')
        result = add_book.get_books_with_specific_genre(genre)

        assert result == [name]

    # проверка получения словаря books_genre
    def test_get_books_genre_receiving_books_genre(self, add_book, add_genre):
        result = add_book.get_books_genre()
        expected = {'Гордость и предубеждение и зомби': 'Детективы', 'Что делать, если ваш кот хочет вас любить': 'Фантастика'}

        assert result == expected

    # проверка возвращения только детских жанров
    def test_get_books_with_specific_genre_request_detectives(self, add_book, add_genre):
        expected = ['Что делать, если ваш кот хочет вас любить']
        result = add_book.get_books_for_children()
        assert result == expected

    # проверка добавления книги в избранное
    def test_add_book_in_favorites_add_in_favorites(self, add_book, add_genre, add_favorites):
        names = ['Гордость и предубеждение и зомби', 'Что делать, если ваш кот хочет вас любить']

        assert add_book.favorites == names

    # проверка удаления книги из избранного
    def test_delete_book_from_favorites_removal_from_favorites(self, add_book, add_genre, add_favorites):
        removal = ('Гордость и предубеждение и зомби')
        name = ('Что делать, если ваш кот хочет вас любить')
        add_book.delete_book_from_favorites(removal)

        assert add_book.favorites == [name]

    # проверка получения списка избранных книг
    def test_get_list_of_favorites_books_get_list_books(self, add_book, add_genre, add_favorites):
        names = ['Гордость и предубеждение и зомби', 'Что делать, если ваш кот хочет вас любить']
        result = add_book.get_list_of_favorites_books()
        assert result == names
