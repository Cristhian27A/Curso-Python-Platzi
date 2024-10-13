import json

file_path = 'products.json'

new_product = {
    "name": "Wireless Charger",
    "price": 75,
    "quantity": 100,
    "brand": "ChargeMaster",
    "category": "Accessories",
    "entry_date": "2024-07-01"
}
# abrimos en modo lectura
with open(file_path, mode='r') as file:
    products = json.load(file)

#agregamos nuevo producto
products.append(new_product)

# modo escritura 
with open(file_path, mode='w') as file:
    json.dump(products, file, indent=4) # se invoca el metodo dump