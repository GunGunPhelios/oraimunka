#1.Feladat
#Készíts egy programot amivel a megadott listából ki kell választani melyek azok a szavak,
#amelyek hosszúságának az értéke 5 és ki kell íratni a konzolra melyek ezek a szavak 
#és hány darab van belőlük.

szavak = [
    "alma", "asztal", "doboz", "ceruza", "egér", "fotel",   # 5 betűs szavak (azonos hosszúságú)
    "szék", "pohár", "táblázat", "könyv", "kulcs", "karkötő",
    "mobiltelefon", "számítógép", "egérpad", "monitor", "hangszóró", "szék",
    "asztalterítő", "függöny", "szőnyeg", "párna", "papucs", "cipőfűző",
    "naptár", "hűtőszekrény", "mosogatógép", "főzőlap", "mikrohullámú",
    "nyomtató", "scanner", "projektor", "távirányító", "szendvics",
    "tolltartó", "jegyzetfüzet", "irattartó", "mappa", "papír",
    "töltőtoll", "hegyező", "ragasztószalag", "füzet", "kapocs",
    "toll", "filctoll", "színesceruza", "vonalzó", "radír"
    ]

    
otbetusszavak = [szo for szo in szavak if len(szo) == 5]

print("ötbetűs szavak: ")
for szo in otbetusszavak:
    print(szo)

print(f" összesen {len(otbetusszavak)} szó található.")


#2.Feladat
#Kérj be születési évszámokat és számold ki a kort és azt add a listához. 
#Írd ki a konzolra, hány db év szerepel és melyik a legnagyobb kor a listában.

from datetime import datetime as dt
korok=[]

while True:
    ev= input("Kérek egy évszámot: ")
    ev=int(ev)
    taktikaikerdes=input("Szeretnél még évet megadni?")
    if taktikaikerdes != 'i':
        break
kor = dt.now().year - ev
korok.append(kor)

print(f"Összesen {len(korok)} db év szerepel a listában.")
print(f"A legnagyobb kor: {max(korok)}")



