from datetime import datetime as dt
class member:
    "Create a new Member"

    #Osztálynak a konstruktora
    def __init__(self, uname, fname):
        #Osztály attribútumai
        self.username=uname
        self.fullname=fname
        self.date_joined= dt.today
        self.is_active=True
    def show_datejoined(self):
        return f"{self.fullname} joined on {self.date_joined}"

newguy= member("Rambo", "Rocco Moe")
print(newguy)
print(newguy.username)
print(newguy.fullname)
print(type(newguy))

newguy.username= "Princess"
print("Username:", newguy.username)
print("Full name", newguy.fullname)
print("Joined:", newguy.show_datejoined())
print("Active:", newguy.is_active)

newguy2= member("John", "Doe")
newguy3= member("Jane", "Doe")
guyslist= member ("Rambo", "Rocco Moe"), member("John", "Doe"), member("Jane", "Doe")
print(newguy2)
print(newguy3)
print(guyslist)