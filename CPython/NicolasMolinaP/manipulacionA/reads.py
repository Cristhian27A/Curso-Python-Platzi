import csv

#mostrar la informacion por columnas
with open('WorldCups.csv', mode='r') as file:
    csv_reader = csv.DictReader(file)
    for row in csv_reader:
        print(f"Año: {row['Year']}, Pais: {row['Country']}, Campeon: {row['Winner']}")