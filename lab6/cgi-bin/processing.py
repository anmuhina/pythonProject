#!/usr/bin/env python3
import sqlite3 as sq
import cgi
import cgitb
cgitb.enable()

form = cgi.FieldStorage()
artistName = form.getfirst("ArtistName", "empty")
print(artistName)
artistBirthYear = form.getfirst("ArtistBirthYear", "empty")
paintingName = form.getfirst("PaintingName", "empty")
paintingYear = form.getfirst("PaintingYear", "empty")
genre = form.getfirst("Genre", "empty")


# Проверка и вставка данных формы в бд
with sq.connect("paintings.db") as con:
    cur = con.cursor()

    cur.execute("SELECT id FROM artists WHERE LOWER(name) = ?", (artistName.lower(),))
    res1 = cur.fetchone()
    if res1 is None:
        cur.execute("""INSERT INTO artists (name, year_of_birth) 
                VALUES (?, ?)""", (artistName, artistBirthYear))
        artistId = cur.lastrowid
    else:
        artistId = res1[0]

    cur.execute("SELECT id FROM genres WHERE LOWER(name) = ?", (genre.lower(),))
    res2 = cur.fetchone()
    if res2 is None:
        cur.execute("""INSERT INTO genres (name)
                    VALUES (?)""", (genre,))
        genreId = cur.lastrowid
    else:
        genreId = res2[0]

    cur.execute("SELECT id FROM paintings WHERE LOWER(name) = ?", (paintingName.lower(),))
    res3 = cur.fetchone()
    if res3 is None:
        cur.execute("""INSERT INTO paintings (name,artist_id,genre_id,year) 
                    VALUES (?, ?, ?, ?)""", (paintingName, artistId, genreId, paintingYear))

    cur.execute("""SELECT p.name AS painting_name, p.year AS painting_year, a.name AS artist_name, g.name AS genre_name
                 FROM paintings p
                 JOIN artists a ON p.artist_id = a.id
                 JOIN genres g ON p.genre_id = g.id
                 """)
    paintingsList =cur.fetchall()


# Вывод данных таблиц на экран
print("Content-type: text/html\n")
print("""<!DOCTYPE HTML>
<html>
<head>
<meta charset="utf-8">
<title>Обработка данных</title>
</head>
<body>""")
print('<h2 style="color: #f213a8;">Ваша форма успешно отправлена!</h2>')
print("\n<h1>Все картины:</h1>")

print("<ol>")
for painting in paintingsList:
    print(f"<li>Название картины: '{painting[0]}'")
    print("<ul>")
    print(f"<li>Год написания: {painting[1]}</li>")
    print(f"<li>Художник: {painting[2]}</li>")
    print(f"<li>Направление живописи: {painting[3]}</li>")
    print("</ul>")
    print("</li>")
print("</ol>")

print("""</body>
</html>
""")
