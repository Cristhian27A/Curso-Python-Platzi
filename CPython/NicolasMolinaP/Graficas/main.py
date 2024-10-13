import utils
import charts

def run():
    file_name = 'C:/Users/USUARIO/OneDrive/Documentos/CPython/NicolasMolinaP/Graficas/WorldCups.csv'
    
    # Leer los datos del archivo CSV
    data = utils.read_csv(file_name)
    
    # Pedir al usuario que introduzca un país
    country = input('Introduce el nombre del país => ')

    # Obtener los goles por año y país
    goals_by_country = utils.get_goals_by_country(data, country)

    # Separar los datos para el gráfico
    if len(goals_by_country) > 0:
        years, countries, goals = zip(*goals_by_country)  # Extrae años, países y goles

        # Generar gráfico de barras
        charts.generate_bar_chart(years, goals)
    else:
        print(f"No se encontraron datos para {country}")

if __name__ == "__main__":
    run()
