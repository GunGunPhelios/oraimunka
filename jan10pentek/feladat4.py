import csv
print("A program vonalban!")
def sort_csv_by_column(file_path, column_index):
    try:
        print("Fájl beolvasása folyamatban...")
        with open(file_path, mode='r', encoding='utf-8') as file:
            reader = csv.reader(file)
            data = list(reader)
        
       
        if len(data) < 2:
            print("A fájl üres vagy nincs elég adat a feldolgozáshoz.")
            return
        
        
        header = data[0]
        rows = data[1:]
        
        
        try:
            rows.sort(key=lambda x: float(x[column_index]))
        except ValueError:
            print("Az adott oszlop nem tartalmaz csak numerikus értékeket.")
            return
        
        
        print("Rendezett adatok:")
        print(", ".join(header))  
        for row in rows:
            print(", ".join(row))
    
    except FileNotFoundError:
        print(f"Hiba: A fájl nem található: {file_path}")
    except Exception as e:
        print(f"Hiba történt: {e}")

print(f"File elérési út: {"C:\\Users\\Asus-01\\Desktop\\(Monty) Python\\januar\\csüt 09\\pentek 10\\ElectricBoogaloo.csv"}")
file_path = "C:\\Users\\Asus-01\\Desktop\\(Monty) Python\\januar\\csüt 09\\pentek 10\\ElectricBoogaloo.csv" 
column_index = 0  
sort_csv_by_column(file_path, column_index)
