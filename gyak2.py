vasarlas= int(input("add meg a vásárlas összegét."))
if vasarlas< 10000:
    print("Nincs kedvezmény")
elif vasarlas < 20000:
    kedvezmeny= 0.1
elif vasarlas> 20000:
    kedvezmeny= 0.2
vegosszeg= vasarlas- (vasarlas*kedvezmeny)
print(f"A kedvezmény összege: {round(vasarlas* kedvezmeny)} Ft")
print(f"A vásárlás végösszege:{round(vegosszeg)} Ft")