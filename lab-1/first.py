import sqlite3

import pandas as pd


def task1(con: sqlite3.Connection) -> None:
    """
    Для каждого жанра посчитать, сколько различных книг этого жанра представлено в
    библиотеке, каково общее количество доступных экземпляров книг (имеющихся в наличии)
    и какой самый ранний год издания книг, относящихся к этому жанру. Информацию
    отсортировать по названию жанра в алфавитном порядке
    """
    print(pd.read_sql("""        
        SELECT g.genre_name, COUNT(b.book_id) AS count, min(b.year_publication) AS year, sum(b.available_numbers) as sum
        FROM book b
            JOIN genre g ON b.genre_id = g.genre_id
        GROUP BY b.genre_id
        ORDER BY g.genre_name
    """, con=con))


def task2(con: sqlite3.Connection, reader_name: str) -> None:
    """
    Вывести информацию о всех книгах, которые сдал заданный читатель. Для каждой
    книги указать дату выдачи, дату сдачи и сколько дней книга была на руках. Информацию
    отсортировать по убыванию количества дней.
    """
    print(pd.read_sql("""
        SELECT
            b.title AS book,
            br.borrow_date,
            br.return_date,
            julianday(br.return_date) - julianday(br.borrow_date) AS days
        FROM book_reader br
            JOIN book b ON br.book_id = b.book_id
            JOIN reader r ON br.reader_id = r.reader_id
        WHERE r.reader_name = :reader_name
          AND br.return_date IS NOT NULL
        ORDER BY days DESC
    """, con=con, params={'reader_name': reader_name}))


def task3(con: sqlite3.Connection) -> None:
    """
    Вывести самый популярный жанр (жанры). Самым популярным считается жанр,
    книги которого чаще всего брали читатели в библиотеке. Вывести название жанра (жанров) и
    сколько раз читатели брали книги этого жанра. Информацию отсортировать по названию
    жанров в алфавитном порядке.
    """
    print(pd.read_sql("""
        WITH most_popular AS (SELECT MAX(count) AS max
                              FROM (SELECT COUNT(b.book_id) AS count
                                    FROM genre g
                                        JOIN book b ON b.genre_id = g.genre_id
                                        JOIN book_reader br ON br.book_id = b.book_id
                                    GROUP BY g.genre_id))
        SELECT g.genre_name, COUNT(b.book_id) AS count
        FROM genre g, most_popular
            JOIN book b ON b.genre_id = g.genre_id
            JOIN book_reader br ON br.book_id = b.book_id
        GROUP BY g.genre_id
        HAVING count = most_popular.max
        ORDER BY g.genre_name
    """, con=con))


def main():
    con = sqlite3.connect("sqlite/library.sqlite")
    task1(con)
    print('-' * 100)
    task2(con, 'Петров Ф.С.')
    print('-' * 100)
    task3(con)
    con.close()


if __name__ == '__main__':
    main()