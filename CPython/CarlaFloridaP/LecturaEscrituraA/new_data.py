import csv

new_product = {
    'name': 'Wireless Charger',
    'price': 75,
    'quantity': 100,
    'brand': 'ChargerMaster',
    'category': 'Accessories',
    'entry_date': '2024-07-01'

}

with open('products.csv', mode='a', newline='') as file: #Append, la forma de lectura es sin ningun caracter o espacio
    file.write('\n')
    csv_writer = csv.DictWriter(file, fieldnames= new_product.keys()) #se habre en modo escritura y se le pasa las llaves
    csv_writer.writerow(new_product) #se le dice que se le quiere escribir en una fila