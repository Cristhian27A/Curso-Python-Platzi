'''
dict = {} # sintaxis normal
for i in range(1,5):
     dict[i] = i * 2

print(dict)

dict_v2 = {i: i * 2 for i in range(1,5)} #sintaxis en una sola linea 
print(dict_v2)
'''

'''
import random
countries = ['col', 'mex', 'bol', 'pe']
population = {}
for country in countries:
  population[country] = random.randint(1,100)

  print(population)


population_v2 = {country: random.randint(1,100) for country in countries}  
print(population_v2)
'''

names = ['cris', 'chester', 'keiser']
ages = [20, 3, 10]
print(list(zip(names, ages)))

#fision de dos listas, en un diccionario
new_dict = {name: age for (name, age) in zip(names, ages)}
print(new_dict)