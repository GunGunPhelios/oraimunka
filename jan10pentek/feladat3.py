import csv
print("A program fut!")
def find_min_max_in_csv(file_path):
    print("File megnyitása...")
    try:
        numeric_values = []

       
        with open(file_path, 'r', encoding='utf-8') as file:
            reader = csv.reader(file)
            for row in reader:
                for value in row:
                    try:
                        numeric_values.append(float(value))
                    except ValueError:
                        continue

        
        if not numeric_values:
            print("A fájl nem tartalmaz numerikus adatokat.")
            return

       
        min_value = min(numeric_values)
        max_value = max(numeric_values)

        print(f"A legkisebb szám a fájlban: {min_value}")
        print(f"A legnagyobb szám a fájlban: {max_value}")

    except FileNotFoundError:
        print(f"Hiba: A fájl nem található: {file_path}")
    except Exception as e:
        print(f"Hiba történt: {e}")

print(f"File elérési út: {"C:\\Users\\Asus-01\\Desktop\\(Monty) Python\\januar\\csüt 09\\pentek 10\\Boogaloo.csv"}")
file_path="C:\\Users\\Asus-01\\Desktop\\(Monty) Python\\januar\\csüt 09\\pentek 10\\Boogaloo.csv" 
find_min_max_in_csv(file_path)