# == (egyenlőség vizsgálata)
#!= (nem egyenlő)
#=(értékadás)
#<(kisebb mint)
#>(nagyobb mint)
#<=(kisebb vagy egyenlő)
#=>(nagyobb vagy egyenlő)

# and, or, not
#if feltétel
#csinálj valamit

sun= "up"
if sun== "down" :
    print("Good night!")
print("I'm here!")

total= 100
salestaxrate= 0.065
taxable= False
if taxable:  
    print(f"Subtotal: ${total:.2f}")
    salestax=total*salestaxrate
    print(f"Sales Tax: ${salestax:.2f}")
    total= total + salestax


print(f"Total: ${total:.2f}")

import datetime as dt
now= dt.datetime.now()

if now.hour<12:
    print("good morning")
else:
    print("good afternoon)")

print("Blehblebleh")


#light_color= "kék"
#if light_color =="green":
 #   print("Go!")
#elif light_color == "yellow":
 #       print("Start your engines!")
#else:
 #       print("Nem látod a színeket.")



#age= 30
#if age< 18:
 #   drink= "milk"
#elif age>= 18 and age >80:
 #   drink ="beer"
#else:
 #   drink=" Orange juice"
#print("You can drink" + drink)

#for x in range(1, 8):
#    print(x, end = ", ")
#word="elefant"
#for x in "elefant":
 #   print(x)



#answers = ["A", "C", "B", "D"]
#or a in answers:
  #  if a == "B":
  #      print("Incomplete")
   #     break
   # print(a)

#print("Véget ért az ellenőrzés")




#for kulso in ["Elso", "Masodik", "Harmadik"]:
   # print(kulso)
#
  #  for belso in range(1,4):
 #       print( f"/t- {belso}")


#print("Mind2 ciklus befejezve!")




szamlalo=1

while szamlalo< 150:
    print(str(szamlalo) + "= " + chr(szamlalo))
    szamlalo= szamlalo + 1 






