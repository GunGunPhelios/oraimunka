tabornev= input("Adja meg a tabor nevet: ")

kaloriak=[]
db=1
while True:
    kaloria= int(input("Adjon meg egy napi kalóriaérteket(jelenlegi adatok száma:{db} ) "))
    kaloriak.append(kaloria)
    db=+1

    if db> 5:
        kerdes= input("Szeretne még kaloriamennyiséget hozzáadni? (i/n):").lower
        if kerdes=="n":
            break

print(f"Tábor neve: {tabornev}")
print(f"Átlagos elégetett kalória naponta: {sum(kaloriak) /len(kaloriak)}")