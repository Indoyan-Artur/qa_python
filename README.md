Описание тестов:

Фикстуры:
add_book — создаёт коллектор с двумя книгами (без жанров).
add_genre — ставит жанры: 'Гордость...' → 'Детективы', 'Что делать...' → 'Фантастика'.
add_favorites — добавляет обе книги в избранное.

Тесты:
test_add_new_book_add_existing_book — проверяет, что повторное добавление уже существующей книги не создаёт дубль и не затирает текущее значение: книга остаётся одна, жанр пустой.
test_set_book_genre_add_genre — проверяет, что после установки жанра через set_book_genre метод get_book_genre возвращает именно установленный жанр ('Детективы').
test_get_book_genre_not_valid_name — проверяет, что get_book_genre с несуществующим (пустым) именем возвращает None, а не падает с ошибкой.
test_get_books_with_specific_genre_request_genre — проверяет, что get_books_with_specific_genre('Детективы') возвращает список с одной книгой, у которой этот жанр.
test_get_books_genre_receiving_books_genre — проверяет, что get_books_genre возвращает весь словарь books_genre с обеими книгами и их жанрами.
test_get_books_with_specific_genre_request_detectives — проверяет, что get_books_for_children возвращает только книги с «детскими» жанрами: книга с жанром 'Детективы' (в genre_age_rating) исключается, книга с 'Фантастика' остаётся.
test_add_book_in_favorites_add_in_favorites — проверяет, что после вызова add_book_in_favorites обе книги попадают в список favorites в правильном порядке.
test_delete_book_from_favorites_removal_from_favorites — проверяет, что delete_book_from_favorites удаляет указанную книгу из избранного, и в списке остаётся только другая.
test_get_list_of_favorites_books_get_list_books — проверяет, что get_list_of_favorites_books возвращает полный список избранных книг, совпадающий с ожидаемым.