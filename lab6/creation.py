import sqlite3 as sq

with sq.connect("paintings.db") as con:
    cur = con.cursor()

    #Создание таблиц
    cur.execute("CREATE TABLE IF NOT EXISTS artists("
                "id INTEGER PRIMARY KEY AUTOINCREMENT,"
                "name TEXT NOT NULL,"
                "year_of_birth INTEGER"
                ")")
    cur.execute("CREATE TABLE IF NOT EXISTS genres("
                "id INTEGER PRIMARY KEY AUTOINCREMENT,"
                "name TEXT NOT NULL"
                ")")
    cur.execute("CREATE TABLE IF NOT EXISTS paintings("
                "id INTEGER PRIMARY KEY AUTOINCREMENT,"
                "name TEXT NOT NULL,"
                "artist_id INTEGER,"
                "genre_id INTEGER,"
                "year INTEGER,"
                "FOREIGN KEY (artist_id) REFERENCES artists(id),"
                "FOREIGN KEY (genre_id) REFERENCES genres(id)"
                ")")

    #Заполнение таблиц
    cur.execute("INSERT OR IGNORE INTO artists (name, year_of_birth) VALUES "
                "('Claude Monet', 1840),"
                "('Vincent Van Gogh', 1853),"
                "('Leonardo Da Vinci', 1452),"
                "('Pablo Picasso', 1881),"
                "('Kazimir Malevich', 1879),"
                "('Frida Kahlo', 1907),"
                "('Michelangelo', 1475),"
                "('Ayvazovsky', 1817),"
                "('Salvador Dali', 1904),"
                "('Ilya Repin', 1844)")
    cur.execute("INSERT OR IGNORE INTO genres (name) VALUES"
                "('Portrait'),"
                "('Landscape'),"
                "('Abstract'),"
                "('Still-life'),"
                "('Historical'),"
                "('Everyday'),"
                "('Realism'),"
                "('Impressionism'),"
                "('Surrealism'),"
                "('Expressionism'),"
                "('Pop-art'),"
                "('Religious'),"
                "('Cubism')")
    cur.execute("INSERT OR IGNORE INTO paintings (name,artist_id,genre_id,year) VALUES"
                "('Farmyard in Normandy', 1, 2, 1863),"
                "('Spring Flowers', 1, 4, 1864),"
                "('Mona Lisa', 3, 1, 1506),"
                "('The Baptism of Christ', 3, 12, 1448),"
                "('The Starry Night', 2, 2, 1889),"
                "('Sunflowers', 2, 4, 1887),"
                "('Self-Portrait of van Gogh',2 , 1, 1889),"
                "('The Weeping Woman', 4, 13, 1937),"
                "('The Old Guitarist', 4, 8, 1903),"
                "('Black Square', 5, 3, 1915),"
                "('White on White', 5, 3, 1918),"
                "('Self-Portrait with Thorn Necklace and Hummingbird', 6, 9, 1940),"
                "('Frieda and Diego Rivera', 6, 9, 1931),"
                "('Without Hope', 6, 9, 1945),"
                "('The Last Judgment', 7, 12, 1536),"
                "('The Creation of Adam', 7, 12, 1512),"
                "('Sunset at Sea', 8, 2, 1864),"
                "('The Persistence of Memory', 9, 9, 1931),"
                "('The Elephants', 9, 9, 1944),"
                "('Barge Haulers on the Volga', 10, 7, 1873),"
                "('Ivan the Terrible and his Son Ivan, 16 November 1581', 10, 7, 1885),"
                "('Portrait of Pavel Tretyakov', 10, 1, 1883)")
