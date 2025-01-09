print("Üdvözöljük a gyümölcsboltban!")
print("Kétféle gyümolcs kapható:")
print("1.Alma - 150ft/db")
print("2. Körte - 200 ft/db")

gyumolcsbeker= input("Kérem, válassza ki a gyümölcsöt! (alma/körte):")
db= int(input("Kérem, adja meg hány darabot szeretne vásárolni: "))

if gyumolcsbeker == "alma":
    eredmeny=db*150
if gyumolcsbeker== "körte":
    eredmeny== db*200

print(f"A választott gyümölcs: {gyumolcsbeker}")
print(f"A mennyiség: {db} darab")
print(f"Fizetendő összeg: {eredmeny} Ft.")
