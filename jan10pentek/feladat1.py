import csv


def read_mockaroo_file(file_path):
    try:
        with open(file_path, mode='r', encoding='utf-8') as file:
            reader = csv.reader(file)
            header = next(reader)  
            print(f"Oszlopnevek: {header}")
            print("\n1.feladat: Az első 5 adat:")
            for i, row in enumerate(reader):
                print(row)
                if i == 4:  
                    break
    except FileNotFoundError:
        print(f"Hiba: A fájl nem található: {file_path}")
    except Exception as e:
        print(f"Hiba történt: {e}")

file_path = "C:\\Users\\Asus-01\\Desktop\\(Monty) Python\\januar\\csüt 09\\pentek 10\\Mockaroo.csv" 
read_mockaroo_file(file_path)
