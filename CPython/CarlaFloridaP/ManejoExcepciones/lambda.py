add = lambda a, b: a + b
print(add(10,4))

multiply = lambda a, b: a * b
print(multiply(80,5))

#Cuadrado de cada numero
numbers = range(11)
squared_numbers = list(map(lambda x: x**2, numbers)) #map es 
print("Cuadrados:", squared_numbers )

#Pares
even_numbers = list(filter(lambda x: x%2 == 0, numbers)) # "filters" se utiliza para seleccionar valores si se cumple la funcion
print("Pares:", even_numbers)