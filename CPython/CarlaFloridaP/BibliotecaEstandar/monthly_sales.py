import csv

# Datos del archivo CSV
data = [
    {"Month": "Enero", "sales": 120},
    {"Month": "Febrero", "sales": 130},
    {"Month": "Marzo", "sales": 150},
    {"Month": "Abril", "sales": 170},
    {"Month": "Mayo", "sales": 160},
    {"Month": "Junio", "sales": 180},
    {"Month": "Julio", "sales": 190},
    {"Month": "Agosto", "sales": 200},
    {"Month": "Septiembre", "sales": 210},
    {"Month": "Octubre", "sales": 190},
    {"Month": "Noviembre", "sales": 185},
    {"Month": "Diciembre", "sales": 210}
]

# Ruta del archivo CSV
csv_file_path = 'ventas.csv'

# Abrir el archivo CSV en modo escritura
with open(csv_file_path, mode='w', newline='') as file:
    writer = csv.DictWriter(file, fieldnames=["Month", "sales"])
    writer.writeheader()  # Escribir los encabezados
    writer.writerows(data)  # Escribir los datos

print(f"Archivo '{csv_file_path}' creado exitosamente.")
