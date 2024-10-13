import utils
import charts

def run():
    file_name = 'C:/Users/USUARIO/OneDrive/Documentos/CPython/NicolasMolinaP/Graficas/WorldCups.csv'
    data = utils.read_csv(file_name)
    
    # Obtener el conteo de ganadores
    winner_counts = utils.get_winners(data)
    
    # Obtener los países y los conteos de victorias
    countries = list(winner_counts.keys())
    percentages = list(winner_counts.values())
    
    # Generar la gráfica de pastel
    charts.generate_pie_chart(countries, percentages)

if __name__ == '__main__':
    run()
