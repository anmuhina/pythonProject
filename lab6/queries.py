import sqlite3 as sq

with sq.connect("paintings.db") as con:
    cur = con.cursor()

    # Запросы select
    cur.execute("SELECT name, year FROM paintings WHERE year<1800")
    res1 = cur.fetchall()
    print("Произведения, написанные ранее 1800 года:")
    for res in res1:
        print(res)
    print("\n")

    cur.execute("SELECT name FROM paintings "
                "WHERE artist_id = (SELECT id FROM artists WHERE name = 'Vincent Van Gogh')")
    res2 = cur.fetchall()
    print("Произведения Ван Гога:")
    for res in res2:
        print(res)
    print("\n")

    cur.execute("SELECT p.name AS painting_name, a.name AS artist_name "
                 "FROM paintings p "
                 "JOIN artists a ON p.artist_id = a.id "
                 "JOIN genres g ON p.genre_id = g.id "
                 "WHERE g.name = 'Landscape'")
    res3 = cur.fetchall()
    print("Все пейзажи:")
    for res in res3:
        print(res)
    print("\n")

    cur.execute("SELECT * FROM genres")
    res4 = cur.fetchall()
    print("Все жанры:")
    for res in res4:
        print(res)
    print("\n")


    '''# Выбор всех картин вместе с художниками и жанрами
    cur.execute("""SELECT p.name AS painting_name, p.year AS painting_year, a.name AS artist_name, g.name AS genre_name
                     FROM paintings p
                     JOIN artists a ON p.artist_id = a.id
                     JOIN genres g ON p.genre_id = g.id
                     """)
    res = cur.fetchall()
    for i in res:
        print(i)'''
