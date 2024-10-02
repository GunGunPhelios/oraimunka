ujabbosszeg= False
shop= []
while not ujabbosszeg:
    termek = int(input(" Add meg a termék összegét "))
    if termek> 0: 
        shop.append(termek)

        valasz=input("Szeretnél-e terméket hozzáadni a listához?").lower()
        if valasz !="i":
            ujabbosszeg=True
tizezeralatt= []
for i in shop:
    if sum(tizezeralatt) + i < 10000:
        tizezeralatt.append(i)
        print(f" A tizezeralatt lista összege {sum(tizezeralatt)}")
print(f"A legnagyobb összeg: {max(shop)})")
print (f"A legkisebb összeg: {min(shop)})")
print(f"A lista elemeinek száma: {len(shop)}")
print(f"A teljes lista tartalmának összege: {sum(shop)} ft")