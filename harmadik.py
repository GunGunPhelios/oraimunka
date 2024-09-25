import datetime as dt
mainap = dt.date.today()
szuletesidatum= dt.date(2002,11,11)


delta_kor = mainap - szuletesidatum
delta_kor_nap= delta_kor.days
ev = delta_kor_nap//365
honap = (delta_kor_nap %365) //30
print (f"Te ennyi {ev} éves vagy és {honap} hónapos")

print