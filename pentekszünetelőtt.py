import datetime as dt
class Member:

    def __init__(self,lastname, firstname):
        self._lastname= lastname
        self._firstname= firstname

        self.date_joined= dt.date.today()

    def join_date(self):
        return f"{self.date_joined} joined to the workspace."

    def is_active(self):
        return "Igen" if self.is_active else "Nem"
    def member_since(self):
        return "Igen" if self.is_active else "Nem"


@property
def is_active(self)
    return self.is_active


@is_active.__setter
def is_active(self,value):
    self.is_active=value
    
newmember= Member("Rocco", "Moe")

print(newmember._lastname) 
print(newmember._firstname)
print(f"isActive változó lekérése @propertyvel: {newmember.is_active}")
newmember.is_active=False
print(f"Aktív tag-e: {newmember.member_since()}")

newmember2= Member("John", "Doe")
newmember2._firstname="John"
newmember2._lastname="Doe"

print(f"Vezetéknév: {newmember2._lastname}")
print(f"Keresztnév: {newmember2._firstname}")
print(newmember.join_date())
print(newmember.is_active())
   