#1.
szam1= 5
szam2= 10
osszeg= szam1 + szam2
print(osszeg)


#2.

def legnagyobb(a,b,c):
    return max (a,b,c)

print(legnagyobb(10,15,5))

#3 paros paratlan
def paros(a):
    if a %2 == 0:
        return "Páros"
    else:
        return "Páratlan"

print(paros(5))
#4
def szoveghossz(s):
    return len(s)
print(szoveghossz("Hello"))


#5 
def listaosszeg(alt):
    return sum(alt)


#6
gyumolcsok={
    "alma": 200,
    "banán": 250,
    "cseresznye": 300
}


print(f"1.feladat{gyumolcsok}" )

#2
gyumolcsok["szőlő"]= 250
print (f"2.feladat {gyumolcsok}")
#3
print(f"3.feladat:{gyumolcsok.keys()} ")
#4
print(f"4.feladat: {gyumolcsok.values()} ")
#5
print(f"5.feladat: {sum(gyumolcsok.values())}")

