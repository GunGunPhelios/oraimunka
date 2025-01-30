import sqlite3

conn=sqlite3.connect("autok.db")
curs=conn.cursor()
# curs.execute("CREATE TABLE IF NOT EXISTS autok (jogositvanyszam TEXT,vasarloneve TEXT, autorendszama TEXT, ar INTEGER, tipus TEXT ) ")
# curs.execute("INSERT INTO autok VALUES ('AB5678920', 'Őz Janka','GG-FA', 3500000 , 'MAZDA') ")
# curs.execute("INSERT INTO autok VALUES ('AT5678967', 'Kurara', 'TA-SU-KE-TE SV-AROG', 60000000,'Renault') ")
# curs.execute("INSERT INTO autok VALUES ('56DF78932', 'Aphelios', 'E-S-T-O-Y CON-TI-GO', 750000, 'BMW') ")
# curs.execute("INSERT INTO autok VALUES ('5678FFG3456', 'Őze Renata Glasc', 'RES-111', 7000000, 'Kicsi Kocsi Audi') ")
# curs.execute("INSERT INTO autok VALUES ('56BB78000', 'Fugue','CLOUD-0', 3500000,'Opel-Astra') ")
# curs.execute("INSERT INTO autok VALUES ('5678675AASD', 'Csizár Robika', 'QIQI-0', 2500000,'Suzuki') ")
# curs.execute("INSERT INTO autok VALUES ('567DDC8921', 'Csillag Patrik','DDUUAAP.10' , 6100000, 'Chevrolet') ")
# curs.execute("INSERT INTO autok VALUES ('567BDQ89440', 'Sánta Vivien', 'UU-DD0', 15000000, 'Mercendes-Benz') ")
# curs.execute("INSERT INTO autok VALUES ('5678AASD9670', 'Vicc Elek Robi', '44AD-0AP', 10000000, 'TESLA') ")
# curs.execute("INSERT INTO autok VALUES ('567DDRT8920', 'Beviz Elek', 'AU-DT-00', 6000000, 'PEUGEOT') ")
# curs.execute("INSERT INTO autok VALUES ('56222DT0', 'Őz János', 'wada-404', 1500000, 'Trabant') ")



curs.execute("SELECT MAX(ar) FROM autok")
curs.execute("SELECT ar FROM autok WHERE ar> 10000000 ")
curs.execute("SELECT vasarloneve FROM autok WHERE vasarloneve Like 'K%'")
curs.execute("SELECT SUM(ar) FROM autok")
curs.execute("SELECT * FROM autok")
print(curs.fetchall())
conn.commit()
conn.close()
