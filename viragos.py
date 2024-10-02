#kérjen be a program 3 virágot, vagy rózsa, vagy tulipán vagy liliom
#hány szálat szeretne a user 
# 0-nál kisebb esetén addig kérje amíg legalább egyet ír be.
# 1 db rózsa: 500ft 1db tulipán 400ft 1 db liliom 300 ft
# írja ki a program a végösszeget
petal= False
while not petal:
        virag= input("Válassz egy virágot: R,T,L,: ").upper()
        db=int(input("Hány szál virágot szeretnél?) "))

        if db.isdigit():
            db= int(db)
        if db > 0:
                if virag == "R":
                    osszeg= db*500
                    petal=True
                    print(f"Fizetendő összeg:{osszeg} FT")
                elif virag == "T":
                    osszeg= db *400
                    petal=True
                    print(f"Fizetendő összeg:{osszeg} FT")
                elif virag== "L":
                    osszeg= db *300
                    petal=True
                    print(f"Fizetendő összeg:{osszeg} FT")
else:
     print("Nem számot adtál meg.")

