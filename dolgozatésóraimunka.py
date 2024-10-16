#Számoljuk meg a pontszámok átlagát és írjuk ki a konzolra.
#Növekvő sorrendbe írjuk ki a pontszámokat.
pontszamok = [
    95, 78, 84, 62, 47, 88, 93, 71, 56, 82,
    65, 90, 74, 60, 85, 79, 68, 91, 73, 58,
    100, 81, 77, 66, 49, 53, 69, 94, 87, 61,
    80, 55, 76, 67, 48, 86, 92, 72, 59, 83,
    64, 50, 99, 75, 89, 54, 63, 57, 70, 52]

print(f"Az átlag: {sum(pontszamok)/len(pontszamok)}")
pontszamok.sort()
print(pontszamok)

#2.Feladat
#Úgy írjuk ki a lista tartalmát, hogy csak a páros indexű szavak kerüljenek kiírásra a konzolon, 
#vesszővel elválasztva.




#3.Feladat
#Készíts egy programot, ahol csak azok a számok kerülnek a listába, amik oszthatóak 3-al.
#És addig kell a listához adni, ameddig a felhasználó szeretne újabb számot megadni, de legalább 5db-ot.
#Ki kell írni a list hosszat és melyik a legkisebb szám a listában.

harommaloszthato=[]
megad= False
while not megad:
    szam=int(input("Adj meg egy számot: "))
    if szam % 3 ==0: 
        harommaloszthato.append(szam)
    valasz= input("Szeretnél még számot megadni?")
    if valasz != "i":
        megad=True

print(f"A lista hossza: {len(harommaloszthato)}")
print(f"A legkisebb szám a listában: {min(harommaloszthato)}")

#4.Feladat
#Kérjünk be szavakat, de csak azokat adjuk a listához, ami legalább 4 karaktert tartalmaznak.
#Majd írjuk ki pontosvesszővel elválasztva a szavakat.
#Azt is írjuk ki melyik a legrövidebb szó.
words = []
hozzaad=False
while not hozzaad:
    word= input("Adj meg szavakat: ")
    if len(word) > 4 and word not in words:

