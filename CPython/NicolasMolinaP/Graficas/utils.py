import csv

# Función para obtener los goles anotados por año y país
def get_goals_by_country(data, country):
    result = list(filter(lambda item: item['Country'] == country, data))
    return [(item['Year'], item['Country'], item['GoalsScored']) for item in result]

# Leer el archivo CSV
def read_csv(file_name):
    data = []
    with open(file_name, mode='r') as file:
        csv_reader = csv.DictReader(file)
        for row in csv_reader:
            data.append(row)
    return data

