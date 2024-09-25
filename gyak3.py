szam= False
evszamok=[]
while not szam:
    evszam= input("Adj meg egy évszámot: ")
    if evszam. isdigit():
        evszam=int(evszam)
        evszamok.append(evszam)
        valasz= input("Szeretnél még évszámot hozzáadni?"). lower()
        if valasz != "i": 
            szam= True
else:
    print("Nem számot adott meg.")
legidosebb = 0
for kor in evszamok:
    ev= 2024-kor
if ev > legidosebb:
    legidosebb+=ev
print(f"A legidősebb:{legidosebb}")