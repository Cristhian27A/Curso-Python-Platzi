import csv

file_path = 'products.csv' #archivo actual
update_file_path = 'products_update.csv' #modificacion

with open('products.csv', mode= 'r') as file: #leer la informacion y anadirla al nuevo csv
    csv_reader = csv.DictReader(file)
    #obtener los nombres de las columnas existente 
    fieldnames = csv_reader.fieldnames + ['total_value'] #de aqui vamos a preguntar los nombres de las columnas

#abrimos en formato escritura
    with open(update_file_path, mode= 'w', newline='') as update_file:
        csv_writer = csv.DictWriter(update_file, fieldnames=fieldnames) #se le manda la informacion que tenemos y el nombre de las columnas
        csv_writer.writeheader() #escribir los encabezados 

        for row in csv_reader:
            row['total_value'] = float(row['price']) * int(row['quantity']) #cantidad de productos por el precio va a ser el total
            csv_writer.writerow(row) #escribir en la columna