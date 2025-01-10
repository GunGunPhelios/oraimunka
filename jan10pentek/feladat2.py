import csv

def read_csv_and_search(file_path):
    try:
        
        with open(file_path, mode='r', encoding='utf-8') as file:
            reader = csv.reader(file)
            data = list(reader)

        
        print(f"A fájl sorainak száma: {len(data)}")

        
        print("\n2.es feladat: Az első 5 sor:")
        for row in data[:5]:
            print(row)

       
        search_value = input("\nAdj meg egy értéket, amit keresni szeretnél: ").strip()
        found = False

        
        for row in data:
            if search_value in row:
                found = True
                print(f"Találat: Az érték '{search_value}' szerepel a következő sorban: {row}")
        
        if not found:
            print(f"Az érték '{search_value}' nem található a fájlban.")

    except FileNotFoundError:
        print(f"Hiba: A fájl nem található: {file_path}")
    except Exception as e:
        print(f"Hiba történt: {e}")


file_path = "C:\\Users\\Asus-01\\Desktop\\(Monty) Python\\januar\\csüt 09\\pentek 10\\Mockaroo.csv" 
read_csv_and_search(file_path)
