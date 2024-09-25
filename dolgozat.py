berlet= int(input("Add meg hány napig szeretnél autót bérelni."))

if berlet <= 3:
    ar= 5000
elif berlet <=7:
    ar= 4500 
else: 
    ar= 4000 
print(f"Ennyibe kerül a bérlésed:{round(berlet*ar)} Ft ")