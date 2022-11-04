from jinja2 import Template
import sqlite3
import library_model

conn = sqlite3.connect("../library.sqlite")

df_publisher = library_model.get_publisher(conn)
df_genre = library_model.get_genre(conn)
df_reader = library_model.get_reader(conn)
df_author = library_model.get_author(conn)

df_book = library_model.get_book(conn)
df_book_author = library_model.get_book_author(conn)
df_book_reader = library_model.get_book_reader(conn)

df_archive = library_model.get_archive(conn)

conn.close()

f_template = open('library_templ.html', encoding='utf-8-sig')
html = f_template.read()
f_template.close()

template = Template(html)
result_html = template.render(
    table_1="publisher",
    relation_1=df_publisher,
    table_2="genre",
    relation_2=df_genre,
    table_3="reader",
    relation_3=df_reader,
    table_4="author",
    relation_4=df_author,
    table_5="book_author",
    relation_5=df_book_author,
    table_6="book",
    relation_6=df_book,
    table_7="book_reader",
    relation_7=df_book_reader,
    table_8="archive",
    relation_8=df_archive,
    len=len
)

f = open('library.html', 'w', encoding='utf-8-sig')
f.write(result_html)
f.close()
