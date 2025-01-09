from datetime import datetime
class Viragbolt:
    def __init__(self):
        self.lista=[]
    def beolvas(self):
        with open("viragok.txt", "r", encoding="UTF-8") as fajl:
            adatok= fajl.readlines()
        for adat in adatok:
            adat=adat.strip()
            adat=adat.split(";")
            virag=adat[0]
            ar=int(adat[1])
            mennyiseg=int(adat[2])
            szallitas=datetime.strptime(adat[3],"%Y-%m-%d")
            self.lista.append([virag,ar,mennyiseg,szallitas])
        for item in self.lista:
            print(f"{item[0]}, {item[1]} Ft, {item[2]} darab, Szállítás: {item[3]}")    
    def legdragabb(self):
        legdragabb_ar=0
        legdragabb_virag=""
        for dragabb in self.lista:
            if dragabb[1] >legdragabb_ar:
                legdragabb_ar= dragabb[1]
                legdragabb_virag= dragabb[0]
        print(f"A legdrágább virág: {legdragabb_virag} - {legdragabb_ar} Ft")

    def atlag(self):
        db_atlaga=[]
        for a in self.lista:
            db_atlaga.append(a[2])
        print(f"Az eladott virágok átlagos darabszáma: {sum(db_atlaga)/len(db_atlaga)} darab")
    def r_kezdodik(self):
        megszamol=0
        with open("rbetusviragok.txt", "w",encoding="UTF-8") as file:
            for r in self.lista:
                if r[0].startswith("R"):
                    megszamol+=1
                    print(f"{r[0]}, {r[1]}Ft, {r[2]} darab, szállítás: {r[3]}")
                    file.write(f"/n {r[0]}, {r[1]}Ft, {r[2]} darab, Szállítás: {r[3]}")
            print(f"Az 'R'-rel kezdődő virágok száma: {megszamol}")


viragok= Viragbolt()
viragok.beolvas()
viragok.legdragabb()
viragok.atlag()
viragok.r_kezdodik()

