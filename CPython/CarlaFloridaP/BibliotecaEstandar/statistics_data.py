import statistics
import csv

# Leer los datos de ventas mensuales desde un archivo csv
monthly_sales = {}
with open('monthly_sales.csv', mode='r') as file:
    reader = csv.DictReader(file)
    for row in reader:
        month = row['Month']  # Asegúrate de que el encabezado sea "Month" y no "month" según tu archivo CSV
        sales = int(row['sales'])
        monthly_sales[month] = sales

# Extraer los valores de ventas
sales = list(monthly_sales.values())

# Hallar la media
mean_sales = statistics.mean(sales) 
print(f"La media es: {mean_sales}")

# Hallar la mediana
median_sales = statistics.median(sales)
print(f"La mediana es: {median_sales}")

# Hallar la moda (si existe)

#Si no hay un valor que aparezca mas de una vez en los datos, statistics.mode() puede lanzar una excepcion
try: # Se agrega un bloque try-except para manejar eso
    mode_sales = statistics.mode(sales)
    print(f"La moda es: {mode_sales}")
except statistics.StatisticsError: 
    print("No hay moda en los datos de ventas.")

# Desviación estándar
stdev_sales = statistics.stdev(sales)
print(f"La desviación estándar es: {stdev_sales}")

# Hallar la varianza
variance_sales = statistics.variance(sales)
print(f"La varianza es: {variance_sales}")

# Rango de ventas (máximo menos mínimo)
max_sales = max(sales)
min_sales = min(sales)
range_sales = max_sales - min_sales
print(f'Rango de ventas: {range_sales}')
