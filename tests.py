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

    def test_add_new_book_add_same_books_not_add(self):
        collector = BooksCollector()

        # добавляем одинаковые книги
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Гордость и предубеждение и зомби')

        # проверяем, что добавилась только 1 книга
        assert len(collector.get_books_rating()) == 1

    def test_add_book_in_favorites_true(self):
        collector = BooksCollector()
        #сначала добавляем новую книгу, а потом добавляем ее в избранное
        collector.add_new_book('Кот и кот')
        collector.add_book_in_favorites('Кот и кот')
        #проверяем, что наша книга находится в списке избранных
        assert collector.get_list_of_favorites_books() == ['Кот и кот']
        #или проверяем, что список избаранных книг увеличился на 1 assert len(collector.get_list_of_favorites_books()) == 1

    def test_add_book_in_favorites_if_book_not_in_books_rating_empty_dic(self):
        collector = BooksCollector()
        #добавляем свою книгу в избранное
        collector.add_book_in_favorites('Кот и пёс')
        #проверяем, что наша книга не попала в список избранных
        assert collector.books_rating == {} and collector.get_list_of_favorites_books() == []
        #или проверяем, что список избаранных книг не увеличился на 1 assert len(collector.get_list_of_favorites_books()) == 0

    def test_delete_book_in_favorites_true(self):
        collector = BooksCollector()
        #сначала добавляем новую книгу, а потом добавляем ее в избранное
        collector.add_new_book('Кот и кот')
        collector.add_book_in_favorites('Кот и кот')
        #удаляем книгу из избранного списка
        collector.delete_book_from_favorites('Кот и кот')
        #проверяем, что книга удалена из избранного
        assert collector.get_list_of_favorites_books() != ['Кот и кот']

    def test_get_books_with_specific_rating_book_not_in_dic(self):
        collector = BooksCollector()
        collector.set_book_rating('Пёс и пёс', 7)
        assert collector.get_books_with_specific_rating(7) != 'Пёс и пёс'

    def test_set_book_rating_less_than_1(self):
        collector = BooksCollector()
        collector.add_new_book('Пёс')
        collector.set_book_rating('Пёс', -1)
        assert collector.get_book_rating('Пёс') >= 1

    def test_set_book_rating_over_10(self):
        collector = BooksCollector()
        collector.add_new_book('Кот')
        collector.set_book_rating('Кот', 11)
        assert collector.get_book_rating('Кот') <= 10

    def test_get_book_rating_not_add_book_not_add_rating(self):
        collector = BooksCollector()
        assert collector.get_book_rating('Кот') == None


