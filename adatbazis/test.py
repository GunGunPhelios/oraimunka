import sqlite3
#Adatbazis létrehozás
conn=sqlite3.connect("felhasznalo.db")
curs=conn.cursor()
#Tábla létrehozás
curs.execute("CREATE TABLE IF NOT EXISTS szemely (nev TEXT, kor INTEGER, nem TEXT)")
#Tábla feltöltése adatokkal
#curs.execute("INSERT INTO szemely Values ('John', 32, 'ferfi')")
#curs.execute("INSERT INTO szemely Values ('Erica', 43, 'no')")
#curs.execute("INSERT INTO szemely Values ('Leonard', 52, 'ferfi')")
#curs.execute("INSERT INTO szemely Values ('Kinga', 23, 'no')")
#curs.execute("INSERT INTO szemely Values ('Emily', 25, 'no')")
#curs.execute("INSERT INTO szemely Values ('Edward', 27, 'ferfi')")


#Adatok megjelenítése a tábláról
curs.execute("SELECT * FROM szemely")
#Adatok módosítása
curs.execute("SELECT nev,kor FROM szemely WHERE kor>50")
curs.execute("UPDATE szemely SET nem=? WHERE nem=?" , ('nő', 'no'))
curs.execute("DELETE FROM szemely WHERE RowID=11")
print(curs.fetchall())
#Adatok mentése
conn.commit()

conn.close()

