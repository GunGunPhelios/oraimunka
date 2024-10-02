pluszpénz=False
bevasarlas=[]
while not pluszpénz:
    termek=int(input("Add meg a termék összegét: "))
    if termek > 0:
        bevasarlas.append(termek)
        kerdes=input("Szeretnél még hozzáadni termékeket a listádhoz? ").lower()
        if kerdes!= "i":
            pluszpénz=True
print(f"A legnagyobb összeg: {max(bevasarlas)}")
print(f"A legkisebb összeg: {min(bevasarlas)}")
print(f"Az összeg: {sum(bevasarlas)}")
huszonotkalatt={}
for huszonot in bevasarlas:
    if sum(huszonotkalatt) + huszonot < 25000:
        huszonotkalatt.append(huszonot)
print(f"{len(huszonotkalatt)} terméket tudnánk venni 25k alatt.")
