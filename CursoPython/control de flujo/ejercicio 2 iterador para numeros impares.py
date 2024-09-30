# Se crea un iterador para los numeros impares

#su Limite
limit = 10

#Creamos un iterador
odd_itter = iter(range(1,limit+1,2))

#Usamos el iterador
for num in odd_itter:
    print(num)