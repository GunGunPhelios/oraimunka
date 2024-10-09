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
