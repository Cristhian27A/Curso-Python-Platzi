file = open('./text.txt')
#print(file.read()) #leer todo el texto directamente

#leer linea por linea
#print(file.readline())
#print(file.readline())
#print(file.readline())
#print(file.readline())

for line in file:
    print(line)


file.close() #se cierra la lectura, por el read ocupa espacio en memoria

#es mas recomendable usar el with open
with open('./text.txt') as file:
    for line in file:
        print(line)
        #esto despues de leer lo cierra automaticamente