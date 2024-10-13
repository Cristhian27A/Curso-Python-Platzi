import csv
from collections import Counter

# Función para leer el archivo CSV
def read_csv(file_name):
    data = []
    with open(file_name, mode='r') as file:
        csv_reader = csv.DictReader(file)
        for row in csv_reader:
            data.append(row)
    return data

# Función para contar los ganadores
def get_winners(data):
    winners = [item['Winner'] for item in data]  # Aquí se asume que la columna del ganador se llama 'Winner'
    winner_counts = Counter(winners)  # Usamos Counter para contar las ocurrencias de cada país
    return winner_counts
