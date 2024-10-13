import matplotlib.pyplot as plt

# Gráfico de barras (años vs goles)
def generate_bar_chart(years, goals):
    plt.bar(years, goals)
    plt.xlabel('Year')
    plt.ylabel('Goals Scored')
    plt.title('Goals Scored in the World Cup by Year')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()

# Gráfico circular de goles por país
def generate_pie_chart(countries, goals):
    plt.pie(goals, labels=countries, autopct='%1.1f%%', startangle=140)
    plt.title('Percentage of Goals Scored by Country')
    plt.show()
