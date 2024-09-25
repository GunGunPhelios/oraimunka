import datetime as dt

today= dt.date.today()
birthdate= dt.date(2002,11,11)

deltaage=(today- birthdate)
days=deltaage.days
years= days //365

months= (days % 365) // 30

print(f"Te ennyi {years} éves vagy és {months} hónapos.")