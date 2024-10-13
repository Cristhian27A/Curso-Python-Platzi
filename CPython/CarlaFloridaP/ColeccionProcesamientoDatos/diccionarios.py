numbers = {1:"uno", 2:"dos", 3:"tres"}
print(numbers[2])
information = {"nombre": "Cely",
               "Apellido": "Dominguez",
               "Altura": 1.57,
               "Edad": 19}
print(information)
del information["Edad"]
print(information)
claves = information.keys() #"keys" para ver cuales son las claves
print(claves)
#print(type(claves)) 
values = information.values() # "values" para ver cuales son los valores
print(values)
pairs = information.items() #"intems" es para ver los pares de valor
print(pairs)
contacts = {"Cristhian": {"Apellido": "Alonso",
               "Altura": 1.65,
               "Edad": 20},
                "Randoll": {"Apellido": "Alonso",
               "Altura": 1.60,
               "Edad": 33}}
print(contacts["Cristhian"])