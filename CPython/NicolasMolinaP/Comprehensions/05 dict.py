names = ['cris', 'chester', 'keiser']
ages = [20, 3, 10]
print(list(zip(names, ages)))

#fision de dos listas, en un diccionario
new_dict = {name: age for (name, age) in zip(names, ages)}
print(new_dict)