import sqlite3

import pandas as pd


def task1(con: sqlite3.Connection) -> None:
    """
    Вывести книги, которые были взяты в библиотеке в октябре месяце. Указать
    фамилии читателей, которые их взяли, а также дату, когда их взяли. Столбцы назвать
    Название, Читатель, Дата соответственно. Информацию отсортировать сначала по
    возрастанию даты, потом в алфавитном порядке по фамилиям читателей, и, наконец, по
    названиям книг тоже в алфавитном порядке.
    """
    print(pd.read_sql("""
        SELECT b.title as 'Название', r.reader_name as 'Читатель', bg.borrow_date as 'Дата'
        FROM book_reader bg
            JOIN book b on bg.book_id = b.book_id
            JOIN reader r on bg.reader_id = r.reader_id
        WHERE bg.borrow_date like '%-10-%'
        ORDER BY bg.borrow_date, r.reader_name, b.title;
    """, con=con))


def task2(con: sqlite3.Connection, publisher_name: str) -> None:
    """
    Для каждой книги, изданной в заданном издательстве, вывести информацию о ее
    принадлежности к группе:
    - если книга издана раньше 2014 года, вывести "III";
    - если книга издана в период с 2014 года по 2017 год, вывести "II";
    - если книга издана позже 2017 года, вывести "I"
    """
    print(pd.read_sql("""
        SELECT b.title, p.publisher_name,
            CASE
              WHEN b.year_publication < 2014 THEN 'III'
              WHEN b.year_publication <= 2017 THEN 'III'
              WHEN b.year_publication > 2017 THEN 'I'
            END 'Группа'
        FROM book b
        JOIN publisher p on p.publisher_id = b.publisher_id
        where p.publisher_name=:publisher_name;
    """, con=con, params={'publisher_name': publisher_name}))


def task3(con: sqlite3.Connection) -> None:
    """
    Для каждой книги также указать ее жанр и год издания. Столбцы назвать
    Название, Жанр, Год, Группа. Информацию отсортировать сначала по группе в
    порядке убывания, потом возрастанию года издания и, наконец, по названию в алфавитном
    порядке.
    """
    print(pd.read_sql("""
        SELECT b.title as 'Название', g.genre_name as 'Жанр', b.year_publication as 'Год',
            CASE
              WHEN b.year_publication < 2014 THEN 'III'
              WHEN b.year_publication >= 2014 AND b.year_publication <= 2017 THEN 'II'
              WHEN b.year_publication > 2017 THEN 'I'
            END 'Группа'
        FROM book b
        JOIN genre g on g.genre_id = b.genre_id
        ORDER BY 4 desc, b.year_publication ASC, b.title ASC;
    """, con=con))


def task4(con: sqlite3.Connection) -> None:
    """
    Для каждой книги вывести количество экземпляров, которые есть в наличии
    (available_numbers) в библиотеке, а также сколько раз экземпляры книги брали
    читатели. Если книгу читатели не брали - вывести 0. Столбцы назвать Название,
    Количество, Количество_выдачи. Информацию отсортировать сначала по убыванию
    количества выданных экземпляров, а потом по названию книги в алфавитном порядке и,
    наконец, по возрастанию доступного количества.
    """
    print(pd.read_sql("""
        select b.title, b.available_numbers,
            iif(br.book_id is null, 0, COUNT(br.book_id)) as 'Сколько брали'
        from book b
        left join book_reader br on b.book_id = br.book_id
        GROUP BY b.title
        order by 3 desc, b.title, b.available_numbers;
    """, con=con))


def main():
    con = sqlite3.connect("sqlite/library.sqlite")
    task1(con)
    print('-' * 100)
    task2(con, 'ЭКСМО')
    print('-' * 100)
    task3(con)
    print('-' * 100)
    task4(con)
    con.close()


if __name__ == '__main__':
    main()