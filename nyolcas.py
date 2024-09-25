valtozo= 1 #int egész
valtozo2 = 2.5 #float tört
valtozo3 = "Csillag Patrik"
valtozo4= 'Patrik'
valtozo5= False
valtozo6= True

#print(type(valtozo))
#print(type(valtozo2))
#print(type(valtozo3))
print(type(valtozo4))
print(type(valtozo5))
print(type(valtozo6)) 


szam1= 30
szam2= 15
print(f"{szam1} + {szam2} = {szam1+szam2}")
print(f"{szam1} - {szam2} = {szam1-szam2}")
print(f"{szam1} * {szam2} = {szam1*szam2}")
print(f"{szam1} / {szam2} = {szam1/szam2}")
print(f"{szam1} % {szam2} = {szam1%szam2}")


firstname= "Patrik"
lastname= "Grósz"

print(firstname, lastname)
print(firstname + " " + lastname)
print(f"{firstname} {lastname}")


x= 50
if x ==10:
    print("x értéke 10", x)
else:  
    print( "x értéke", x)

import datetime as dt
ma= dt.date.today ()
print(ma)
print(ma.month)
print(ma.day)
print(ma.year)

ejfel= dt.time()
print(ejfel)

most= dt.datetime.now()
print(most)

ujev= dt.datetime(2024,12,31,23,59,59)
print(ujev)

kettokozott= most - ujev
print(kettokozott)

egyhet = dt.timedelta(days=7)

print(most+egyhet)