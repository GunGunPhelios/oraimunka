import datetime as dt

today= dt.date.today()
print(today)
print(f"Nap:{today.day}")
print(f"Hónap:{today.month}")
print(f"Év: {today.year}")

ido= dt.datetime.now()
print(ido)

ujev= dt.datetime(2024,12,31,23,59)
print(ujev)

mainap= dt.datetime(2024,9,13,23,59)
print(mainap)

napokhatra= mainap - ujev
print(napokhatra)

nap2=dt.date(2024,9,13)
ujertek2=dt.timedelta(days=109)
print(nap2 + ujertek2)
kezdoidopont= dt.datetime(2024,9,13,8,0,0)
befejezesidopont= dt.datetime(2024,9,13,13,30,0)
szamitas=befejezesidopont - kezdoidopont
print(szamitas)
print(type(kezdoidopont))
print(type(befejezesidopont))
print(type(szamitas))

most= dt.datetime.now()
szuletesnap=dt.datetime(2002,11,11,15,30)
kalkulacio= most - szuletesnap
print(kalkulacio)


now= dt.datetime.now()
print(f"{now}")
print(f"{now:%H:%M:%S}")

