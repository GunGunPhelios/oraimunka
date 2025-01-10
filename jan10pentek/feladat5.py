import csv
import statistics
print("A fájl aktív!")
def generate_statistics(file_path, column_index):
    try:
        print("A fájl leolvasása folyamatban...")
        with open(file_path, mode='r', encoding='utf-8') as file:
            reader = csv.reader(file)
            data = list(reader)

        
        if len(data) < 2:
            print("A fájl üres vagy nincs elég adat a feldolgozáshoz.")
            return
        
        
        header = data[0]
        rows = data[1:]
        
     
        if column_index >= len(header):
            print(f"Hiba: A megadott oszlop index ({column_index}) nem létezik a fájlban.")
            return
        
        
        values = []
        for row in rows:
            try:
                values.append(float(row[column_index]))  
            except ValueError:
                continue  
        
        
        if len(values) == 0:
            print("A megadott oszlopban nincsenek numerikus adatok.")
            return

       
        count = len(values)
        mean = statistics.mean(values)
        minimum = min(values)
        maximum = max(values)
        stdev = statistics.stdev(values) if count > 1 else 0 

        
        print("Statisztikai eredmények:")
        print(f"Adatok száma: {count}")
        print(f"Átlag: {mean:.2f}")
        print(f"Minimum: {minimum:.2f}")
        print(f"Maximum: {maximum:.2f}")
        print(f"Szórás: {stdev:.2f}")
    
    except FileNotFoundError:
        print(f"Hiba: A fájl nem található: {file_path}")
    except Exception as e:
        print(f"Hiba történt: {e}")

print("A file elérési útvonala: C:\\Users\\Asus-01\\Desktop\\(Monty) Python\\januar\csüt 09\\pentek 10\\Stat.csv")
file_path = "C:\\Users\\Asus-01\\Desktop\\(Monty) Python\\januar\csüt 09\\pentek 10\\Stat.csv"  
column_index = 4  
generate_statistics(file_path, column_index)
