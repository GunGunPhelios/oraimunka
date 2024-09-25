#1. Feladat
#Pizzarendelő app
#Az S méretű 1500, a M 2000 az L 2500 FT

smallpizza=1500
mediumpizza=2000
largepizza=2500

pizza=input ("Válassz egy pizza méretet(S ,M ,L)")
if pizza=="S":
    price += smallpizza
elif pizza =="M" :
    price += mediumpizza
elif pizza=="L" :
     price += largepizza
else:
   print("Nem helyes értéket adtál meg.")
print(f"Az általad választott pizza ára:{price} Ft")




sajt = 300
sonka = 200
kukorica = 150
feltét=input("Válassz feltétet (sajt,sonka, kukorica):")
if feltét == "sajt":
    price += sajt
elif feltét == "sonka" :
    price += sonka
elif feltét == "kukorica":
    price += kukorica

    print(f"a fizetendő összeg {price} ft")




szam= 1 
while szam <= 10:
    print(szam)
    szam+=1