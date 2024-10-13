# convertir Archivo Json a csv
import json
import csv
# Paso 1: leemos el archivo JSON
ruta = "C:\\Users\\USUARIO\\OneDrive\\Documentos\\CPython\\Carla Florida - Curso de python\\Lectura y escritura de archivos\\archivo.json"
with open(ruta, mode='r') as json_file:
    data = json.load(json_file)

# Paso 2: escribimos el archivo csv
ruta2 = "C:\\Users\\USUARIO\\OneDrive\\Documentos\\CPython\\Carla Florida - Curso de python\\Lectura y escritura de archivos\\archivo.csv"
with open(ruta2, mode='w', newline='') as csv_file:
    csv_writer = csv.DictWriter(csv_file, fieldnames=data[0].keys())# escribir esa lista en formato csv
    csv_writer.writeheader()  # encabezados del csv 
    csv_writer.writerows(data)  # Escribimos las filas del csv