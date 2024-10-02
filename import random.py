
import random
gep= random.randint(1,10)
w=False
while not w:
    gep= random.randint(1,10)
    szam= int(input("Adj meg egy számot 1 ÉS 10 között:"))


    if gep > szam: 
        print("Kisebb számot adtál meg.")     
    elif gep < szam:
        print("Nagyobb számot adtál meg.")    
    elif gep == szam:
        print("Victory.")
        w=True
        
print(f"A gép által megadott szám {gep}, szam: {szam}")