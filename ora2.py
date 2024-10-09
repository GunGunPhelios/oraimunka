import random
import string
nevek=['Anna', 'Béla', 'Csilla', 'Dávid', 'Emma']
nev= random.choice(nevek)
print(f"A választott név:{nev}")
print(f"A választott nevek: {random.sample(nevek,2)}")

alany= ['A macska', 'A kutya', 'A kisfiú', 'A tanár']
ige= ['fut', 'ugrik', 'alszik', 'Játszik',]
targy= ['a labdával', 'a fűben', 'a barátokkal', 'A házban']
print(f"{random.choice(alany)} {random.choice(ige)} {random.choice(targy)}")


karakterek= string.ascii_letters + string.digits
jelszó=".".join(random. choice(karakterek) for i in range (8))
print(jelszó)


lista=['kő', 'papír', 'olló',]
gep= random.choice(lista)
user= input("válassz egyet: kő, papír, olló:")
if user == gep:
    print("Döntetlen")
elif user == "kő" and gep == "olló" or user =="olló" and gep =="papír" or user == "Papír" and gep == "kő":
    print("Győztél.")
else:
    print("Vesztettél.")

print(f"A gép választotta {gep}, választásod: {user}")
#


szamok= []

while len(szamok) <= 15:
    szam=random.randint(1,200)
    if szam % 2 == 0:
        szamok.append(szam)
print(f"A lista hossza: {len(szamok)}")
print(';'. join(map(str,szamok)))

with open("data.txt", "w") as file:
    file.write(';'. join(map(str,szamok)))
    for i in range(10):
        