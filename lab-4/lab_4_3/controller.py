from jinja2 import Template
import sqlite3
from model import get_publisher, get_author, get_genre, card

genres = (1, 2, 3)
authors = (2, 3, 4, 5)
publishers = ()
conn = sqlite3.connect("../library.sqlite")
df_author = get_author(conn)
df_publisher = get_publisher(conn)
df_genre = get_genre(conn)
df_card = card(conn, publishers, genres, authors)
conn.close()

f_template = open('template.html')
html = f_template.read()
f_template.close()

template = Template(html)
result_html = template.render(
    authors=df_author,
    publishers=df_publisher,
    genres=df_genre,
    card=df_card,
    sel_authors=authors,
    sel_publishers=publishers,
    sel_genres=genres,
    len=len
)

f = open('result.html', 'w', encoding='utf-8-sig')
f.write(result_html)
f.close()