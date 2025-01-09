mertekegyseg=input("Milyen mértékegységre szeretne átváltani?(liter/dl:)")
mennyiség=int(input("Adja meg az átváltandó mennyiséget: "))

if mertekegyseg =="l":
    eredmeny= mennyiség*10
    print(f"Az eredmény: {round(eredmeny)} dl.")

elif mertekegyseg == "dl":
    eredmeny= mennyiség/10
    print(f"Az eredmény: {round(eredmeny)} l.")
