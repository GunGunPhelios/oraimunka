import random
allatok= []
print("Add meg a 3 kedvenc állatodat:")
db=0
while True:
    allat=input("Adja meg a kedvenc állatot:")
    allatok.append(allat)
    db+=1
    print(f"{db} állat került hozzáadásra a listához.")
    if len(allatok)==3:
        break
for animal in allatok:
    print(",".join(map(str,allatok)))

kivalasztottallat=random.choice(allatok)
print(f"A kiválasztott kedvenc állat: {kivalasztottallat}")