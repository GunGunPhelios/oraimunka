class Zoldsegek:
    def __init__(self):
        self.lista=[]
    
    def beolvas(self): 
        with open("zoldsegek.txt", "r", encoding="UTF-8") as file:
            adatok= file.readlines()

            for adat in adatok:
                adat= adat.strip()
                adat= adat.split(";")

                zoldseg= adat[0]
                tonna= int(adat[1])
                ar= int(adat[[2]])
                ev= int(adat[3])
                self.lista.append([zoldseg,tonna,ar,ev])
            for list in self.lista:
                print(f"{list[0]}- {list[1]} tonna - {list[2]} Ft/kg- {list[3]}")


    def termesek_2015utan(self):
        for termes in self.lista:
            if termes[3]>2015:
                print(f"{termes[0]}- {termes[1]} tonna - {termes[2]} Ft/kg- {termes[3]}")

    def legolcsobb(self):
        legolcsobb=float("inf")
        legolcsobbzoldség= ""
        print("A legolcsóbb zöldség:")
        for olcso in self.lista:
            if olcso[2] < legolcsobb:
                legolcsobb=olcso[2]
                legolcsobbzoldség= olcso[0]
        print(f"{legolcsobbzoldség} - {legolcsobb} Ft/kg.")

    def paprikaval_kezdodo_szavak(self):
        with open("Paprika_zoldsegek.txt", "W", encoding="UTF-8")
            megszam=0
            print("---------------------------")
            for kezdodik in self.lista:
                


etelek=Zoldsegek
etelek.beolvas()

