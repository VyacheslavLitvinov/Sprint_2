# qa_python
test_add_new_book_add_two_books проверка добавления 2 книг
test_add_new_book_add_same_books_not_add - проверка того, что одиннаковые книги не добавляются
test_add_book_in_favorites_true - проверка добавления книги в избранное
test_add_book_in_favorites_if_book_not_in_books_rating_empty_dic - проверка, что нельзя добавить книгу в избранное, если её нет в словаре books_rating.
test_delete_book_in_favorites_true - проверка удаления книги из избранного
test_get_books_with_specific_rating_book_not_in_dic - нельзя выставить рейтинг книге, которой нет в списке
test_set_book_rating_less_than_1 - нельзя выставить рейтинг меньше 1
test_set_book_rating_over_10 - нельзя выставить рейтинг больше 10
test_get_book_rating_not_add_book_not_add_rating - проверка, что у не добавленной книги нет рейтинга