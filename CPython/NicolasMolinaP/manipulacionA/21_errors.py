# print(0 / 0)
# print(result)
print('Hola')

suma = lambda x,y: x + y
assert suma(2,2) == 4 #te indica que esta funcion no esta funcionando como deberia

print('Hola 2')

age = 10
if age < 18:
    raise Exception('No se permite menores de edad')#para lanzar un error

