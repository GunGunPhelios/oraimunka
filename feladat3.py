szam= int(input("Kérek egy számot: "))
osszeg = 0
for i in range(1, szam+1):
    osszeg+=i
print("Összeg:",osszeg)