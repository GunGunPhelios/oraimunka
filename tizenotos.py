szemely= int(input("Hány személyre lesz a foglalás?(felnőtt): "))
nap = input("Hány napra foglal szállást: ")
gyerek= int(input("Hány kiskorú lenne: "))

if nap .isdigit():
    nap= int(nap)
    if nap> 0:
        if gyerek <= 2:
             osszeg= (nap * szemely * 5000) -(gyerek*700)
             megad= True
        elif gyerek >= 3:
            osszeg= (nap * szemely * 5000)-(gyerek*1000)
            megad=True
        elif gyerek == 0:
             osszeg= (nap * szemely * 5000)
             megad=True
    else: print("0-nál kisebb számot adtál meg.")
else:
    print("Nem számot adtál meg vagy kevesebb mint 0")
print(f"A fizetendő összeg: {osszeg} ft")

#kérjen be a program 3 virágot, vagy rózsa, vagy tulipán vagy liliom
#hány szálat szeretne a user 
# 0-nál kisebb esetén addig kérje amíg legalább egyet ír be.
# 1 db rózsa: 500ft 1db tulipán 400ft 1 db liliom 300 ft
# írja ki a program a végösszeget

rose= 500
Bouquet= int(input("Hány szál virágot szeretnél?" ))
ár= rose *Bouquet
if rose== 0:
    print("0nál kisebb számot adtál meg.")

